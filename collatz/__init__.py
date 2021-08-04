"""
Collatz Conjecture.

A simple Plot of the Collatz Conjecture

Copyright Manas Mengle 2021
"""
import json
import os
import statistics
from collections import Counter

from matplotlib import pyplot as plt


def main(max_seed=10465, start_seed=1):
    """Run Collatz Conjecture."""
    with plt.ion():
        start = start_seed
        fig, ax = plt.subplots()
        fail_fig, fail_ax = plt.subplots()
        fail_bottom = [1]
        fail_top = [0]
        bottom = []
        top = []
        bottom.append(1)
        top.append(start)
        ax.plot(bottom, top)
        inLoop = True
        while inLoop:
            try:
                if (top[-1] % 2) == 0:  # Even
                    top.append(top[-1] / 2)
                    bottom.append(bottom[-1] + 1)
                else:  # Odd
                    top.append(top[-1] * 3 + 1)
                    bottom.append(bottom[-1] + 1)
                ax.plot(bottom, top)
                if top[-1] == 4:  # Loop failed
                    fail_bottom.append(fail_bottom[-1] + 1)
                    fail_top.append(bottom[-1])
                    fail_ax.scatter(fail_bottom, fail_top)
                    print(top[0], "failed after", bottom[-1], "iterations")
                    bottom.clear()
                    top.clear()
                    start += 1
                    if start == max_seed:
                        inLoop = False
                        return fail_top
                    bottom.append(1)
                    top.append(start)
            except KeyboardInterrupt:
                fail_bottom.append(fail_bottom[-1] + 1)
                fail_top.append(bottom[-1])
                fail_ax.scatter(fail_bottom, fail_top)
                print(top[0], "failed after", bottom[-1], "iterations")
                bottom.clear()
                top.clear()
                start += 1
                inLoop = False
                return fail_top

def mode(sample):
    """Calculate the mode of a given sample."""
    c = Counter(sample)
    return [k for k, v in c.items() if v == c.most_common(1)[0][1]]


def median(sample):
    """Calculate the median of a given sample."""
    return statistics.median(sample)


def mean(sample):
    """Calculate the mean of a given sample."""
    return statistics.mean(sample)


if __name__ == "__main__":
    fail_top = main()
    with open(os.path.join(os.path.dirname(__name__), "score.txt"), "w") as f:
        json.dump(fail_top, f, indent=4, sort_keys=True)
        json.dump(
            {
                "mode": mode(fail_top),
                "mean": mean(fail_top),
                "median": median(fail_top),
            },
            f,
            indent=4,
            sort_keys=True,
        )
    print("mode:", mode(fail_top))
    print("median:", median(fail_top))
    print("mean:", mean(fail_top))
    input()
