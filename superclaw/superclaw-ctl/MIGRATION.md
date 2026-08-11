# Migration guide: superclaw-ctl 1.2.0

This guide covers upgrading an existing `superclaw-ctl` installation to
version 1.2.0. For a new installation, follow the setup steps in
[README.md](README.md).

## What changes in 1.2.0

Model directories now use owner-scoped names derived from their Hugging Face
repository IDs. The bundled compose template uses the new names as well.

| Model | Legacy directory | Canonical directory |
|---|---|---|
| Qwen3-Coder-Next | `Qwen3-Coder-Next` | `Qwen--Qwen3-Coder-Next` |
| KaLM embedding v2.5 | `KaLM-embedding-v2.5` | `KaLM-Embedding--KaLM-embedding-multilingual-mini-instruct-v2.5` |

The migration is designed to preserve the existing configuration and API key.

## Recommended upgrade

Install the 1.2.0 binary first, then run the following commands on the
model-serving workstation:

```bash
superclaw-ctl version

# Run this if the serving stack is currently running.
superclaw-ctl down

superclaw-ctl upgrade
superclaw-ctl up
superclaw-ctl status
```

`upgrade`:

- Renames recognized legacy model directories to their canonical names.
- Refreshes the bundled `docker-compose.vllm.yml` in the configured compose
  directory.
- Keeps the existing API key and does not write `secrets.toml`.
- Is safe to run again when the installation is already current.

After the upgrade, optionally verify the active model files:

```bash
superclaw-ctl doctor
superclaw-ctl models download --model Qwen/Qwen3-Coder-Next --verify
```

Use canonical directory names with commands that take a local directory name:

```bash
superclaw-ctl models info Qwen--Qwen3-Coder-Next
```

## Important: do not re-run `init`

Do not run `superclaw-ctl init` to apply an upgrade. `init` generates a new
`VLLM_API_KEY` and can invalidate existing clients, browser sessions, and saved
environment files.

Run `init` only for a genuinely new installation. If an existing installation
does not have its configuration, restore or locate the original
`~/.config/superclaw-ctl/` directory before upgrading.

## Compose files and `--force`

`upgrade` refuses to overwrite a compose file that appears to have been
hand-modified. It also refuses to continue while containers are running.

If the compose file is intentionally customized:

1. Stop the containers with `superclaw-ctl down`.
2. Review the differences and make a backup of any custom configuration.
3. Run `superclaw-ctl upgrade --force` only if replacing the managed compose
   file is acceptable.

When `--force` replaces a managed compose file, it keeps the previous file as
`<file>.bak`. The base compose file is managed by `superclaw-ctl`; files listed
in `config.compose.extra_files` are not rewritten automatically.

If an extra compose file contains a legacy model path, update it manually to
the canonical directory name before starting the stack.

## Manual layout migration

Use this only when you need to inspect or control the directory migration
separately from the compose refresh:

```bash
# Preview changes; this does not rename anything.
superclaw-ctl models migrate-layout

# Apply all planned renames.
superclaw-ctl models migrate-layout --apply

# Apply a single model migration.
superclaw-ctl models migrate-layout \
  --model Qwen/Qwen3-Coder-Next --apply
```

If both a legacy and canonical directory exist, the command stops rather than
choosing which one to keep. Resolve the duplicate manually after checking
which directory contains the complete model, then retry the migration.

## Troubleshooting

- **Containers are running:** run `superclaw-ctl down` and retry.
- **No configuration found:** do not initialize over an existing installation;
  restore `~/.config/superclaw-ctl/` first.
- **A legacy directory is still referenced:** run `superclaw-ctl upgrade` and
  update any `config.compose.extra_files` entries manually.
- **A canonical model directory is missing:** run
  `superclaw-ctl models download --model <owner>/<model> --verify`, then
  download or repair the model if verification reports missing files.
- **A custom router port is used:** pass the same `--router-port` value to
  `superclaw-ctl status` that was used with `up`.
