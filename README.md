# Minimal Template Project for Colvert

A minimal Python project template for Colvert that demonstrates integration with various Colvert packages including authentication, internationalization, and worker data management.

## Features

- FastAPI-based REST API
- JWT Authentication integration
- Internationalization support via colvert-i18n
- Worker data management via colvert-models
- CORS middleware configuration
- Comprehensive error handling
- Development server with hot reload

## Installation

This project uses Poetry for dependency management. To install:

1. Make sure you have Poetry installed
2. Clone this repository
3. Configure Poetry to use the Colvert private repository:
   ```bash
   poetry config http-basic.colvert-repo <user-name> [password]
   ```
4. Install dependencies:
   ```bash
   poetry install
   ```
Note: Poetry stores the credentials in: `~/.config/pypoetry/config.toml`

## Environment Variables

The following environment variables need to be configured. Create a `.env` file in the root directory with the following content:

Note: there is a .env.example file that can be renamend.

```env
# General Configuration
LOG_LEVEL=INFO
APP_TITLE="Colvert API"
APP_DESCRIPTION="API for Colvert"
APP_VERSION="1.0.0"
APP_DEBUG=True
APP_ROOT_PATH=""

# CORS Configuration
CORS_ALLOW_ORIGINS=["*"]
CORS_ALLOW_CREDENTIALS=True
CORS_ALLOW_METHODS=["*"]
CORS_ALLOW_HEADERS=["*"]
CORS_EXPOSE_HEADERS=["*"]
CORS_MAX_AGE=3600

# Colvert Models Configuration
SUPABASE_URL="your-supabase-url"
SUPABASE_SERVICE_ROLE_KEY="your-supabase-service-role-key"
```

### General Configuration
- `LOG_LEVEL`: Logging level (e.g., DEBUG, INFO, WARNING)
- `APP_TITLE`: API title (default: "Colvert API")
- `APP_DESCRIPTION`: API description (default: "API for Colvert") 
- `APP_VERSION`: API version (default: "1.0.0")
- `APP_DEBUG`: Debug mode (default: True)
- `APP_ROOT_PATH`: Root path prefix (default: "")

### CORS Configuration
- `CORS_ALLOW_ORIGINS`: Allowed origins (default: ["*"])
- `CORS_ALLOW_CREDENTIALS`: Allow credentials (default: True)
- `CORS_ALLOW_METHODS`: Allowed HTTP methods (default: ["*"])
- `CORS_ALLOW_HEADERS`: Allowed headers (default: ["*"])
- `CORS_EXPOSE_HEADERS`: Exposed headers (default: ["*"])
- `CORS_MAX_AGE`: Max age in seconds (default: 3600)

### Colvert Models Configuration
- `SUPABASE_URL`: URL of your Supabase instance
- `SUPABASE_SERVICE_ROLE_KEY`: Service role key for Supabase authentication

## Usage

To start the development server:

```bash
poetry run python main.py
```

The server will start at `http://localhost:8000` with hot reload enabled.

## API Endpoints

### 1. Example Endpoint
```bash
curl http://localhost:8000/example
```
Returns a simple hello message.

### 2. Worker Data Endpoint
```bash
curl http://localhost:8000/worker/{worker_id}
```
Fetches worker data for a specific worker ID.

### 3. Translation Test Endpoint
```bash
curl http://localhost:8000/translation-test/en  # for English
curl http://localhost:8000/translation-test/fr  # for French
```
Tests the translation functionality for different languages.

### 4. JWT Validation Endpoint
```bash
curl -X GET "http://localhost:8000/jwt-validation" \
  -H "Authorization: Bearer <your-jwt-token>"
```

Example with an actual token (from Colvert Agency Web):
```bash
curl -X GET "http://localhost:8000/jwt-validation" \
  -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhYWwiOiJhYWwxIiwiYW1yIjpbeyJtZXRob2QiOiJwYXNzd29yZCIsInRpbWVzdGFtcCI6MTc0ODQ2NTQ0N31dLCJhcHBfbWV0YWRhdGEiOnsicHJvdmlkZXIiOiJlbWFpbCIsInByb3ZpZGVycyI6WyJlbWFpbCJdfSwiYXVkIjoiYXV0aGVudGljYXRlZCIsImVtYWlsIjoiZ2VvZmZyb3lAY29sdmVydC5haSIsImV4cCI6MTc0ODQ2OTA0NywiaWF0IjoxNzQ4NDY1NDQ3LCJpc19hbm9ueW1vdXMiOmZhbHNlLCJwaG9uZSI6IiIsInJvbGUiOiJhdXRoZW50aWNhdGVkIiwic2Vzc2lvbl9pZCI6IjQ5MThjYmI2LWNiZDAtNDc5ZC05NzM3LTI3YjAzNGM4Nzk3ZSIsInN1YiI6IjM5YjgyZWE1LTYzYTYtNDg0Zi1hYWFjLWIyODFiZWE3MGFjOSIsInVzZXJfbWV0YWRhdGEiOnsiZW1haWxfdmVyaWZpZWQiOnRydWV9LCJ1c2VyX3JvbGUiOiJhZG1pbl9lbXBsb3llZSJ9.6NA78Lj7rRRtjpT3k5S065GD5gCo1UvLfDBRQe6LZ_M"
```

This endpoint validates JWT tokens. The token should be obtained from the Colvert Agency Web interface after logging in.

## Development

The project is structured as follows:

```
colvert-minimal-project/
├── colvert_app/
│   ├── core/          # Core functionality (auth, exceptions)
│   ├── handlers/      # Request handlers
│   ├── routes/        # API routes
│   └── utils/         # Utility functions
├── main.py           # Application entry point
├── poetry.lock       # Lock file for dependencies
└── pyproject.toml    # Project configuration
```
