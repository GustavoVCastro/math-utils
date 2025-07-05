#!/usr/bin/env python
import argparse


def fat(x: int) -> list:
    lista = [1]
    for i in range(2, x + 1):
        n = i
        l = reversed(range(1, i))
        for j in l:
            n *= j
        lista.append(n)

    return lista


def main(x: int):
    print(f"{x}:\t{fat(x)}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Generate factorial sequence up until x."
    )
    parser.add_argument(
        "-x",
        "--x",
        type=int,
        required=True,
        help="Size of the sequence",
    )
    args = parser.parse_args()
    x = args.x

    main(x)
