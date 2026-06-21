def count_three():
    yield 1
    yield 2
    yield 3


def main():
    print("list:")
    for value in [1, 2, 3]:
        print(value)

    print()
    print("str:")
    for char in "abc":
        print(char)

    print()
    numbers = [1, 2, 3]
    print("iter(list) is list:")
    print(iter(numbers) is numbers)

    print()
    gen = count_three()
    print("iter(generator) is generator:")
    print(iter(gen) is gen)


if __name__ == "__main__":
    main()
