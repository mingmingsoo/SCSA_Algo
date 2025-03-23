#       0   1   2   3   4         5    6   7   8   9
adj = [[1], [2], [3], [4], [5], [6, 11], [7], [8], [9], [10],
#      10       11  12    13  14   15   16    17   18   19
       [16, 14], [12], [13], [28], [15], [28], [17], [18], [19], [20],
#      20      21   22   23   24   25   26   27   28   29
       [21, 25], [22], [23], [24], [31], [26], [27], [28], [29], [30],
#      30   31(도착점)
       [31], [32]]

score_info = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18,
              20, 13, 16, 19, 22, 24, 22, 24, 26, 28,
              30, 32, 34, 36, 38, 28, 27, 26, 25, 30, 35, 40, 0]

state = [0, 0, 0, 0]  # 말 위치 -1 이면 죽은거
dice = list(map(int, input().split()))
ans = 0


def btk(idx, score):
    global ans
    if (10 - idx) * 40 + score <= ans:
        return
    if idx == 10:
        ans = max(ans, score)
        return
    for i in range(4):
        if state[i] == -1:
            continue  # 죽은 말이면 넘어가!
        cur = state[i]
        go = dice[idx]

        # 일단 한번 이동인데 파란색이면 파란색으로 갈 수 있게
        next = adj[cur][-1]
        if next >= 32:
            next = -1
        else:
            # 나머지 칸 이동
            for j in range(go - 1):
                next = adj[next][0]
                if next >= 32:
                    next = -1
                    break
        possible = True
        for j in range(4):
            if i == j:
                continue
            if state[j] == next and next != - 1:
                possible = False
                break
        if possible:
            state[i] = next
            btk(idx + 1, score + score_info[next])
            state[i] = cur
        else:
            continue


btk(0, 0)  # 몇번째 다이스인지, 점수
print(ans)
