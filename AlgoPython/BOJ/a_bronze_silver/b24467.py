import sys

lst = []
try:
    while True:
        line = list(map(int, input()))
        if not line:  # 빈 입력이면 종료
            break
        lst.append(line)
except EOFError:  # 입력이 끝나면 종료
    pass

      # 0    1    2    3    4     5        6   7    8    9       10      11    12    13    14    15
adj = [[1], [2], [3], [4], [5], [6, 20], [7], [8], [9], [10], [11, 23], [12], [13], [14], [15], [16],

      # 16    17   18     19   20    21      22       23   24    25    26    27   28
       [17], [18], [19], [0], [21], [22], [27, 26], [24], [22], [15], [25], [28], [0]]
ans = "LOSE"
lo = 0
for idx, yut in enumerate(lst):
    go = 0
    if yut.count(0) == 1:
        go = 1
    elif yut.count(0) == 2:
        go = 2
    elif yut.count(0) == 3:
        go = 3
    elif yut.count(0) == 4:
        go = 4
    elif yut.count(0) == 0:
        go = 5

    # 일단 한 칸 이동
    lo = adj[lo][-1]
    if lo == 0 and idx < len(lst)-1:
        ans = "WIN"
        break
    # 그 다음 이동
    for _ in range(go - 1):
        lo = adj[lo][0]
        if lo == 0 and idx < len(lst) - 1:
            ans = "WIN"
            break
    if ans == "WIN":
        break
print(ans)