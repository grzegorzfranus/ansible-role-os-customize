# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

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
