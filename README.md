# Minimal Template Project for Colvert

A minimal Python project for Colvert.

## Installation

This project uses Poetry for dependency management. To install:

1. Make sure you have Poetry installed
2. Clone this repository
3. Run:
   ```bash
   poetry config http-basic.colvert-repo <user-name> [password]
   ```
3. Run:
   ```bash
   poetry install
   ```

Poetry stores the credentials in: ~/.config/pypoetry/config.toml

## Usage


To execute:
poetry run main 



## Environment Vars

general basic project:
LOG_LEVEL

colvert-models:
SUPABASE_URL
SUPABASE_SERVICE_ROLE_KEY

colvert-i18n:



curl -X GET "http://localhost:8000/jwt-validation" \
  -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhYWwiOiJhYWwxIiwiYW1yIjpbeyJtZXRob2QiOiJwYXNzd29yZCIsInRpbWVzdGFtcCI6MTc0ODQ2NTQ0N31dLCJhcHBfbWV0YWRhdGEiOnsicHJvdmlkZXIiOiJlbWFpbCIsInByb3ZpZGVycyI6WyJlbWFpbCJdfSwiYXVkIjoiYXV0aGVudGljYXRlZCIsImVtYWlsIjoiZ2VvZmZyb3lAY29sdmVydC5haSIsImV4cCI6MTc0ODQ2OTA0NywiaWF0IjoxNzQ4NDY1NDQ3LCJpc19hbm9ueW1vdXMiOmZhbHNlLCJwaG9uZSI6IiIsInJvbGUiOiJhdXRoZW50aWNhdGVkIiwic2Vzc2lvbl9pZCI6IjQ5MThjYmI2LWNiZDAtNDc5ZC05NzM3LTI3YjAzNGM4Nzk3ZSIsInN1YiI6IjM5YjgyZWE1LTYzYTYtNDg0Zi1hYWFjLWIyODFiZWE3MGFjOSIsInVzZXJfbWV0YWRhdGEiOnsiZW1haWxfdmVyaWZpZWQiOnRydWV9LCJ1c2VyX3JvbGUiOiJhZG1pbl9lbXBsb3llZSJ9.6NA78Lj7rRRtjpT3k5S065GD5gCo1UvLfDBRQe6LZ_M" \
  --include
