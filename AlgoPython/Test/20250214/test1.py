'''
신입사원

문제 설명
    모든 신입사원은 K개의 명함을 가지고 있음
    8방향으로 인접하게 명함을 전달
    I들은 12시부터 시계방향으로
    E들은 12시부터 반시계방향으로 전달

    강당에서 전달된 명함의 총! 갯수는?

입력
    행 N, 열 M, 명함갯수 K
    1은 I, 2는 E
구상
    주변에 몇명이 있냐?, k-몇명 합
특이점
    명함을 나눠주는 시간이 제한되어 있는게 아닌데
    시계, 반시계가 의미가 있나?ㅜㅜㅜ
    그렇게 치면 가운데 1도 4장은 못주는데.....

반례
1
3 3 3
1 1 1
1 1 1
1 1 1
정답 27
주변에 친구가 많아도 가지고 있는 카드수 만큼만 줄 수 있음
'''

def count(r, c):
    total = 0
    for k in range(8):
        nr = r + row[k]
        nc = c + col[k]
        if (not (0 <= nr < n and 0 <= nc < m)):
            continue
        if (grid[nr][nc] != 0): # 친구가 있으면
            total += 1
    return total

T = int(input())
for tc in range(T):

    n, m, card = map(int, input().split())
    grid = [list(map(int, input().split())) for i in range(n)]

    around = [[0] * m for i in range(n)] # 8방에 친구가 몇명 앉아있는지 적는 행렬
    row = [-1, -1, 0, 1, 1,  1,  0, -1]
    col = [0,   1, 1, 1, 0, -1, -1, -1]
    ans = 0

    for i in range(n):
        for j in range(m):
            if (grid[i][j] != 0): # 빈자리가 아니면 주변에 몇명있냐?
                around[i][j] = count(i, j)

    for i in range(n):
        for j in range(m):
            if (around[i][j] != 0): # 자리에 앉아있는 애들 중에
                if (around[i][j] < card): # 총 카드수보다 친구들이 적게 앉아있으면
                    ans += around[i][j] # 그것만큼 더해주고
                else:
                    ans += card # 더 많이 앉아있으면 카드수 만큼 더해줌

    print(f"#{tc+1} {ans}")