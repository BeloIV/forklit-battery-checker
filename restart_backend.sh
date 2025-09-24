#!/usr/bin/env bash
set -e

echo "Reštartujem backend kontajner..."
sudo docker compose stop backend
sudo docker compose rm -f backend
sudo docker compose up -d backend

echo "Hotovo. Logy sleduj cez:"
echo "  sudo docker compose logs -f backend"