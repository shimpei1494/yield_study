# yield-study

Python の `yield` を初学者向けに整理するための学習リポジトリです。

最終的には、`article/zenn_draft.md` をもとに Zenn 記事を書く想定です。記事だけでも流れが分かるようにしつつ、動きを確認したい場合は `examples/` のコードを `uv` で実行できます。

## Structure

```text
article/
  zenn_draft.md
examples/
  01_return_vs_yield.py
  02_next_step_by_step.py
  03_for_loop.py
  04_list_vs_generator.py
  05_file_reader.py
  06_pipeline.py
  07_streaming_basic.py
  08_fastapi_sse_sample.py
  09_fastapi_dependency_sample.py
  10_contextmanager.py
data/
  sample.txt
docs/
  implementation_plan.md
```

## Run Examples

Use `uv`, not `pip` or bare `python`.

```sh
uv run python examples/02_next_step_by_step.py
```

FastAPI の SSE サンプル:

```sh
uv run uvicorn examples.08_fastapi_sse_sample:app --reload
```

FastAPI の dependency サンプル:

```sh
uv run uvicorn examples.09_fastapi_dependency_sample:app --reload
```
