'''
계단은 무조건 두개
계단A를 박아두고  사람 고르고, 안골라진 애가 계단 B임
그리고 그 선택된 애들을 거리 오름차순으로 정렬
그 max가 ans 가 되고 최솟값으로 갱신해줘야함.
'''
T = int(input())

def subset(sidx):
    global ans
    if sidx == len(people):
        A = []
        B = []
        for idx, s in enumerate(sel):
            if s:
                A.append(people[idx])
            else:
                B.append(people[idx])
        ar, ac, at = stairs[0]
        br, bc, bt = stairs[1]
        A_dist = []
        B_dist = []
        for pr, pc in A:
            A_dist.append(abs(pr - ar) + abs(pc - ac))
        for pr, pc in B:
            B_dist.append(abs(pr - br) + abs(pc - bc))
        # 거리 가까운 순으로 정렬
        A_dist.sort(reverse=True)
        B_dist.sort(reverse=True)
        # print(A_dist)
        # print(B_dist)

        A_end = 0
        A_tmp = []
        # A 계단 처리
        time = 0
        while True:
            for i in range(len(A_tmp) - 1, -1, -1):
                if A_tmp[i] == at + 1:
                    A_tmp.pop(i)

            if not A_dist and not A_tmp:
                A_end = time
                break
            for i in range(len(A_dist) - 1, -1, -1):
                if A_dist[i] == time and len(A_tmp) < 3:
                    A_dist.pop(i)
                    A_tmp.append(0)
                elif A_dist[i] < time and len(A_tmp) < 3:
                    A_dist.pop(i)
                    A_tmp.append(1)
                else:
                    break
            for idx, down in enumerate(A_tmp):  # 대기 1분
                A_tmp[idx] += 1
            time += 1

        B_end = 0
        B_tmp = []
        # B 계단 처리
        time = 0
        while True:
            for i in range(len(B_tmp) - 1, -1, -1):
                if B_tmp[i] == bt + 1:
                    B_tmp.pop(i)

            if not B_dist and not B_tmp:
                B_end = time
                break
            for i in range(len(B_dist) - 1, -1, -1):
                if B_dist[i] == time and len(B_tmp) < 3:
                    B_dist.pop(i)
                    B_tmp.append(0)
                elif B_dist[i] < time and len(B_tmp) < 3:
                    B_dist.pop(i)
                    B_tmp.append(1)
                else:
                    break
            for idx, down in enumerate(B_tmp):  # 대기 1분
                B_tmp[idx] += 1
            time += 1
        mini = max(A_end, B_end)
        ans = min(ans, mini)
        return

    sel[sidx] = 0
    subset(sidx + 1)
    sel[sidx] = 1
    subset(sidx + 1)


for tc in range(T):
    n = int(input())
    grid = [list(map(int, input().split())) for i in range(n)]

    people = []
    stairs = []
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 1:
                people.append((i, j))
            elif grid[i][j] > 1:
                stairs.append((i, j, grid[i][j]))

    sel = [0] * len(people)

    ans = int(1e9)
    subset(0)
    print(f"#{tc + 1} {ans}")
