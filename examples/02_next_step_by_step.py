def count_three():
    print("start")
    yield 1

    print("after 1")
    yield 2

    print("after 2")
    yield 3

    print("end")


def main():
    gen = count_three()

    print("created generator")
    print()

    print("first next:")
    print(next(gen))
    print()

    print("second next:")
    print(next(gen))
    print()

    print("third next:")
    print(next(gen))
    print()

    print("fourth next:")
    try:
        print(next(gen))
    except StopIteration:
        print("StopIteration: the generator is done")


if __name__ == "__main__":
    main()
