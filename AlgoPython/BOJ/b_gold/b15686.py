'''
치킨 거리는 집과 가장 가까운 치킨집 사이의 거리
도시의 치킨 거리는 모든 집의 치킨 거리의 합
맨해튼 거리 사용
0은 빈 칸, 1은 집, 2는 치킨집
가장 수익을 많이 낼 수 있는  치킨집의 개수는 최대 M개
M개 선택시 최소 도시 치킨 거리

순열로.. 이 아니라 조합임.ㅋ

백트래킹: ans 보다 커지면 return
'''

n, m = map(int, input().split())  # 맵 크기, 선택할 갯수
grid = [[0] * n for i in range(n)]
num_chicken = 1
chicken = {}
house = []
for i in range(n):
    grid[i] = list(map(int, input().split()))
    for j in range(n):
        if (grid[i][j] == 2):
            chicken[num_chicken] = (i, j)
            num_chicken += 1
        elif (grid[i][j] == 1):
            house.append((i, j))

chi_n = len(chicken)
arr = list(range(1, chi_n + 1))
sel = [0] * m
ans = float('inf')
visited = [False] * chi_n


def cal(sel):
    total = 0
    for hr, hc in house:
        ele = float('inf')
        for num in sel:
            r, c = chicken[num]
            ele = min(abs(hr - r) + abs(hc - c), ele)
        total += ele
        if(total>=ans):
            return total
    return total


def combi(sidx, idx):
    global ans
    if (sidx == m):
        # 치킨집 선택은 끝났음. 거리 계산 필요
        # bfs 로 집에서 2나오면 return 이 방법도 있는데
        # 그냥 완탐해야쥥
        sum = cal(sel)
        if (ans > sum):
            ans = sum

        return
    if (idx == chi_n):
        return

    sel[sidx] = arr[idx]
    combi(sidx + 1, idx + 1)
    combi(sidx, idx + 1)


combi(0, 0)
print(ans)
