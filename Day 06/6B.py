# 1-line solution

import os.path

with open(os.path.join("Day 06", "input.txt")) as f:
    print(sum([len(set.intersection(*(list(map(set, s.split("\n")))))) for s in f.read().split("\n\n")]))
