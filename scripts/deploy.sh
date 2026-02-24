#!/usr/bin/env bash
set -euo pipefail

echo "=== Starting deploy ==="

APP_DIR="/opt/app"

cd "$APP_DIR"

echo "[1/4] Pull latest changes (if using git)..."
if [ -d ".git" ]; then
  git pull
else
  echo "No git repo found, skipping pull"
fi

echo "[2/4] Building images..."
docker compose build

echo "[3/4] Recreating containers..."
docker compose up -d --force-recreate

echo "[4/4] Cleaning unused images..."
docker image prune -f

echo "=== Deploy completed ==="
