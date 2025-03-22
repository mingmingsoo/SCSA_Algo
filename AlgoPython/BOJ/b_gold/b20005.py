'''
a,b,c가 보스향해서 갔으면 bfs 종료
그리고 때려 졸라때림

혹시a,b,z이렇게 플레이어주는건 아니지?;;;

d아 ㅠboss에서만 bfs 돌리기
'''
from collections import deque

n, m, player_num = map(int, input().split())
grid = [list(input()) for i in range(n)]
boss_r, boss_c = -1, -1
player_power = {}
for i in range(n):
    for j in range(m):
        if grid[i][j] == "B":
            boss_r, boss_c = i, j
            grid[i][j] = "."

player_eta = {}
for p in range(player_num):
    player, hp = input().split()
    num = ord(player) - 97
    player_power[num] = int(hp)
    player_eta[num] = -1

boss_hp = int(input())
# print(player_eta)

# 몇시에 도착하는지 기록을 해놓자.
row = [-1, 1, 0, 0]
col = [0, 0, 1, -1]


def bfs():
    q = deque([(boss_r, boss_c, 0)])
    visited = [[False] * m for i in range(n)]
    visited[boss_r][boss_c] = True
    while q:
        r, c, time = q.popleft()
        if "a" <= grid[r][c] <= "z":
            player_eta[ord(grid[r][c]) - 97] = time

        for k in range(4):
            nr = r + row[k]
            nc = c + col[k]

            if not (0 <= nr < n and 0 <= nc < m) or visited[nr][nc] or grid[nr][nc] == "X":
                continue
            visited[nr][nc] = True
            q.append((nr, nc, time + 1))


bfs()

attack = [False] * player_num

while boss_hp >= 0:
    ele_hp = 0
    for player, eta in player_eta.items():
        if eta == 0:
            ele_hp += player_power[player]
            attack[player] = True

    for player, eta in player_eta.items():
        if eta > 0:
            player_eta[player] -= 1
    boss_hp -= ele_hp

# print(attack)
print(sum(attack))
