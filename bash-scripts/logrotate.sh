#!/bin/bash
LOG_DIR="./logs"
ARCHIVE_DIR="./archive"

mkdir -p "$ARCHIVE_DIR"

for file in "$LOG_DIR"/*.log; do
  if [ -f "$file" ]; then
    timestamp=$(date +"%Y%m%d%H%M%S")
    mv "$file" "$ARCHIVE_DIR/$(basename "$file" .log)-$timestamp.log"
    echo "Rotated: $file"
  fi
done
