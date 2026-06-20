def count_three():
    yield 1
    yield 2
    yield 3


def main():
    for number in count_three():
        print(number)


if __name__ == "__main__":
    main()
