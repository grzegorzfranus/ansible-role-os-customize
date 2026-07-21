# Ansible Role: OS Customize

|Source|Version|CI|License|
|------|-------|--|-------|
|[![Source Code](https://img.shields.io/badge/source-github-blue.svg)](https://github.com/grzegorzfranus/ansible-role-os-customize)|[![Version](https://img.shields.io/github/v/release/grzegorzfranus/ansible-role-os-customize)](https://github.com/grzegorzfranus/ansible-role-os-customize/releases)|[![CI](https://github.com/grzegorzfranus/ansible-role-os-customize/actions/workflows/ci.yml/badge.svg)](https://github.com/grzegorzfranus/ansible-role-os-customize/actions/workflows/ci.yml)|[![Repository License](https://img.shields.io/badge/license-apache2.0-brightgreen.svg)](LICENSE)|

This Ansible role customizes basic Linux OS settings, including login banners, welcome messages, shell environment, timezone, and package installation. It is designed for secure, consistent, and maintainable system configuration across Debian, Ubuntu, and EL-based distributions.

## ✨ Features

- ⏰ **Timezone Management**: Set system timezone with validation support
- 📦 **Package Installation**: Install and manage additional packages with flexible configuration
- 🛡️ **Login Banners**: Configure login banners with customizable security warning messages
- 🚀 **Welcome Messages**: Deploy customized welcome message scripts for both Debian and EL-based systems
- 🐚 **Shell Standardization**: Standardize and enhance .bashrc for root, skeleton, and all users
- 🔄 **MOTD Management**: Disable MOTD news service to prevent unwanted external network messages
- 🔒 **SSH Security**: Create a dedicated SSH users group for enhanced security and access control
- 🧪 **Variable Validation**: Robust dual-layer variable validation and OS-specific configuration handling

## 🎯 Architecture

The role provides modular system customization tasks organized into functional areas:

```
[Main Tasks (tasks/main.yml)]
   ├── [Assert Checks (tasks/assert.yml)]
   ├── [Configure Core OS (tasks/configure.yml)]
   └── [Configure Shell (tasks/bashrc.yml)]
```

- **Core OS Customization**: Timezone settings, security banner deployment, welcome message setup, and package updates.
- **Access Group Setup**: Ensures a local SSH users group is present with a specific GID for policy enforcement.
- **Shell Customization**: Appends standardized aliases, history settings, and shell prompts to global and user shell profiles.

## 📋 Requirements

- **Ansible**: 2.15 or higher
- **Python**: 3.9 or higher on target hosts
- **Privileges**: sudo/root access on target hosts (`become: true`)

### Supported operating systems

List of officially supported operating systems for this role:

| OS Family | Version | Status |
|-----------|---------|---------|
| Ubuntu | 26.04 (Resolute) | ![✓](https://img.shields.io/badge/✓-brightgreen.svg) |
| Ubuntu | 24.04 (Noble) | ![✓](https://img.shields.io/badge/✓-brightgreen.svg) |
| Ubuntu | 22.04 (Jammy) | ![✓](https://img.shields.io/badge/✓-brightgreen.svg) |
| Debian | 13 (Trixie)   | ![✓](https://img.shields.io/badge/✓-brightgreen.svg) |
| Debian | 12 (Bookworm) | ![✓](https://img.shields.io/badge/✓-brightgreen.svg) |
| Debian | 11 (Bullseye) | ![✓](https://img.shields.io/badge/✓-brightgreen.svg) |
| EL (RHEL, Rocky, Alma, Oracle) | 9 | ![✓](https://img.shields.io/badge/✓-brightgreen.svg) |

> **Note**: EL 8 is not supported — `python3-dnf` bindings are compiled for Python 3.6, which is incompatible with ansible-core >= 2.17. Use EL 9 or newer.

### Setup module

The role uses facts gathered by Ansible on the remote host. If you disable the Setup module in your playbook, the role will not work properly.

### Root access

This role requires root access for system customization. Make sure you are using a user with root privileges.

## 🚀 Quick Start

### 1. Basic OS Customization

```yaml
---
- name: Customize OS Settings
  hosts: all
  become: true
  roles:
    - role: grzegorzfranus.os_customize
```

### 2. Custom Timezone and Packages

```yaml
---
- name: Customize OS with Timezone and Custom Packages
  hosts: all
  become: true
  roles:
    - role: grzegorzfranus.os_customize
      vars:
        os_customize_configure_timezone: true
        os_customize_timezone: "Europe/Warsaw"
        os_customize_additional_packages:
          - vim
          - curl
          - htop
```

### 3. Run the playbook

```bash
ansible-playbook -i inventory playbook.yml
```

## ⚙️ Configuration

### Default Configuration

The role comes with secure and clean defaults:

```yaml
# Enable package installs but keep timezone configuration optional
os_customize_configure_timezone: false
os_customize_timezone: "Europe/Warsaw"
os_customize_configure_additional_packages: true
os_customize_additional_packages: [bc, vim, nano, htop]
os_customize_configure_welcome_message: true
os_customize_configure_bashrc: true
os_customize_disable_motd_news: true
os_customize_configure_ssh_group: true
```

### Advanced Configuration

Customize for specific enterprise environments:

```yaml
---
- name: Advanced OS Customization
  hosts: all
  become: true
  vars:
    os_customize_system_admin_mail: "sysadmin@company.com"
    os_customize_configure_timezone: true
    os_customize_timezone: "Europe/Berlin"
    os_customize_additional_packages:
      - net-tools
      - htop
      - vim
      - tmux
      - rsync
    os_customize_configure_bashrc: true
    os_customize_configure_ssh_group: true
    os_customize_ssh_group_name: "ssh-access"
    os_customize_ssh_group_gid: 59888
  roles:
    - role: grzegorzfranus.os_customize
```

## 📊 Variables

### General Options

| Variable | Description | Default |
|----------|-------------|---------|
| `os_customize_system_admin_mail` | System administrator e-mail address (used in banners) | `"admin@example.com"` |
| `os_customize_configure_timezone` | Enable/disable timezone configuration | `false` |
| `os_customize_timezone` | Timezone to set on the system (e.g., "Europe/Warsaw") | `"Europe/Warsaw"` |
| `os_customize_configure_additional_packages` | Enable/disable installation of additional packages | `true` |
| `os_customize_additional_packages` | List of additional packages to install | `[bc, vim, nano, htop]` |
| `os_customize_configure_welcome_message` | Enable/disable welcome message and login banner | `true` |
| `os_customize_configure_bashrc` | Enable/disable configuration of .bashrc files | `true` |
| `os_customize_disable_motd_news` | Enable/disable motd-news.timer service | `true` |
| `os_customize_configure_ssh_group` | Enable/disable creation of a dedicated SSH users group | `true` |
| `os_customize_ssh_group_name` | Name of the SSH users group | `"sshusers"` |
| `os_customize_ssh_group_gid` | GID for the SSH users group | `59876` |

### Banner and Welcome Message Options

| Variable | Description | Default |
|----------|-------------|---------|
| `os_customize_welcome_banner_path` | Path to the banner file | OS-specific (see vars/*.yml) |
| `os_customize_welcome_script_path` | Path to the login message script | OS-specific (see vars/*.yml) |

### Bashrc Configuration Options

| Variable | Description | Default |
|----------|-------------|---------|
| `os_customize_bashrc_list` | List of .bashrc files to configure | `["/root/.bashrc", "/etc/skel/.bashrc"]` |

## 📌 Role Properties

| Property | Value | Description |
|---|---|---|
| **Idempotent** | ✅ Yes | Running the role multiple times produces no changes unless configurations differ. |
| **Atomic** | ❌ No | Failure mid-run may leave the OS partially customized. |
| **Check Mode** | ✅ Supported | All customization steps support check mode without making changes. |
| **Diff Mode** | ✅ Supported | File templates support diff mode preview. |

## 📤 Role Output

This role does not set any public output facts. All internal facts use the `__os_customize_` prefix.

## 🔍 Verification

After deployment, verify that the OS customizations have been applied successfully:

### Check Timezone

```bash
timedatectl status
```

### Verify Welcome Message and Login Banner

```bash
# View login banner
cat /etc/issue.net

# View MOTD welcome script
cat /etc/profile.d/welcome.sh
```

### Verify SSH Group

```bash
getent group sshusers
```

## 🛡️ Security Features

- ✅ **Login Banners**: Security warnings displayed on login screens.
- ✅ **Privileged Escalation**: All tasks run with `become: true` where necessary.
- ✅ **Access Control**: Dedicated SSH users group created to lock down access.

### Uninstall

This role does not support automatic rollback or uninstallation. Custom packages, timezone changes, and `.bashrc` profile edits are permanent unless manually reverted.

### Roll-back Capabilities

Configuration files are backed up automatically using Ansible's `backup: true` directive. If you need to revert to a previous state:

1. Restore `.bashrc` or issue file from `.bak` timestamps created in target directories.
2. Revert any package manager edits manually.

## 🔧 Troubleshooting

### Timezone Errors

If timezone configuration fails, verify the spelling of timezone string and that it exists on the target host:

```bash
# List available timezones
timedatectl list-timezones
```

### Shell Welcome Message Issues

If the welcome message does not appear on login, verify that `/etc/profile.d/` scripts are sourced by your shell configuration.

## 📁 File Structure

```
ansible-role-os-customize/
├── .github/
│   ├── ISSUE_TEMPLATE/                # Issue templates for bug, feature, task
│   │   ├── bug_report.yml
│   │   ├── config.yml
│   │   ├── feature_request.yml
│   │   └── task.yml
│   ├── PULL_REQUEST_TEMPLATE/         # Pull request description template
│   │   └── pull_request_template.md
│   ├── workflows/
│   │   ├── ci.yml                     # CI pipeline
│   │   └── release.yml                # Release Please + Galaxy publish
│   └── dependabot.yml                 # Dependabot configuration for GitHub Actions
├── defaults/
│   └── main.yml             # Default role variables
├── handlers/
│   └── main.yml             # Event handlers
├── meta/
│   └── main.yml             # Role metadata and Galaxy information
├── molecule/                # Molecule testing framework
│   └── default/             # Default testing scenario
├── tasks/
│   ├── main.yml             # Main task orchestration
│   ├── assert.yml           # Variable validation
│   ├── configure.yml        # System configuration and services tasks
│   └── bashrc.yml           # .bashrc configuration
├── templates/
│   ├── banner.j2            # Login banner with security warning
│   └── scripts/
│       ├── login_debian.sh.j2  # Debian/Ubuntu login welcome script
│       └── login_redhat.sh.j2  # RHEL/Rocky login welcome script
└── vars/
    └── *.yml                # OS-specific variables
```

## 🏷️ Tags

All tags are prefixed with `os_customize_` to avoid collisions.

| Tag | Description |
|-----|-------------|
| `always` | Tasks that always run (variable loading and validation) |
| `os_customize_setup` | Setup tasks including OS-specific variables |
| `os_customize_init` | Initial setup tasks |
| `os_customize_validate` | Variable validation tasks |
| `os_customize_check` | Validation and verification tasks |
| `os_customize_configure` | System configuration tasks (banner, login, timezone, packages, services) |
| `os_customize_services` | Service configuration tasks (MOTD news, SSH group) |
## CI/CD Pipeline

This repository uses centralized, reusable GitHub Actions workflows from [grzegorzfranus/github-workflows](https://github.com/grzegorzfranus/github-workflows) (`v3.0.1`) for quality assurance, security scanning, and release automation.

### CI Pipeline (`ansible-ci.yml@v3.0.1`)

Runs on every Pull Request in a two-tier gate pattern:

1. **Branch Name Lint** — enforces naming conventions (`feature/`, `bugfix/`, `fix/`, `hotfix/`, `release/`, `chore/`, `docs/`, `refactor/`, `test/`, `build/`, `ci/`, `perf/`, `revert/`)
2. **PR Title Lint** — enforces [Conventional Commits](https://www.conventionalcommits.org/) format (`feat:`, `fix:`, `ci:`, etc.)
3. **YAML Syntax Lint** — validates YAML formatting via `yamllint`
4. **Ansible Lint** — checks Ansible best practices and role standards
5. **Galaxy Metadata Validation** — verifies `meta/main.yml` schema and requirements (`ansible-meta-validate.yml`)
6. **Security Scanning** — TruffleHog secret detection and Trivy IaC scanning (`ansible-security.yml`)
7. **Molecule Integration Tests** — executes Molecule test matrix across Ubuntu 26.04, Ubuntu 24.04, Ubuntu 22.04, Debian 13, Debian 12, Debian 11, and Rocky Linux 9 (`ansible-molecule.yml`)
8. **Merge Check Gate** — single authoritative status check aggregating all results for branch protection

### Release & Publish Pipeline (`ansible-publish.yml@v3.0.1`)

Automated via [Release Please](https://github.com/googleapis/release-please):

1. **Push to `main`** → Release Please creates or updates a Release PR with automated changelog generation
2. **Release PR Validation** → validates YAML syntax and actions schema before setting `Merge Check` status
3. **Merge Release PR** → creates Git version tag and GitHub Release automatically
4. **Ansible Galaxy Publish** → publishes tagged release to Ansible Galaxy via `ansible-publish.yml@v3.0.1` with exponential backoff retry logic

## Example Playbooks

```yaml
---
- name: Customize OS Settings
  hosts: all
  become: true
  roles:
    - role: grzegorzfranus.os_customize
      vars:
        os_customize_configure_timezone: true
        os_customize_timezone: "Europe/Warsaw"
        os_customize_additional_packages:
          - htop
          - curl
```

## 🤝 Contributing

Contributions, bug reports, and feature requests are welcome!

- Fork the repository and create your branch from `main`
- Use [Conventional Commits](https://www.conventionalcommits.org/) for commit messages
- Centralized workflows from [github-workflows](https://github.com/grzegorzfranus/github-workflows) version `v3.0.1` are used to run CI/CD pipelines
- Ensure your code passes all CI checks (YAML lint, Ansible lint, Molecule tests)
- Submit a pull request describing your changes (a template is available under `.github/PULL_REQUEST_TEMPLATE/pull_request_template.md` to help structure your PR description)
- For major changes, please open an issue first to discuss what you would like to change (issue templates for bug reports, feature requests, and tasks are available under `.github/ISSUE_TEMPLATE/`)

## 📝 License

This project is licensed under the Apache-2.0 License - see the LICENSE file for details.

## 👥 Author Information

This role was created by [Grzegorz Franus](https://github.com/grzegorzfranus).