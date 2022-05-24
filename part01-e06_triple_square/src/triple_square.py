#!/usr/bin/env python3

def triple(x):
    return x*3


def square(x):
    return x**2


def main():
    for i in range(1, 11):
        tripled = triple(i)
        squared = square(i)
        if squared > tripled:
            break
        print(f"triple({i})=={tripled} square({i})=={squared}")


if __name__ == "__main__":
    main()
