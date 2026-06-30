# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.2.2](https://github.com/grzegorzfranus/ansible-role-os-customize/compare/v1.2.1...v1.2.2) (2026-06-30)


### Miscellaneous

* migrate workflows to github-workflows and align configuration ([#9](https://github.com/grzegorzfranus/ansible-role-os-customize/issues/9)) ([025a862](https://github.com/grzegorzfranus/ansible-role-os-customize/commit/025a862bdefcc631c205d6fe568ebc8f20a73910))

## [1.2.1](https://github.com/grzegorzfranus/ansible-role-os-customize/compare/v1.2.0...v1.2.1) (2026-05-24)


### Documentation

* standardize README.md structure to match tailscale reference ([#6](https://github.com/grzegorzfranus/ansible-role-os-customize/issues/6)) ([4db4419](https://github.com/grzegorzfranus/ansible-role-os-customize/commit/4db441905b9599d3ed6a2d704e4d0369844484bb))

## [1.2.0](https://github.com/grzegorzfranus/ansible-role-os-customize/compare/v1.1.0...v1.2.0) (2026-05-22)


### Features

* **ci:** add pr-title-validation, concurrency, release metadata chec… ([#4](https://github.com/grzegorzfranus/ansible-role-os-customize/issues/4)) ([e7499ca](https://github.com/grzegorzfranus/ansible-role-os-customize/commit/e7499ca93ea7f0f35b1770e1be23c7db31991d9e))

## [1.1.0](https://github.com/grzegorzfranus/ansible-role-os-customize/compare/v1.0.3...v1.1.0) (2026-05-21)


### Features

* migrate to centralized CI, Release Please, Galaxy publish, and … ([#2](https://github.com/grzegorzfranus/ansible-role-os-customize/issues/2)) ([3097318](https://github.com/grzegorzfranus/ansible-role-os-customize/commit/3097318b15b83531cab7141dce3a6f86c2283d51))

## [1.0.3] - 2026-05-18

### Fixed
- Upgraded `actions/checkout` from v4 to v6 (Node.js 24 compatible)
- Upgraded `actions/setup-python` from v5 to v6 (Node.js 24 compatible)

### Changed
- Standardized workflow and job naming to enterprise convention (Numbered Title Case)

## [1.0.2] - 2025-11-29

### Fixed 🔧
- Fixed deprecated `ansible_os_family` and `ansible_service_mgr` variables in Molecule converge playbook.
- Added tzdata package installation in Molecule prepare step for timezone support.
- Changed test timezone to `UTC` for universal container compatibility.

## [1.0.1] - 2025-11-29

### Added ✅
- Molecule test scenario with comprehensive verification tests.
- GitHub Actions workflows for test/validation and Galaxy publishing.

### Fixed 🔧
- Updated deprecated `ansible_date_time` variable to `ansible_facts['date_time']` format in login templates.
- Ensured compatibility with Ansible 2.20+ `INJECT_FACTS_AS_VARS` deprecation.

### Changed 🔄
- Templates now use `ansible_facts['date_time']['date']` instead of `ansible_date_time.date`.
- Removed emojis from all task names for cleaner output.
- Simplified login banner by removing ASCII art logo.

## [1.0.0] - 2025-08-10
### Added ✅
- Initial role hardening to align with internal Ansible best practices.
- Role-level `.ansible-lint` and `.yamllint` configs.
- OS-specific variable loading via `first_found` pattern.
- Variable validation using dedicated `tasks/assert.yml`.
- Banner and login scripts for Debian and RedHat families.

### Fixed 🔧
- YAML lint issues (trailing spaces, newline at EOF).
- Typo in `meta/main.yml` galaxy tags (removed stray bracket).
- Replaced deprecated `with_items` with `loop`.

### Changed 🔄
- Consistent task naming with emojis per style guide.
- README: removed Molecule references; clarified requirements.

### Removed ❌
- Molecule/CI references for this role, per project policy.
