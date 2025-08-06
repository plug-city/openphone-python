<!-- Use this file to provide workspace-specific custom instructions to Copilot. For more details, visit https://code.visualstudio.com/docs/copilot/copilot-customization#_use-a-githubcopilotinstructionsmd-file -->

# OpenPhone Python SDK - Copilot Instructions

This is a Python SDK for the OpenPhone API following these architectural principles:

## Project Structure
- `src/openphone_python/` - Main package source code
- `src/openphone_python/client.py` - Main client class with lazy-loaded resources
- `src/openphone_python/resources/` - API resource handlers (messages, contacts, calls, etc.)
- `src/openphone_python/models/` - Data models with type safety
- `src/openphone_python/auth/` - Authentication handling
- `src/openphone_python/utils/` - Utilities (validation, pagination, formatting)
- `src/openphone_python/exceptions.py` - Custom exception classes
- `tests/` - Test files

## Key Principles
1. **DRY (Don't Repeat Yourself)** - Common functionality in base classes
2. **Separation of Concerns** - Clear module boundaries and responsibilities
3. **Easy to Comprehend** - Clear naming, documentation, and structure
4. **Easy to Extend** - Plugin system and inheritance-based design

## Code Style Guidelines
- Use type hints throughout
- Follow Python naming conventions (snake_case for functions/variables, PascalCase for classes)
- Comprehensive docstrings with Args/Returns/Raises sections
- Error handling with specific exception types
- Phone numbers should be in E.164 format

## API Integration Patterns
- All API calls go through `BaseResource._request()` method
- Use pagination with `PaginatedResult` for list endpoints
- Validate phone numbers with utilities from `utils.formatting`
- Handle API errors with custom exception types from `exceptions.py`

## Resource Classes Structure
- Inherit from `BaseResource`
- Methods: `list()`, `get()`, `create()`, `update()`, `delete()` as applicable
- Return model instances, not raw dictionaries
- Use pagination for list methods

## Model Classes Structure
- Inherit from `BaseModel`
- Use properties for accessing data fields
- Parse timestamps in `_parse_data()` method
- Convert API field names (camelCase) to Python conventions (snake_case)

## Testing Approach
- Use `responses` library for HTTP mocking
- Test both success and error scenarios
- Validate proper model instantiation
- Test pagination behavior

When implementing new features, follow these established patterns and maintain consistency with the existing codebase.
