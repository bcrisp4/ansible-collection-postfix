# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]
### Changed
- Modify the install role to ensure that the apt cache is updated before installing the Postfix package
- Fix the path to the CHANGELOG file in the PR workflow
- Removed redundant prepare step from the install role Molecule scenario (it populated apt cache on debian hosts, but now the role takes care of that itself)

## [0.1.1] - 2021-01-10
### Added
- CHANGELOG.md
- Support for more OSs (Ubuntu, EL, Fedora) in the install role
- Add pull request actions workflow that enforces CHANGELOG.md updates

### Changed
- Release workflow now includes changes from CHANGELOG.md in the GitHub release
- The install role unit tests no longer checks for the instance OS
- Reduce repetition in Molecule test workflow for the install role
- Add CI status badge for the install role to relevant README files
- Add link to install role folder in the collection README
- Removed unneccessary steps from install role Molecule scenario
- Simplify the install role molecule workflow matrix
- Renamed the install role molecule  workflow to just the FQCN of the role

## [0.0.1] - 2021-01-10
### Added
- Misc: initialise the collection
- roles/install: Created the install role
- roles/install: Molecule GitHub Actions test workflow for the install role
- CI: GitHub Actions release workflow
