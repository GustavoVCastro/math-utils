#!/usr/bin/env python
import math
import argparse

"""
Almost here means all divisors other than 1.
"""


def get_almost_all_divisors(x: int) -> set:
    s = set()
    for i in range(2, x + 1):
        if x % i == 0:
            s.add(i)
    return s


"""
grp_lt means Get Relative Primes of x that are Less Than x.
"""


def grp_lx(x: int) -> set | None:
    s = set()
    d = get_almost_all_divisors(x)
    # for i in range(2, math.floor(x / 2) + 1):
    for i in range(2, x):
        if get_almost_all_divisors(i).isdisjoint(d):
            s.add(i)

    return None if (not s) else s


def main(x: int):
    print(f"{x}:\t{sorted(list(grp_lx(x)))}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Find relative primes of x that are less than x."
    )
    parser.add_argument(
        "-x",
        "--x",
        type=int,
        required=True,
        help="Number up to which its relative primes will be found",
    )
    args = parser.parse_args()
    x = args.x

    main(x)
