#!/usr/bin/env python
import argparse
from pprint import pprint

SEQ_SIZE = 10


def diff_seq(n: int, s: int = SEQ_SIZE) -> list:
    seqs = []
    seq = []
    x = 1

    # Base sequence
    for i in range(s if n <= s else n + 1):
        seq.append(x**n)
        x += 1
    seqs.append(seq)

    # Difference sequences
    for _ in range(n):
        seq = []
        for i in range(len(seqs[-1]) - 1):
            seq.append(seqs[-1][i + 1] - seqs[-1][i])
        seqs.append(seq)

    return seqs


def main(n: int, s: int):
    pprint(diff_seq(n, s))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="")
    parser.add_argument(
        "-n",
        "--n",
        type=int,
        required=True,
        help="Exponent",
    )
    parser.add_argument(
        "-s",
        "--s",
        type=int,
        required=True,
        help="Minimum sequence size.",
    )
    args = parser.parse_args()
    n = args.n
    s = args.s

    main(n, s)
