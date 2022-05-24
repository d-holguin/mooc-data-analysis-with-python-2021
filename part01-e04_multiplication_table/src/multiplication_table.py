#!/usr/bin/env python3


def main():
    for row in range(1, 11):
        for col in range(1, 11):
            num = row * col
            print(f"{num:2} ", end="")
        print()


if __name__ == "__main__":
    main()
