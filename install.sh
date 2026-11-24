#!/usr/bin/env bash
# ==============================================================================
# agents-config symlink installer & manager (Bash 3.2+ compatible)
# ==============================================================================
set -euo pipefail

# ------------------------------------------------------------------------------
# 0. Bootstrap Configuration & Logging
# ------------------------------------------------------------------------------
SCRIPT_PATH="${BASH_SOURCE[0]:-}"
REPO_DIR=""
if [ -n "$SCRIPT_PATH" ] && [ -f "$SCRIPT_PATH" ]; then
  REPO_DIR="$(cd "$(dirname "$SCRIPT_PATH")" 2>/dev/null && pwd || echo "")"
fi

DEFAULT_TARGET_REPO="${AGENTS_CONFIG_DIR:-${HOME}/.agents-config}"
AGENTS_CONFIG_BRANCH="${AGENTS_CONFIG_BRANCH:-main}"
AGENTS_CONFIG_REMOTE_URL="${AGENTS_CONFIG_REMOTE_URL:-https://github.com/gdtknight/agents-config.git}"
REMOTE_RAW_URL="https://raw.githubusercontent.com/gdtknight/agents-config/${AGENTS_CONFIG_BRANCH}/install.sh"

COLOR_RESET="\033[0m"
COLOR_GREEN="\033[32m"
COLOR_YELLOW="\033[33m"
COLOR_BLUE="\033[34m"
COLOR_RED="\033[31m"

log_info()   { echo -e "${COLOR_BLUE}[INFO]${COLOR_RESET} $*"; }
log_ok()     { echo -e "${COLOR_GREEN}[OK]${COLOR_RESET} $*"; }
log_dry()    { echo -e "${COLOR_YELLOW}[DRY-RUN]${COLOR_RESET} $*"; }
log_backup() { echo -e "${COLOR_YELLOW}[BACKUP]${COLOR_RESET} $*"; }
log_warn()   { echo -e "${COLOR_RED}[WARN]${COLOR_RESET} $*"; }

BACKUP_BASE="${HOME}/.agents-config_backups"
TIMESTAMP="$(date +%Y%m%d_%H%M%S)"
BACKUP_DIR="${BACKUP_BASE}/backup_${TIMESTAMP}"

DRY_RUN=false
FORCE=false
SKIP_CLI=false

usage() {
  local prog="install.sh"
  if [ -n "$SCRIPT_PATH" ] && [ -f "$SCRIPT_PATH" ]; then
    prog="$(basename "$SCRIPT_PATH")"
  fi

  cat << EOF
Usage: ${prog} [OPTIONS] [MODULE...]

Remote One-Line Quickstart:
  # SDKMAN style
  curl -fsSL ${REMOTE_RAW_URL} | bash
  curl -fsSL ${REMOTE_RAW_URL} | bash -s -- --dry-run

  # Homebrew style
  /bin/bash -c "\$(curl -fsSL ${REMOTE_RAW_URL})"
  /bin/bash -c "\$(curl -fsSL ${REMOTE_RAW_URL})" -- --dry-run

Modules:
  agents            Sync MCP and link Claude, Gemini, Codex + ensure CLIs (Default)
  claude            Link Claude Code configurations (~/.claude)
  gemini            Link Gemini CLI / Antigravity configurations (~/.gemini)
  codex             Link Codex CLI configurations (~/.codex)
  mcp               Synchronize shared/mcp.json across Claude, Gemini/AGY, and Codex
  formatter, docker Build the agents-config-formatter Docker image
  all               Run 'agents' module (Default if no module specified)

Options:
  -n, --dry-run     Preview actions without creating symlinks or modifying files
  -f, --force       Force relink even if destination symlink already points to target
  --skip-cli        Skip automatic CLI installation checks (agy, claude, codex)
  -h, --help        Display this help message and exit

Environment Variables:
  AGENTS_CONFIG_DIR         Target repository directory (Default: ~/.agents-config)
  AGENTS_CONFIG_BRANCH      Git branch for remote install (Default: main)
  AGENTS_CONFIG_REMOTE_URL  Git remote used by web bootstrapper

Examples:
  ${prog} --dry-run
  ${prog} --dry-run --skip-cli
  ${prog} claude gemini
  ${prog} mcp
  ${prog} formatter
EOF
}

