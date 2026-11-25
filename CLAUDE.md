# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project

Axs Hasher is a text hasher that outputs the Base64 representation of the hash of an entered string. The planned algorithms are SHA-2, SHA-3 and BLAKE-2 (see `README.md`). It is an interactive CLI (questionary prompts, pyperclip clipboard) offering SHA-256/512, SHA3-256/512 and BLAKE2b/2s.

Modules in `src/axs_hasher/`:
- `hashing.py`: `Algorithm` enum and `hash_to_base64()` (pure logic, stdlib `hashlib`).
- `models.py`: pydantic `HashRequest` (validates input) and `HashResult`.
- `cli.py`: `run()`, the interactive flow (select, text, print, optional copy).
- `__init__.py`: `main()` delegates to `cli.run()`.

## Commands

Dependencies are managed with `uv` (Python 3.15, pinned in `.python-version`).

- Install/sync: `uv sync`
- Run the app: `uv run axs-hasher` (console script pointing to `axs_hasher:main`)
- Run all tests: `uv run pytest`
- Run a single test: `uv run pytest test/test_cli.py::test_prints_and_copies`
- Lint: `uv run pylint src test`
- Add a dependency: `uv add <pkg>` (runtime) or `uv add --dev <pkg>` (dev)

## Layout and configuration

- Sources live in `src/axs_hasher/` (src layout, built with `uv_build`). Tests live in `test/`, not `tests/`.
- `pyproject.toml` sets `pytest` `testpaths = ["test"]` and `pythonpath = ["src"]`, and pylint `source-roots = ["src"]`. Keep these in sync if directories move.
- Pylint requires module and function docstrings, and the code currently scores 10/10. Keep it that way.
