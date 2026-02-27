#!/usr/bin/env bash
set -euo pipefail

if grep -R -n "AI-HPP-.*X" standard/; then
  echo "Placeholder requirement IDs detected in standard/."
  exit 1
fi

echo "No placeholder requirement IDs found in standard/."
