# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- Nothing yet

### Changed
- Nothing yet

### Deprecated
- Nothing yet

### Removed
- Nothing yet

### Fixed
- Nothing yet

### Security
- Nothing yet

## [0.4.0] - 2025-01-27

### Added
- Raw request functionality to client with `raw_request()` and `raw_request_with_response_object()` methods
- Standalone raw request utilities in `utils.raw_request` module
- Support for direct API calls without SDK model processing
- Comprehensive documentation and examples for raw request usage
- Multiple usage patterns: client methods, standalone utilities, and mixed approaches

### Changed
- Enhanced client class with direct API access capabilities
- Updated documentation with raw request examples and best practices

## [0.2.1] - 2025-01-27

### Fixed
- Contact object creation issues
- General bug fixes and improvements

## [0.2.0] - 2025-08-06

### Added
- Retry logic with exponential backoff for API requests
- Configurable max_retries parameter (default: 3)
- Automatic retry with 1s, 2s, 4s delays for network failures

## [0.1.0] - 2025-08-06

### Added
- Initial release of OpenPhone Python SDK
- Complete API coverage for OpenPhone v1 API
- Type-safe models and resources
- Authentication handling
- Comprehensive documentation and examples
- Development tools (testing, linting, formatting)

[Unreleased]: https://github.com/plug-city/openphone-python/compare/v0.4.0...HEAD
[0.4.0]: https://github.com/plug-city/openphone-python/compare/v0.2.1...v0.4.0
[0.2.1]: https://github.com/plug-city/openphone-python/compare/v0.2.0...v0.2.1
[0.2.0]: https://github.com/plug-city/openphone-python/compare/v0.1.0...v0.2.0
[0.1.0]: https://github.com/plug-city/openphone-python/releases/tag/v0.1.0
