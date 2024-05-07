#!/bin/bash
# https://github.com/tailwindlabs/tailwindcss/releases/tag/v3.4.3
curl -sLO https://github.com/tailwindlabs/tailwindcss/releases/download/v3.4.3/tailwindcss-macos-arm64
chmod +x tailwindcss-macos-arm64
mv tailwindcss-macos-arm64 ./bin/tailwindcss
./bin/tailwindcss