#!/usr/bin/env python
import argparse


def fact(x: int) -> list:
    """
    Generate factorial sequence from 1 to x.
    """
    if x <= 0:
        return []
    seq = [1]
    if x == 1:
        return seq

    curr_factorial = 1
    for i in range(2, x + 1):
        curr_factorial *= i
        seq.append(curr_factorial)

    return seq


def main(x: int):
    print(f"{x}:\t{fact(x)}")


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
