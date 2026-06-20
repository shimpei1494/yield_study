from contextlib import contextmanager


@contextmanager
def open_resource():
    print("setup")

    try:
        yield "resource"
    finally:
        print("cleanup")


def main():
    with open_resource() as resource:
        print(f"use {resource}")


if __name__ == "__main__":
    main()
