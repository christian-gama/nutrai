#!/bin/bash
# ==============================================================================================
# Title:    test.sh
# Brief:    Run Django Tests from the api container.
# Author:   christiangama.dev@gmail.com
# Creation: 2023-05-08
# Usage:    ./scripts/test.sh
# ==============================================================================================

docker compose up psql -d
sh ./scripts/wait_for_db.sh nutrai-postgres
export DATABASE_HOST=localhost
python manage.py test
