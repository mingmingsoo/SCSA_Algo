'''
19:18~
문제 설명
    dfs
1. 먼저 최대 상금 계산
2. 최대상금 먹게끔만 움직임

3 3 1
aaa
aaa
aaa
aa
레벨업이 4임
'''
import sys

sys.setrecursionlimit(10 ** 5)

from collections import defaultdict

n, m, tmp = map(int, input().split())
grid = [list(input()) for i in range(n)]
target_word = input()
target = defaultdict(int)
my_have = dict()
row = [-1, 0, 1, 0]
col = [0, 1, 0, -1]
for w in target_word:
    target[w] += 1
    my_have[w] = 0
total_have = defaultdict(int)

for i in range(n):
    for j in range(m):
        total_have[grid[i][j]] += 1
# print(total_have)

levelup = 0  # 최대 상금 금액.
# print(total_have)
# print(target)
while True:
    limit = False
    for key in target:
        if total_have[key] - target[key] >= 0:
            total_have[key] -= target[key]
        else:
            limit = True
            break
    if limit:
        break
    levelup += 1
# print(total_have)


target_word *= levelup

r, c = 0, 0
ans = ""
visited = [[False] * m for i in range(n)]
for word in target_word:
    for i in range(n):
        find = False
        for j in range(m):
            if grid[i][j] == word and not visited[i][j]:
                nr, nc = i, j
                if nr > r:
                    ans += "D" * (nr - r)
                if nr < r:
                    ans += "U" * (r - nr)
                if nc > c:
                    ans += "R" * (nc - c)
                if nc < c:
                    ans += "L" * (c - nc)
                ans += "P"
                visited[i][j] = True
                find = True
                r = nr
                c = nc
                break
        if find:
            break

karo = n - r - 1
ans += "D" * karo
sero = m - c - 1
ans += "R" * sero
print(levelup, len(ans))
print(ans)
