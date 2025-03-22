'''
헷갈리는 점
이 겹치는게 2개 이상도되나?
ㅇㅇ 됨 ;; 어카지
재귀타는순간 쥬금
'''
T = int(input())
row = [0, -1, 0, 1, 0]
col = [0, 0, 1, 0, -1]
for tc in range(T):

    move_num, bc_num = map(int, input().split())
    A = list(map(int, input().split())) + [0]
    B = list(map(int, input().split())) + [0]
    bc_list = [list(map(int, input().split())) for i in range(bc_num)]
    maxi = 0
    grid = [[[] for i in range(10)] for i in range(10)]
    for bc in range(bc_num):
        c, r, bin, hp = bc_list[bc]
        r -= 1
        c -= 1
        for i in range(10):
            for j in range(10):
                if (abs(r - i) + abs(c - j)) <= bin:
                    grid[i][j].append((bc, hp))
    for i in range(10):
        for j in range(10):
            if grid[i][j]:
                grid[i][j].sort(key=lambda x: x[1], reverse=True)
    ans = 0
    r1 = c1 = 0
    r2 = c2 = 9
    for move in range(move_num + 1):
        if grid[r1][c1] and not grid[r2][c2]:
            ans += grid[r1][c1][0][1]
        elif not grid[r1][c1] and grid[r2][c2]:
            ans += grid[r2][c2][0][1]
        elif grid[r1][c1] and grid[r2][c2]:
            maxi = 0
            for abc, ahp in grid[r1][c1]:
                for bbc, bhp in grid[r2][c2]:
                    if abc == bbc:
                        maxi = max(maxi, ahp)
                    else:
                        maxi = max(maxi, ahp + bhp)

            ans += maxi
        r1 = r1 + row[A[move]]
        c1 = c1 + col[A[move]]
        r2 = r2 + row[B[move]]
        c2 = c2 + col[B[move]]
    print(f"#{tc + 1} {ans}")
