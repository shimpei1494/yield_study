from pathlib import Path


def read_non_empty_lines(path):
    with Path(path).open(encoding="utf-8") as file:
        for line in file:
            stripped_line = line.strip()

            if stripped_line:
                yield stripped_line


def main():
    for line in read_non_empty_lines("data/sample.txt"):
        print(line)


if __name__ == "__main__":
    main()