bootstrap_remote_repo() {
  log_info "Running via web bootstrapper. Preparing local repository..."

  if ! command -v git >/dev/null 2>&1; then
    if [ "$(uname -s)" = "Darwin" ] && ! xcode-select -p >/dev/null 2>&1; then
      log_warn "'git' is not installed. Run 'xcode-select --install' first, then retry."
    else
      log_warn "'git' is required to clone agents-config but was not found in PATH."
    fi
    exit 1
  fi

  if [ -d "${DEFAULT_TARGET_REPO}/.git" ]; then
    log_info "Existing agents-config repository found at ${DEFAULT_TARGET_REPO}. Pulling latest..."
    git -C "$DEFAULT_TARGET_REPO" pull --ff-only || log_warn "Could not fast-forward ${DEFAULT_TARGET_REPO}; continuing with existing checkout."
  elif [ -e "$DEFAULT_TARGET_REPO" ] && [ -n "$(ls -A "$DEFAULT_TARGET_REPO" 2>/dev/null || true)" ]; then
    log_warn "Target directory exists and is not a git repo: ${DEFAULT_TARGET_REPO}"
    log_warn "Move it aside or set AGENTS_CONFIG_DIR to an alternate path."
    exit 1
  else
    log_info "Cloning agents-config (${AGENTS_CONFIG_BRANCH}) into ${DEFAULT_TARGET_REPO}..."
    mkdir -p "$(dirname "$DEFAULT_TARGET_REPO")"
    git clone --branch "$AGENTS_CONFIG_BRANCH" --single-branch "$AGENTS_CONFIG_REMOTE_URL" "$DEFAULT_TARGET_REPO"
    log_ok "Cloned agents-config into ${DEFAULT_TARGET_REPO}"
  fi

  log_info "Handoff to local installer: ${DEFAULT_TARGET_REPO}/install.sh $*"
  if [ -t 0 ]; then
    exec /bin/bash "${DEFAULT_TARGET_REPO}/install.sh" ${1+"$@"}
  elif (: </dev/tty) 2>/dev/null; then
    exec /bin/bash "${DEFAULT_TARGET_REPO}/install.sh" ${1+"$@"} </dev/tty
  else
    exec /bin/bash "${DEFAULT_TARGET_REPO}/install.sh" ${1+"$@"} </dev/null
  fi
}

# ------------------------------------------------------------------------------
# Core linking & cleanup helpers
# ------------------------------------------------------------------------------
link_target() {
  local src="$1"
  local dst="$2"

  if [ ! -e "$src" ]; then
    log_warn "Source does not exist: $src"
    return 1
  fi

  local dst_dir
  dst_dir="$(dirname "$dst")"

  if [ -L "$dst" ]; then
    local current_target
    current_target="$(readlink "$dst")"
    if [ "$current_target" = "$src" ]; then
      if [ "$FORCE" = true ]; then
        if [ "$DRY_RUN" = true ]; then
          log_dry "Force relink: $dst -> $src"
          return 0
        fi
        ln -sfn "$src" "$dst"
        log_ok "Force relinked: $dst -> $src"
        return 0
      fi
      log_ok "Already linked: $dst -> $src"
      return 0
    else
      if [ "$DRY_RUN" = true ]; then
        log_dry "Relink $dst -> $src (currently points to: $current_target)"
        return 0
      fi
      rm -f "$dst"
      ln -sfn "$src" "$dst"
      log_ok "Updated symlink: $dst -> $src"
      return 0
    fi
  fi

  if [ -e "$dst" ]; then
    if [ "$DRY_RUN" = true ]; then
      log_dry "Backup existing $dst to ${BACKUP_DIR} and link to $src"
      return 0
    fi

    local rel_to_home
    rel_to_home="${dst#"$HOME"/}"
    local backup_target="${BACKUP_DIR}/${rel_to_home}"
    mkdir -p "$(dirname "$backup_target")"
    mv "$dst" "$backup_target"
    log_backup "Backed up: $dst -> $backup_target"

    mkdir -p "$dst_dir"
    ln -sfn "$src" "$dst"
    log_ok "Linked: $dst -> $src"
    return 0
  fi

  if [ "$DRY_RUN" = true ]; then
    log_dry "Create symlink: $dst -> $src"
    return 0
  fi

  mkdir -p "$dst_dir"
  ln -sfn "$src" "$dst"
  log_ok "Created link: $dst -> $src"
}

