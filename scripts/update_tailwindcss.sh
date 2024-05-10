#!/bin/bash
# https://github.com/tailwindlabs/tailwindcss/releases
curl -sLO https://github.com/tailwindlabs/tailwindcss/releases/latest/download/tailwindcss-macos-arm64
chmod +x tailwindcss-macos-arm64
mv tailwindcss-macos-arm64 ./bin/tailwindcss
./bin/tailwindcss