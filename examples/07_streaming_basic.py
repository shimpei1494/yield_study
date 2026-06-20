import time


def fake_ai_tokens():
    tokens = ["こんにちは", "。", "yield", "で", "少しずつ", "返します", "。"]

    for token in tokens:
        time.sleep(0.2)
        yield token


def main():
    for token in fake_ai_tokens():
        print(token, end="", flush=True)

    print()


if __name__ == "__main__":
    main()
