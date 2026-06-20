def normal_function():
    return 1
    return 2


def generator_function():
    yield 1
    yield 2


def main():
    print("normal_function() returns:")
    print(normal_function())

    print()
    print("generator_function() returns:")
    gen = generator_function()
    print(gen)

    print()
    print("values from the generator:")
    print(next(gen))
    print(next(gen))


if __name__ == "__main__":
    main()
