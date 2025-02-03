'''
맵 정보를 받고
내가 1이고 옆에 0이 하나라도 있으면 둘레 카운팅.
모서리점들 카운팅 ( 여기서 모서리는 주변에 0이 두개인 애들)
'''
T = int(input())
size = 101  # 디버깅 위해서 25로 줄여서 한 번 틀림
grid = [[0] * size for i in range(size)]
ans = 0
for t in range(T):
    r, c = map(int, input().split())
    for i in range(r, r + 10):
        for j in range(c, c + 10):
            grid[i][j] = 1

row = [-1, 1, 0, 0]
col = [0, 0, 1, -1]

for i in range(size):
    for j in range(size):
        if (grid[i][j] == 1):
            for k in range(4):
                nr = i + row[k]
                nc = j + col[k]
                cnt = 0
                if (0 <= nr < size and 0 <= nc < size and grid[nr][nc] == 0):
                    cnt += 1
                if (cnt == 1):
                    ans += 1
                if (cnt == 2):
                    ans += 1
print(ans)
