# Full-stack Django with HTMX and Tailwind

[testdriven.io - Course: Full-stack Django with HTMX and Tailwind](https://testdriven.io/courses/django-htmx)

- Setup project: `./scripts/setup_project.sh`
- Setup [TailwindCSS CLI](https://tailwindcss.com/blog/standalone-cli): adjust the download to your system and architecture in `./scripts/update_tailwindcss.sh`, execute the script
- Run project in VSCode: `Ctrl+Shift+D`, run launch target `Django Party`.
- Recreate `venv` after updates of dependencies in `./requirements.txt`: `./scripts/update_venv.sh`
- Teardown project: `./scripts/teardown_project.sh`

## Optional

- Format JSON fixture files: Open fixture files in `./party/fixtures/*.json` and format them using `Alt+Shift+F`.
- Update tailwindcss cli version: adjust the download to your system and architecture in `./scripts/update_tailwindcss.sh`, execute the script and adjust `TAILWIND_CLI_VERSION` in `./core/settings.py` accordingly
- Update htmx version: `./scripts/update_htmx.sh`
- Update alpinejs version: `./scripts/update_htmx.sh`
