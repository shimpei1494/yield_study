def make_list():
    result = []

    for number in range(1, 4):
        print(f"make {number}")
        result.append(number)

    return result


def make_generator():
    for number in range(1, 4):
        print(f"make {number}")
        yield number


def main():
    print("list:")
    numbers = make_list()
    for number in numbers:
        print(f"use {number}")

    print()
    print("generator:")
    for number in make_generator():
        print(f"use {number}")


if __name__ == "__main__":
    main()
