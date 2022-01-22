#!/bin/bash

set -e

export PGPASSWORD=$POSTGRES_PASSWORD;
psql -v ON_ERROR_STOP=1 \
    --username "$POSTGRES_USER" -tc \
     "SELECT 1 FROM pg_database WHERE datname = '$APP_DB'" | grep -q 1 | psql -U "$POSTGRES_USER" -c "CREATE DATABASE $APP_DB"