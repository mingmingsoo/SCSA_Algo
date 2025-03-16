'''
시도횟수: 1회
실행시간: 576 ms
메모리: 113420 KB
'''
import itertools


def score_cal(sel):
    global maxi
    ele_ans = [0] * m
    for j in range(m):
        zero, one = 0, 0
        for ii in sel:
            if grid[ii][j] == 0: zero += 1
            else: one += 1
        if zero > one: ele_ans[j] = 0
        else: ele_ans[j] = 1

    ele_score = 0
    for j in range(m):
        if ele_ans[j] == ans[j]: ele_score += 1
    maxi = max(maxi, ele_score)

n, m = map(int, input().split())
ans = list(map(int, input().split()))
grid = [list(map(int, input().split())) for i in range(n)]

maxi = 0
for i in range(n):
    score = 0
    for j in range(m):
        if grid[i][j] == ans[j]: score += 1
    maxi = max(score, maxi)
origin_maxi = maxi

arr = list(range(n))
for i in range(3, n + 1, 2):
    combi_list = itertools.combinations(arr, i)
    for sel in combi_list:
        score_cal(sel)

if maxi > origin_maxi:
    print(1)
else:
    print(0)
