dice = list(map(int, input().split()))  # 이 만치 갈 수있음
#       0     1   2    3    4     5       6    7    8     9     10
adj = [[1], [2], [3], [4], [5], [6, 20], [7], [8], [9], [10], [11, 23],
#       11     12   13    14     15       16    17   18     19    20    21
       [12], [13], [14], [15], [16, 25], [17], [18], [19], [31], [21], [22],
#       22    23    24    25    26    27    28    29    30    31
       [28], [24], [28], [26], [27], [28], [29], [30], [31], [32]
       ]
score_info = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 13, 16, 19, 22, 24, 28, 27, 26,
              25, 30, 35, 40, 0]
sel = [0] * 10
ans = 0


def duple(horse,cur,where):
    for i in range(4):
        if i != horse and  cur != 32 and cur == where[i]:
            return True
    return False


def duple_perm(idx):
    global ans
    if idx == 10:
        where = [0] * 4
        score = 0
        for idx, horse in enumerate(sel):
            if where[horse] == 32:
                return # 도착칸에 있는 애를 골랐엉
            go = dice[idx]
            cur = where[horse]
            cur = adj[cur][-1]  # 일단 한 칸 이동
            if cur == 32:
                where[horse] = 32  # 혹시 도착 했나?
                continue
            for _ in range(go - 1):
                cur = adj[cur][0]
                if cur == 32:
                    where[horse] = 32  # 혹시 도착 했나?
                    break
            if duple(horse,cur,where):
                return
            where[horse] = cur
            score += score_info[cur]
        ans = max(ans,score)
        return

    for i in range(4):
        sel[idx] = i
        duple_perm(idx + 1)


duple_perm(0)
print(ans)

'''
# 17825 코드트리 윷놀이 사기단(백준 주사위 윷놀이)
# 체감난이도 골2

# 문제 풀고 나서 기록

    문제 시작 14:00
    첫 제출 15:11
    코드트리 맞은 코드 제출 16:19 -> 백준에서 틀림
    백준 맞은 코드 제출 18:33

    메모리 115824 KB
    시간 840 ms

    회고
    1. 구현에서 놓친부분이 많아서 아쉬웠다. 25에 위치할 때 처리나 그런 부분이 .. 너무너무 아쉽당
    2. 문제 이해 못한 것도 바보같다.................................
    3. 코드트리에서 맞은 코드 로직이 완전 틀렸는데 맞춘 것도 웃기다.........

    틀린이유
        .... 가려는 위치에 말이 있으면 말이 대기하는 건 줄 알았음..............
        또 죽은 말을 고르면 그냥 다음 턴으로 넘어가는 줄 알았다...
        문제를 잘 읽자...............................................
        .....ㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠ
        ㅜㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠ
        ㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠ
        ㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠ

# 문제 풀면서의 기록
문제설명
    4개의 말이 있을 때 받을 수 있는 최대 점수는?
구상
    1,2,3,4 중복순열
반례
5 5 5 5 5 5 5 5 5 5
정답 130

'''
'''
문제설명
    4개의 말이 있을 때 받을 수 있는 최대 점수는?
구상
    1,2,3,4 중복순열
반례
5 5 5 5 5 5 5 5 5 5
정답 130

25 처리해주는 게 필요함.
'''
cube = list(map(int, input().split()))  # 짬푸할 칸.
sel = [0] * 10
ans = 0
score = [[2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40],
         [10, 13, 16, 19, 25],
         [20, 22, 24, 25],
         [30, 28, 27, 26, 25],
         [25, 30, 35, 40]]


def perm(idx):
    global ans
    if idx == 10:
        ele_score = 0
        state = [(0, -1) for i in range(4)]
        for i in range(10):
            if (10 - i) * 40 + ele_score < ans:
                return
            horse = sel[i] - 1
            dice = cube[i]
            if (state[horse][0], state[horse][1]) == (-1, -1):
                return
            nr, nc = state[horse][0], state[horse][1] + dice

            if (nr, nc) == (0, 4):  # 10
                (nr, nc) = (1, 0)  # 위치 바꿔줌
            elif (nr, nc) == (0, 9):  # 20
                (nr, nc) = (2, 0)
            elif (nr, nc) == (0, 14):  # 30
                (nr, nc) = (3, 0)
            elif (nr, nc) == (0, 19):  # 40
                (nr, nc) = (3, 7)
            if 0 < nr < 4 and nc >= len(score[nr]) - 1:
                nc = nc - len(score[nr]) + 1
                nr = 4

            if nr == 0 and nc > 19:
                state[horse] = (-1, -1)
                continue
            elif nr == 4 and nc > 3:
                state[horse] = (-1, -1)
                continue

            for j in range(4):
                if j == horse:
                    continue
                hr, hc = state[j]
                if (hr, hc) == (nr, nc):
                    return
            state[horse] = (nr, nc)
            ele_score += score[nr][nc]
        ans = max(ans, ele_score)
        return
    for i in range(1, 5):
        sel[idx] = i
        perm(idx + 1)


perm(0)
print(ans)
