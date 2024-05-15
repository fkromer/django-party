#!/bin/bash
rm -rf venv
rm .env
rm db.sqlite3
find bin -type f -name 'tailwind*' -delete