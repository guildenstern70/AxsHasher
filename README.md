# Axs Hasher

Axs Hasher is a simple, yet powerful, text hasher written in Python. It provides the Base64 representation of the hash code of the entered string using these algorithms:

* SHA-2 (SHA-256, SHA-512)
* SHA-3 (SHA3-256, SHA3-512)
* BLAKE-2 (BLAKE2b, BLAKE2s)

## Setup

The project uses [uv](https://docs.astral.sh/uv/) and Python 3.15 (pinned in `.python-version`; uv will fetch it if needed).

1. Install uv, e.g. `brew install uv` (see the uv documentation for other methods).
2. From the project root, install the dependencies:

   ```sh
   uv sync
   ```

## Running the program

```sh
uv run axs-hasher
```

The program is interactive:

1. Pick an algorithm with the arrow keys and press Enter.
2. Type the phrase to hash and press Enter.
3. The Base64 digest is printed.
4. Confirm the prompt to copy the digest to the clipboard.

Press Ctrl-C at any prompt to exit.

## Running the tests

Run the whole test suite:

```sh
uv run pytest
```

Run a single test:

```sh
uv run pytest test/test_cli.py::test_prints_and_copies
```

Optionally, run the linter (the code is expected to score 10/10):

```sh
uv run pylint src test
```
