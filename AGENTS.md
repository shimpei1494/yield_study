# AGENTS.md

## Project Overview

This repository is a learning project for explaining Python's `yield` clearly to beginners and turning the examples into a Zenn article.

The code should stay small, readable, and ordered to match the article flow. Prefer examples that make execution order visible with `print()` before introducing practical FastAPI samples.

## Python Environment

Use `uv` for dependency management and Python execution.

- Add dependencies with `uv add`, not `pip install`.
- Run scripts with `uv run python ...`, not bare `python` when documenting commands.
- Run FastAPI examples with `uv run uvicorn ...`.
- Keep `pyproject.toml` and `uv.lock` as the source of truth for dependencies.

Examples:

```sh
uv add fastapi uvicorn
uv run python examples/02_next_step_by_step.py
uv run uvicorn examples.08_fastapi_sse_sample:app --reload
```

## Writing Guidelines

- Write explanations in Japanese.
- Keep sample code focused on one idea per file.
- For beginner-facing examples, prefer explicit names and visible output over clever abstractions.
- For article-only FastAPI examples, it is acceptable that the code is illustrative, but it should still be syntactically valid.

## Planned Structure

See `docs/implementation_plan.md` for the article outline and the corresponding sample files.
