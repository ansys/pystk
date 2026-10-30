"""Execute the examples once and cache the executed notebooks.

An executed notebook is reused only if its key matches the current key. The key
combines a global hash with the hash of the example and its data files. Any
change to the dependencies, the library sources, the documentation
configuration, the packaging metadata or the CI/CD workflows changes the global
hash and therefore invalidates every notebook.

Usage: ``python scripts/examples_cache.py`` executes the missing or stale
notebooks. It does nothing if ``BUILD_EXAMPLES`` is ``false``. Set
``EXAMPLES_CACHE_FORCE=true`` to execute every example regardless of the cache.
"""

import hashlib
import os
import pathlib
import sys

PROJECT_ROOT = pathlib.Path(__file__).resolve().parents[1]
EXAMPLES_DIRECTORY = PROJECT_ROOT / "examples"
CACHE_DIRECTORY = pathlib.Path(os.environ.get("EXAMPLES_CACHE_DIR", EXAMPLES_DIRECTORY / ".cache"))

# Files and directories that invalidate every cached notebook when modified
GLOBAL_INPUTS = [
    "uv.lock",
    "pyproject.toml",
    "tox.ini",
    "doc/source/conf.py",
    "scripts/examples_cache.py",
    "src",
    ".github/workflows",
]
EXAMPLE_EXTRA_INPUTS = ["data", "img"]
EXCLUDED_PARTS = {"__pycache__"}


def _iter_files(path: pathlib.Path):
    if path.is_file():
        yield path
    elif path.is_dir():
        for file in sorted(path.rglob("*")):
            if file.is_file() and not EXCLUDED_PARTS & set(file.parts):
                yield file


def _update(digest, files):
    for file in files:
        digest.update(file.relative_to(PROJECT_ROOT).as_posix().encode())
        digest.update(file.read_bytes())


def global_key() -> str:
    """Return the hash shared by all the examples."""
    digest = hashlib.sha256()
    for name in GLOBAL_INPUTS:
        _update(digest, _iter_files(PROJECT_ROOT / name))
    # The salt lets the CI/CD invalidate the cache when the STK image changes
    digest.update(os.environ.get("EXAMPLES_CACHE_SALT", "").encode())
    digest.update(sys.version.encode())
    return digest.hexdigest()


def example_key(example: pathlib.Path, global_hash: str | None = None) -> str:
    """Return the hash of an example, including the global hash."""
    digest = hashlib.sha256((global_hash or global_key()).encode())
    digest.update(example.name.encode())
    digest.update(example.read_bytes())
    for name in EXAMPLE_EXTRA_INPUTS:
        _update(digest, _iter_files(EXAMPLES_DIRECTORY / name))
    return digest.hexdigest()


def cached_notebook(example: pathlib.Path, global_hash: str | None = None):
    """Return the path of a valid cached notebook, or ``None``."""
    notebook = CACHE_DIRECTORY / f"{example.stem}.ipynb"
    key_file = CACHE_DIRECTORY / f"{example.stem}.key"
    if not (notebook.is_file() and key_file.is_file()):
        return None
    if key_file.read_text(encoding="utf-8").strip() != example_key(example, global_hash):
        return None
    return notebook


def execute_examples() -> None:
    """Execute the examples without a valid cached notebook."""
    import jupytext
    from nbclient import NotebookClient
    import nbformat

    CACHE_DIRECTORY.mkdir(parents=True, exist_ok=True)
    global_hash = global_key()
    force = os.environ.get("EXAMPLES_CACHE_FORCE", "false") == "true"
    examples = sorted(EXAMPLES_DIRECTORY.glob("*.py"))
    current = {example.stem for example in examples}

    # Remove notebooks of examples that no longer exist
    for file in CACHE_DIRECTORY.glob("*"):
        if file.stem not in current:
            file.unlink()

    for example in examples:
        if not force and cached_notebook(example, global_hash):
            print(f"[cache hit]  {example.name}")
            continue
        print(f"[executing]  {example.name}", flush=True)
        key_file = CACHE_DIRECTORY / f"{example.stem}.key"
        key_file.unlink(missing_ok=True)
        notebook = jupytext.read(example)
        NotebookClient(
            notebook,
            timeout=-1,
            kernel_name="python3",
            resources={"metadata": {"path": str(EXAMPLES_DIRECTORY)}},
        ).execute()
        nbformat.write(notebook, CACHE_DIRECTORY / f"{example.stem}.ipynb")
        # The key is written last so an interrupted run never leaves a valid entry
        key_file.write_text(example_key(example, global_hash), encoding="utf-8")


if __name__ == "__main__":
    if os.environ.get("BUILD_EXAMPLES", "true") == "true":
        execute_examples()
