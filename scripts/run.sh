#!/bin/bash
# ==============================================================================================
# Title:    run.sh
# Brief:    Run Django Server and Database in Docker.
# Author:   christiangama.dev@gmail.com
# Creation: 2023-05-08
# Usage:    ./scripts/run.sh
# ==============================================================================================

docker compose up -d --build --force-recreate --remove-orphans