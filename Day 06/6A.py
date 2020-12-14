# 1-line solution

import os.path

with open(os.path.join("Day 06", "input.txt")) as f:
    print(sum(map(len, ["".join(set(s.replace("\n", ""))) for s in f.read().split("\n\n")])))
