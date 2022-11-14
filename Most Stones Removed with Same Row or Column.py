from collections import defaultdict
from itertools import chain
from typing import List


def removeStones(stones: List[List[int]]):
    print(stones)
    rows, cols = defaultdict(list), defaultdict(list)
    en_stones = list(enumerate(stones))
    print(en_stones)
    for s, (r, c) in enumerate(stones):
        rows[r].append(s)
        cols[c].append(s)
    print(rows, cols)
    seen, n = set(), len(stones)

    def dfs(s):
        if s in seen:
            return 0
        seen.add(s)
        r, c = stones[s]
        for ss in chain(rows[r], cols[c]): dfs(ss)
        return 1

    c = sum(dfs(s) for s in range(n))

    print(n - c)

input_list = [[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]
removeStones(input_list)

