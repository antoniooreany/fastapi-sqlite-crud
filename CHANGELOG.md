\# Changelog



All notable changes to this project will be documented in this file.



The format is inspired by Keep a Changelog, and this project follows a simple versioned release approach.



\## \[0.1.0] - 2026-07-12



\### Added

\- Added `LICENSE` to clarify repository licensing.

\- Added `scripts/project\_snapshot.ps1` for generating a Markdown snapshot of the project state.

\- Expanded `README.md` with setup, testing, Docker, security, logging, and snapshot tooling sections.

\- Added CI artifact upload for `pip-audit` JSON reports.



\### Changed

\- Updated CI so `pip-audit` runs in non-blocking mode and produces a machine-readable report.

\- Improved project documentation and repository structure descriptions.

\- Refined logging-related implementation and security-oriented tracing behavior.

\- Updated parts of the application and tests for improved maintainability and consistency.



\### Security

\- Kept dependency vulnerability scanning in CI via `pip-audit`.

\- Changed security scanning behavior so vulnerabilities are reported without blocking the full pipeline.



\### Notes

\- Documentation deployment remains tied to pushes on `main`.

\- This release represents the first documented project release suitable for portfolio presentation.

