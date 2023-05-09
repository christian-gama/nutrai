#!/bin/bash
# ==============================================================================================
# Title:    migrate.sh
# Brief:    Run Django Migrations from the api container.
# Author:   christiangama.dev@gmail.com
# Creation: 2023-05-08
# Usage:    ./scripts/migrate.sh
# ==============================================================================================

docker compose up psql -d
sh ./scripts/wait_for_db.sh nutrai-postgres
export DATABASE_HOST=localhost
python manage.py makemigrations
python manage.py migrate