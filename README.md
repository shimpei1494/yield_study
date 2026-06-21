# yield-study

Python の `yield` を初学者向けに整理するための学習リポジトリです。

`article/zenn_draft.md` をもとに Zenn 記事を書く想定で、記事だけでも流れが分かるようにしつつ、動きを確認したい場合は `examples/` のコードを `uv` で実行できます。

GitHub リポジトリ:

https://github.com/shimpei1494/yield_study

## Setup

`uv` のインストールは済んでいる前提です。

```sh
git clone https://github.com/shimpei1494/yield_study.git
cd yield_study
uv sync
```

`uv sync` で、`pyproject.toml` と `uv.lock` をもとに必要な依存関係が用意されます。

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
  11_for_iterable_iterator.py
data/
  sample.txt
docs/
  implementation_plan.md
```

## Run Examples

Use `uv`, not `pip` or bare `python`.

まずは `yield` の一時停止と再開が見える例がおすすめです。

```sh
uv run python examples/02_next_step_by_step.py
```

リストとジェネレータの違い:

```sh
uv run python examples/04_list_vs_generator.py
```

ストリーミングの基本:

```sh
uv run python examples/07_streaming_basic.py
```

`contextmanager` と `yield`:

```sh
uv run python examples/10_contextmanager.py
```

`for`、イテラブル、イテレータの補足:

```sh
uv run python examples/11_for_iterable_iterator.py
```

FastAPI の SSE サンプル:

```sh
uv run uvicorn examples.08_fastapi_sse_sample:app --reload
```

ブラウザで開く:

```text
http://127.0.0.1:8000
```

FastAPI の dependency サンプル:

```sh
uv run uvicorn examples.09_fastapi_dependency_sample:app --reload
```

ブラウザで開く:

```text
http://127.0.0.1:8000/items
```

## Article Draft

記事草稿は `article/zenn_draft.md` にあります。
