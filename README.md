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

