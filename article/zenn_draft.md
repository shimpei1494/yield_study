---
title: "Python の yield を、止まる・続く・少しずつ返すで理解する"
emoji: "🐍"
type: "tech"
topics: ["python", "yield", "generator", "fastapi"]
published: false
---

Python の `yield` は、初学者にとって少しつかみにくい文法です。

`return` なら「値を返して関数が終わる」と考えればよいですが、`yield` は値を返したあとも、関数の途中からまた動きます。

この記事では、`yield` を次の順番で整理します。

- `return` との違い
- `next()` で一歩ずつ動かす方法
- `for` との関係
- リストとの違い
- ファイル読み込みやパイプラインでの使い方
- FastAPI や SSE など、実用寄りの使い方

最初から難しい用語をたくさん覚える必要はありません。

まずは、`yield` をこう捉えるところから始めます。

> `yield` は、値を外に渡して、そこで一時停止する。
> 次に呼ばれると、止まった場所の続きから動く。

この記事内のコードは、リポジトリの `examples/` にも置いてあります。動きを確認したい場合は、次のように実行できます。

```sh
uv run python examples/02_next_step_by_step.py
```

## return は終わる、yield は止まる

まずは `return` と `yield` を並べて見ます。

```python
def normal_function():
    return 1
    return 2


def generator_function():
    yield 1
    yield 2
```

`normal_function()` は `return 1` で関数が終わります。なので、下の `return 2` には到達しません。

一方で、`generator_function()` は少し違います。`yield 1` で値を返しますが、関数は完全には終わりません。そこで一時停止します。

このように `yield` を含む関数は、呼び出すと普通の値ではなく **ジェネレータ** を返します。

```python
gen = generator_function()
print(gen)
```

この時点では、まだ `yield 1` も `yield 2` も実行されていません。

ここが最初の大事なポイントです。

> `yield` を含む関数は、呼び出しただけでは中身が進まない。
> `next()` されたときに、次の `yield` まで進む。

対応コード:

```sh
uv run python examples/01_return_vs_yield.py
```

## next() で一歩ずつ動かす

`yield` の動きは、`for` より先に `next()` で見ると分かりやすいです。

```python
def count_three():
    print("start")
    yield 1

    print("after 1")
    yield 2

    print("after 2")
    yield 3

    print("end")
```

この関数を呼び出します。

```python
gen = count_three()
```

この時点では、まだ `"start"` は表示されません。ジェネレータが作られただけです。

次に `next()` します。

```python
print(next(gen))
```

すると、関数の中身が `yield 1` まで進みます。

```text
start
1
```

もう一度 `next()` します。

```python
print(next(gen))
```

すると、前回止まった `yield 1` の続きから動きます。

```text
after 1
2
```

さらにもう一度 `next()` します。

```python
print(next(gen))
```

```text
after 2
3
```

ここまでで、3つの値を取り出しました。

もう一度 `next()` すると、関数は最後まで進みます。

```python
print(next(gen))
```

このとき `"end"` は表示されますが、次の `yield` がないため `StopIteration` が発生します。

この挙動をまとめると、こうです。

- `next(gen)` で関数が動き始める
- `yield` に到達すると値を外に渡して止まる
- 次の `next(gen)` で止まった場所の続きから動く
- もう `yield` がなければ終了する

対応コード:

```sh
uv run python examples/02_next_step_by_step.py
```

## for は next() を順番に呼んでいる

普段は、ジェネレータを `next()` で直接扱うより、`for` で回すことが多いです。

```python
def count_three():
    yield 1
    yield 2
    yield 3


for number in count_three():
    print(number)
```

出力はこうなります。

```text
1
2
3
```

`for` は、内部で次のようなことをしています。

```python
gen = count_three()

print(next(gen))
print(next(gen))
print(next(gen))
```

実際には、最後に `StopIteration` が発生したところでループを止めてくれます。

つまり、こう考えると自然です。

> `for` は、ジェネレータから値を1つずつ取り出している。

対応コード:

```sh
uv run python examples/03_for_loop.py
```

## リストは全部作る、ジェネレータは少しずつ作る

`yield` が便利なのは、値を必要な分だけ作れるところです。

たとえば、リストを返す関数を書いてみます。

```python
def make_list():
    result = []

    for number in range(1, 4):
        print(f"make {number}")
        result.append(number)

    return result
```

この関数は、先にすべての値を作ってからリストを返します。

```python
numbers = make_list()

for number in numbers:
    print(f"use {number}")
```

出力はこうなります。

```text
make 1
make 2
make 3
use 1
use 2
use 3
```

次に、ジェネレータで書きます。

```python
def make_generator():
    for number in range(1, 4):
        print(f"make {number}")
        yield number
```

これを `for` で使います。

```python
for number in make_generator():
    print(f"use {number}")
```

出力はこうなります。

```text
make 1
use 1
make 2
use 2
make 3
use 3
```

リスト版は「全部作る」してから「使う」でした。

ジェネレータ版は「1つ作る」「1つ使う」を交互に行っています。

この違いが、大量データを扱うときに効いてきます。すべてをメモリに載せなくても、必要な分だけ処理できるからです。

対応コード:

```sh
uv run python examples/04_list_vs_generator.py
```

## ファイルを1行ずつ処理する

実用的な例として、ファイルを1行ずつ読む処理を考えます。

```python
from pathlib import Path


def read_non_empty_lines(path):
    with Path(path).open(encoding="utf-8") as file:
        for line in file:
            stripped_line = line.strip()

            if stripped_line:
                yield stripped_line
```

この関数は、ファイル全体をリストにして返しません。

1行読み、空行でなければ `yield` します。

```python
for line in read_non_empty_lines("data/sample.txt"):
    print(line)
```

ファイルが大きくなっても、「読んだ行を順番に処理する」という形を保てます。

対応コード:

```sh
uv run python examples/05_file_reader.py
```

## ジェネレータで処理をつなぐ

ジェネレータは、複数の処理をつなぐときにも使えます。

たとえば、次の3つの処理を考えます。

- 数字を作る
- 偶数だけに絞る
- 2乗する

```python
def numbers():
    for number in range(1, 8):
        yield number


def only_even(values):
    for value in values:
        if value % 2 == 0:
            yield value


def squared(values):
    for value in values:
        yield value * value
```

これらをつなぐと、次のように書けます。

```python
for value in squared(only_even(numbers())):
    print(value)
```

出力はこうです。

```text
4
16
36
```

これは、すべての値を一度リストにしてから加工しているわけではありません。

必要な値が流れてきたら、次の処理に渡しています。

こういう処理は、データの流れを作っているので **パイプライン** と呼ばれることがあります。

対応コード:

```sh
uv run python examples/06_pipeline.py
```

## ここまでのまとめ

ここまでで、`yield` の基本はかなり見えてきました。

- `yield` を含む関数はジェネレータを返す
- 関数の中身は、呼び出しただけでは進まない
- `next()` されると、次の `yield` まで進む
- `yield` は値を返して一時停止する
- 次の `next()` では、止まった場所の続きから動く
- `for` はジェネレータから値を1つずつ取り出している
- リストと違い、ジェネレータは値を少しずつ作れる

この理解を土台にすると、実務で出てくる `yield` も読みやすくなります。

次は、ストリーミングレスポンス、FastAPI の dependency、`contextmanager` での `yield` を見ていきます。
