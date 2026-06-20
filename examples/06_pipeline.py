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


def main():
    for value in squared(only_even(numbers())):
        print(value)


if __name__ == "__main__":
    main()
