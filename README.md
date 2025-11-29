# Ansible Role: OS Customize

|Source|Version|CI|License|
|------|-------|-------|-------|
|[![Source Code](https://img.shields.io/badge/source-github-blue.svg)](https://github.com/grzegorzfranus/ansible-role-os-customize)|[![Version](https://img.shields.io/github/v/release/grzegorzfranus/ansible-role-os-customize)](https://github.com/grzegorzfranus/ansible-role-os-customize/releases)|[![Repository License](https://img.shields.io/badge/license-apache2.0-brightgreen.svg)](LICENSE)|

This Ansible role customizes basic Linux OS settings, including login banners, welcome messages, shell environment, timezone, and package installation. It is designed for secure, consistent, and maintainable system configuration across Debian, Ubuntu, and RHEL-based distributions.

## Main Features

- Set system timezone with validation
- Install and manage additional packages with flexible configuration
- Configure login banner with security warning message
- Deploy customized welcome message scripts for both Debian and RHEL-based systems
- Standardize and enhance .bashrc for root, skeleton, and all users
- Disable MOTD news service to prevent unwanted messages
- Create a dedicated SSH users group for enhanced security and access control
- Ensure robust variable validation and idempotency
- OS-specific configuration handling

## Requirements

### Supported Operating Systems
List of officially supported operating systems:
| OS Family | Version | Status |
|-----------|---------|---------|
| Ubuntu | 24.04 (Noble) | ![✓](https://img.shields.io/badge/✓-brightgreen.svg) |
| Ubuntu | 22.04 (Jammy) | ![✓](https://img.shields.io/badge/✓-brightgreen.svg) |
| Debian | 12 (Bookworm) | ![✓](https://img.shields.io/badge/✓-brightgreen.svg) |
| Debian | 11 (Bullseye) | ![✓](https://img.shields.io/badge/✓-brightgreen.svg) |
| Rocky Linux | 9 | ![✓](https://img.shields.io/badge/✓-brightgreen.svg) |
| EL | 8, 9 | ![✓](https://img.shields.io/badge/✓-brightgreen.svg) |

### Ansible Version
Ansible >= 2.15 (tested with Ansible 2.20)

### Python Version
Python >= 3.9

### Setup Module
The role uses facts gathered by Ansible on the remote host. If you disable the Setup module in your playbook, the role will not work properly.

### Root Access
This role requires root access for most tasks. Use a user with root privileges or set `become: true` in your playbook or inventory.

## Role Variables

All variables for this role are declared in:
- `defaults/main.yml`
- `vars/*.yml`

### General Options

| Variable | Description | Default |
|----------|-------------|---------|
| `os_customize_system_admin_mail` | System administrator e-mail address (used in banners, notifications, etc.) | `admin@example.com` |
| `os_customize_configure_timezone` | Enable/disable timezone configuration | `false` |
| `os_customize_timezone` | Timezone to set on the system (e.g., "Europe/Warsaw") | `Europe/Warsaw` |
| `os_customize_configure_additional_packages` | Enable/disable installation of additional packages | `true` |
| `os_customize_additional_packages` | List of additional packages to install | `[bc, vim, nano, htop]` |
| `os_customize_configure_welcome_message` | Enable/disable configuration of welcome message and login banner | `true` |
| `os_customize_configure_bashrc` | Enable/disable configuration of .bashrc files | `true` |
| `os_customize_disable_motd_news` | Enable/disable disabling of motd-news.timer service | `true` |
| `os_customize_configure_ssh_group` | Enable/disable creation of a dedicated SSH users group | `true` |
| `os_customize_ssh_group_name` | Name of the SSH users group | `sshusers` |
| `os_customize_ssh_group_gid` | GID for the SSH users group | `59876` |

### Banner and Welcome Message Options

| Variable | Description | Default |
|----------|-------------|---------|
| `os_customize_welcome_banner_path` | Path to the banner file | OS-specific (see vars/*.yml) |
| `os_customize_welcome_script_path` | Path to the login message script | OS-specific (see vars/*.yml) |

### Bashrc Configuration Options

| Variable | Description | Default |
|----------|-------------|---------|
| `os_customize_bashrc_list` | List of .bashrc files to configure | `/root/.bashrc` and `/etc/skel/.bashrc` |

## Role Structure

The role is organized as follows:

```
ansible-role-os-customize/
├── .github/
│   └── workflows/
│       ├── test-and-validation.yml  # CI testing pipeline
│       └── publish-to-galaxy.yml    # Galaxy publishing workflow
├── defaults/
│   └── main.yml             # Default role variables
├── handlers/
│   └── main.yml             # Event handlers
├── meta/
│   └── main.yml             # Role metadata and dependencies
├── molecule/
│   └── default/
│       ├── converge.yml     # Test playbook
│       ├── molecule.yml     # Molecule configuration
│       ├── prepare.yml      # Test preparation
│       └── verify.yml       # Verification tests
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

## Tags

- `always` - Tasks that always run (variable loading and validation)
- `setup` - Setup tasks including OS-specific variables
- `init` - Initial setup tasks
- `validate` - Variable validation tasks
- `check` - Validation and verification tasks
- `configure` - System configuration tasks (banner, login, timezone, packages, services)
- `services` - Service configuration tasks (MOTD news, SSH group)
- `bashrc` - .bashrc configuration tasks

## Example Playbooks

### Basic Customization
```yaml
---
- name: Basic OS Customization
  hosts: all
  become: true
  roles:
    - role: grzegorzfranus.os_customize
      vars:
        # Administrator contact
        os_customize_system_admin_mail: "sysadmin@company.com"
        
        # Timezone configuration
        os_customize_configure_timezone: true
        os_customize_timezone: "Europe/Warsaw"
        
        # Basic packages
        os_customize_additional_packages:
          - net-tools
          - htop
          - vim
          - tmux
```

### Advanced Customization
```yaml
---
- name: Advanced OS Customization
  hosts: production_servers
  become: true
  roles:
    - role: grzegorzfranus.os_customize
      vars:
        # Administrator contact
        os_customize_system_admin_mail: "sysadmin@company.com"
        
        # Timezone configuration
        os_customize_configure_timezone: true
        os_customize_timezone: "Europe/Berlin"
        
        # Comprehensive package set
        os_customize_additional_packages:
          - net-tools
          - htop
          - vim
          - tmux
          - iotop
          - sysstat
          - nc
          - tcpdump
          - curl
          - rsync
        
        # Enable .bashrc customization
        os_customize_configure_bashrc: true
        
        # Configure SSH access security
        os_customize_configure_ssh_group: true
        os_customize_ssh_group_name: "ssh-access"
        os_customize_ssh_group_gid: 59888
```

## Testing

This role includes Molecule tests for comprehensive verification across multiple distributions.

### Running Tests

```bash
# Run default test scenario
molecule test

# Run tests on specific distribution
MOLECULE_DISTRO=ubuntu2404 molecule test
MOLECULE_DISTRO=debian12 molecule test
MOLECULE_DISTRO=rockylinux9 molecule test
```

### Test Matrix

| Distribution | Image |
|--------------|-------|
| Ubuntu 24.04 | geerlingguy/docker-ubuntu2404-ansible |
| Ubuntu 22.04 | geerlingguy/docker-ubuntu2204-ansible |
| Debian 12 | geerlingguy/docker-debian12-ansible |
| Debian 11 | geerlingguy/docker-debian11-ansible |
| Rocky Linux 9 | geerlingguy/docker-rockylinux9-ansible |

### CI/CD

This role uses GitHub Actions for continuous integration:
- **test-and-validation.yml** - Runs linting and Molecule tests on every push/PR
- **publish-to-galaxy.yml** - Publishes to Ansible Galaxy on release

## Variable Validation

This role includes comprehensive validation of all variables through assertions to ensure proper configuration before making any changes to the system. The validations include:

- **Required Variables Check** - Ensures all required variables are defined
- **Type and Value Validation** - Ensures booleans, lists, and strings are correct and non-empty
- **Timezone Validation** - Verifies that the specified timezone is available on the system
- **Fail Fast** - If any validation fails, the role will stop execution with a descriptive error message

## License

Apache-2.0

## Author Information

This role was created by [Grzegorz Franus](https://github.com/grzegorzfranus).

## Contributing

Contributions, bug reports, and feature requests are welcome!

- Fork the repository and create your branch from `main`.
- Make your changes with clear, descriptive commit messages.
- Ensure your code passes all lint tests.
- Submit a pull request describing your changes and the motivation.
- For major changes, please open an issue first to discuss what you would like to change.

If you have questions or suggestions, feel free to open an issue or contact the author via GitHub.