cleanup_stale_skills() {
  local skills_dir="$1"
  [ -d "$skills_dir" ] || return 0

  local entry
  for entry in "${skills_dir}"/*; do
    if [ -L "$entry" ] && [ ! -e "$entry" ]; then
      if [ "$DRY_RUN" = true ]; then
        log_dry "Remove stale skill dir symlink: $entry"
      else
        rm -f "$entry"
        log_ok "Removed stale skill dir symlink: $entry"
      fi
    fi
  done

  local skill_file
  for skill_file in "${skills_dir}"/*/SKILL.md; do
    if [ -L "$skill_file" ] && [ ! -e "$skill_file" ]; then
      if [ "$DRY_RUN" = true ]; then
        log_dry "Remove stale skill symlink: $skill_file"
      else
        rm -f "$skill_file"
        rmdir "$(dirname "$skill_file")" 2>/dev/null || true
        log_ok "Removed stale skill symlink: $skill_file"
      fi
    fi
  done
}

link_shared_skills() {
  local skills_dir="$1"
  [ -d "${REPO_DIR}/shared/skills" ] || return 0

  local skill_dir
  local skill_name
  for skill_dir in "${REPO_DIR}/shared/skills"/*; do
    if [ -d "$skill_dir" ]; then
      skill_name="$(basename "$skill_dir")"
      link_target "$skill_dir" "${skills_dir}/${skill_name}"
    fi
  done
}

link_agent_skills() {
  local skills_dir="$1"
  [ -d "${REPO_DIR}/shared/agents" ] || return 0

  local agent_md
  local agent_name
  for agent_md in "${REPO_DIR}/shared/agents"/*.md; do
    if [ -f "$agent_md" ]; then
      agent_name="$(basename "$agent_md" .md)"
      link_target "$agent_md" "${skills_dir}/${agent_name}/SKILL.md"
    fi
  done
}

# ------------------------------------------------------------------------------
# Module handlers
# ------------------------------------------------------------------------------
sync_shared_mcp() {
  local mcp_sync="${REPO_DIR}/shared/sync_mcp.py"
  local mcp_src="${REPO_DIR}/shared/mcp.json"
  if [ ! -f "$mcp_sync" ] || [ ! -f "$mcp_src" ]; then
    return 0
  fi
  if ! command -v python3 >/dev/null 2>&1; then
    log_warn "python3 not found; skipping cross-vendor MCP synchronization."
    return 0
  fi

  log_info "Synchronizing shared MCP servers (Claude, Gemini/AGY, Codex)..."
  if [ "$DRY_RUN" = true ]; then
    python3 "$mcp_sync" --dry-run
  else
    python3 "$mcp_sync"
  fi
}

link_claude() {
  log_info "Configuring Claude Code (~/.claude)..."
  if [ "$DRY_RUN" = false ]; then
    mkdir -p "${HOME}/.claude" "${HOME}/.claude/skills"
  fi

  link_target "${REPO_DIR}/shared/INSTRUCTIONS.md" "${HOME}/.claude/CLAUDE.md"
  link_target "${REPO_DIR}/claude/settings.json" "${HOME}/.claude/settings.json"
  link_target "${REPO_DIR}/shared/rules" "${HOME}/.claude/rules"
  link_target "${REPO_DIR}/shared/agents" "${HOME}/.claude/agents"
  link_target "${REPO_DIR}/shared/hooks" "${HOME}/.claude/hooks"

  cleanup_stale_skills "${HOME}/.claude/skills"
  link_shared_skills "${HOME}/.claude/skills"
}

link_gemini() {
  log_info "Configuring Gemini CLI / Antigravity (~/.gemini)..."
  if [ "$DRY_RUN" = false ]; then
    mkdir -p "${HOME}/.gemini/config/skills"
  fi

  link_target "${REPO_DIR}/shared/INSTRUCTIONS.md" "${HOME}/.gemini/GEMINI.md"
  link_target "${REPO_DIR}/shared/rules" "${HOME}/.gemini/config/rules"
  link_target "${REPO_DIR}/shared/agents" "${HOME}/.gemini/agents"
  link_target "${REPO_DIR}/gemini/settings.json" "${HOME}/.gemini/settings.json"
  link_target "${REPO_DIR}/gemini/config.json" "${HOME}/.gemini/config/config.json"
  link_target "${REPO_DIR}/gemini/hooks.json" "${HOME}/.gemini/config/hooks.json"
  link_target "${REPO_DIR}/shared/hooks" "${HOME}/.gemini/config/hooks"
  link_target "${REPO_DIR}/gemini/mcp_config.json" "${HOME}/.gemini/config/mcp_config.json"

  cleanup_stale_skills "${HOME}/.gemini/config/skills"
  link_agent_skills "${HOME}/.gemini/config/skills"
  link_shared_skills "${HOME}/.gemini/config/skills"
}

link_codex() {
  log_info "Configuring Codex CLI (~/.codex)..."
  if [ "$DRY_RUN" = false ]; then
    mkdir -p "${HOME}/.codex/skills"
  fi

  link_target "${REPO_DIR}/shared/INSTRUCTIONS.md" "${HOME}/.codex/AGENTS.md"
  link_target "${REPO_DIR}/codex/config.toml" "${HOME}/.codex/config.toml"
  link_target "${REPO_DIR}/shared/rules" "${HOME}/.codex/rules"
  link_target "${REPO_DIR}/codex/agents" "${HOME}/.codex/agents"
  link_target "${REPO_DIR}/shared/hooks" "${HOME}/.codex/hooks"

  cleanup_stale_skills "${HOME}/.codex/skills"
  link_agent_skills "${HOME}/.codex/skills"
  link_shared_skills "${HOME}/.codex/skills"
}

ensure_cli() {
  local bin_name="$1"
  local display_name="$2"
  local install_cmd="$3"

  if command -v "$bin_name" >/dev/null 2>&1 || [ -x "${HOME}/.local/bin/${bin_name}" ]; then
    log_ok "${display_name} (${bin_name}) is installed"
    return 0
  fi

  if [ "$DRY_RUN" = true ]; then
    log_dry "Install ${display_name} via: ${install_cmd}"
    return 0
  fi

  log_info "Installing ${display_name} (${bin_name})..."
  eval "$install_cmd"
  log_ok "Installed ${display_name} (${bin_name})"
}

ensure_clis() {
  if [ "$SKIP_CLI" = true ]; then
    log_info "Skipping CLI installation checks (--skip-cli)."
    return 0
  fi

  ensure_cli "agy" "Antigravity CLI" "curl -fsSL https://antigravity.google/cli/install.sh | bash"
  ensure_cli "claude" "Claude CLI" "curl -fsSL https://claude.ai/install.sh | bash"
  ensure_cli "codex" "Codex CLI" "curl -fsSL https://chatgpt.com/codex/install.sh | sh"
}

link_agents() {
  log_info "Configuring Agents (Claude, Gemini, Codex)..."
  sync_shared_mcp
  link_claude
  link_gemini
  link_codex
  ensure_clis
}

build_formatter() {
  log_info "Building Formatter Docker Image (agents-config-formatter:latest)..."
  if ! command -v docker >/dev/null 2>&1; then
    log_warn "Docker is not installed or not in PATH; skipping formatter build."
    return 1
  fi

  if [ "$DRY_RUN" = true ]; then
    log_dry "Build docker image: agents-config-formatter:latest from ${REPO_DIR}/docker/formatter"
    return 0
  fi

  "${REPO_DIR}/docker/formatter/build.sh"
  log_ok "Formatter Docker Image built successfully."
}

# ------------------------------------------------------------------------------
# Entrypoint & Argument Parsing
# ------------------------------------------------------------------------------
main() {
  if [ -z "$REPO_DIR" ] || [ ! -f "${REPO_DIR}/shared/INSTRUCTIONS.md" ] || [ ! -f "${REPO_DIR}/shared/mcp.json" ]; then
    local arg
    for arg in ${1+"$@"}; do
      case "$arg" in
        -h|--help)
          usage
          exit 0
          ;;
      esac
    done
    bootstrap_remote_repo ${1+"$@"}
  fi

  local modules=()

  while [ $# -gt 0 ]; do
    case "$1" in
      -n|--dry-run)
        DRY_RUN=true
        shift
        ;;
      -f|--force)
        FORCE=true
        shift
        ;;
      --skip-cli)
        SKIP_CLI=true
        shift
        ;;
      -h|--help)
        usage
        exit 0
        ;;
      agents|claude|gemini|codex|mcp|formatter|docker|all)
        modules+=("$1")
        shift
        ;;
      *)
        log_warn "Unknown option or module: $1"
        usage
        exit 1
        ;;
    esac
  done

  if [ ${#modules[@]} -eq 0 ]; then
    modules=("all")
  fi

  log_info "Starting agents-config installation from: ${REPO_DIR}"
  if [ "$DRY_RUN" = true ]; then
    log_dry "DRY RUN MODE ENABLED - No changes will be written to disk."
  fi

  local mod
  for mod in "${modules[@]}"; do
    case "$mod" in
      agents|all)       link_agents ;;
      claude)           link_claude ;;
      gemini)           link_gemini ;;
      codex)            link_codex ;;
      mcp)              sync_shared_mcp ;;
      formatter|docker) build_formatter ;;
    esac
  done

  log_ok "Completed agents-config installation tasks."
}

main ${1+"$@"}
