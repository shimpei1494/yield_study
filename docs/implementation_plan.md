# Python yield Study Implementation Plan

このリポジトリは、Python の `yield` を初学者が段階的に理解し、最終的に Zenn 記事として説明できる状態に整理するための学習用リポジトリです。

## ゴール

- `yield` と `return` の違いを、実行結果から説明できるようにする。
- `next()`、`for`、ジェネレータ、遅延評価の関係を小さなコードで確認できるようにする。
- 実務で `yield` が使われる場面として、ストリーミング、SSE、FastAPI の dependency、context manager を説明できるようにする。
- Zenn 記事では、前半を基礎理解、後半を実用例として構成する。

## 記事の想定構成

### 1. なぜ yield は分かりづらいのか

最初に、初学者がつまずきやすい疑問を明示する。

- `return` と何が違うのか。
- `yield` したあと関数は終わるのか。
- なぜ `for` で回せるのか。
- いつ関数本体が実行されるのか。
- メモリ効率が良いとはどういう意味か。

対応コード:

- `examples/01_return_vs_yield.py`

### 2. return と yield を並べて見る

`return` は関数を終了するが、`yield` は値を外に渡して一時停止する、という違いを最小コードで示す。

対応コード:

- `examples/01_return_vs_yield.py`

### 3. next() で一歩ずつ動かす

`yield` の前後に `print()` を置き、処理がどこで止まり、どこから再開するのかを確認する。

ここが基礎編の中心。`for` より先に `next()` を見せる。

対応コード:

- `examples/02_next_step_by_step.py`

### 4. for は内部で next() している

`for` でジェネレータを回す例を示し、`StopIteration` の詳細には深入りしすぎず、まずは「順番に取り出している」と説明する。

対応コード:

- `examples/03_for_loop.py`

### 5. リストとジェネレータの違い

リストは先に全部作る。ジェネレータは必要になった分だけ作る。大量データや無限列に向いている、という理解につなげる。

対応コード:

- `examples/04_list_vs_generator.py`

### 6. ファイルを1行ずつ処理する

実用例の入り口として、ファイルを1行ずつ読み、必要な行だけ処理する例を置く。

対応コード:

- `examples/05_file_reader.py`
- `data/sample.txt`

### 7. ジェネレータでパイプラインを作る

値を一気に加工するのではなく、複数の処理を流れ作業のようにつなぐ例を示す。

対応コード:

- `examples/06_pipeline.py`

### 8. ストリーミングレスポンスと yield

AI からのレスポンスを少しずつ受け取り、画面へ返すような場面を想定する。

まずは外部 AI API にはつながず、疑似的なトークン列を `yield` する。FastAPI の `StreamingResponse` と SSE の `text/event-stream` を使う記事用コードにする。

対応コード:

- `examples/07_streaming_basic.py`
- `examples/08_fastapi_sse_sample.py`

説明ポイント:

- 全文を作ってから返すのではなく、`yield` するたびに一部を返す。
- SSE はブラウザの `EventSource` で受け取れる一方向のストリーム。
- 実際の AI API に接続する場合も、「届いた chunk を順に `yield` する」と考えれば読みやすい。

### 9. FastAPI の dependency で yield を使う

DB セッションのようなリソースを用意し、リクエスト処理後に閉じる例を示す。

対応コード:

- `examples/09_fastapi_dependency_sample.py`

説明ポイント:

- `yield` の前は準備。
- `yield` した値がエンドポイントに渡される。
- `yield` の後、特に `finally` は後片付け。
- これは「処理の途中で外側に制御を渡し、あとで戻ってくる」という `yield` の性質を使っている。

### 10. contextmanager と yield

`contextlib.contextmanager` を使い、`with` 文の前後処理を `yield` で表現する。

対応コード:

- `examples/10_contextmanager.py`

説明ポイント:

- `yield` の前は `with` ブロックに入る前の準備。
- `yield` した値は `as` に入る。
- `yield` の後は `with` ブロックを抜けるときの後片付け。
- FastAPI の dependency with yield と同じ構造として理解できる。

## 実装方針

- 各サンプルは、記事の節番号と対応するファイル名にする。
- 基礎編のコードは実行できる小さなスクリプトにする。
- FastAPI のサンプルは、アプリ全体を作り込みすぎず、記事で読める最小構成にする。
- 外部 AI API には接続しない。疑似トークンを使い、`yield` の役割に集中する。
- 依存管理と実行は `uv` を使う。

## 想定ディレクトリ構成

```text
yield_study/
  AGENTS.md
  README.md
  pyproject.toml
  uv.lock
  data/
    sample.txt
  docs/
    implementation_plan.md
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
  article/
    zenn_draft.md
```

## uv コマンド

依存追加:

```sh
uv add fastapi uvicorn
```

Python スクリプト実行:

```sh
uv run python examples/02_next_step_by_step.py
```

FastAPI サンプル実行:

```sh
uv run uvicorn examples.08_fastapi_sse_sample:app --reload
```

## Zenn 記事の結論メモ

`yield` は「値を返すだけの文法」ではなく、「処理の途中で外側に制御を渡し、あとで続きに戻ってこられる仕組み」。

だから、次のような場面で使われる。

- 値を少しずつ作る。
- レスポンスを少しずつ流す。
- リソースを貸し出して、あとで閉じる。
- `with` 文の前後処理を書く。
