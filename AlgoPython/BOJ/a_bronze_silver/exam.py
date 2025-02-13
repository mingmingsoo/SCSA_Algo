'''
bfs: 주사위로 갈 수 있는 숫자와 depth를 넣어서 방문하지 않은 곳 방문

[디버깅]
뱀/사다리로 1회 이동 후, 이동한 그곳에 또 뱀/사다리가 있을 수 있다.
1에서 시작하여 1번의 주사위로 갈 수 있는 곳 2~7
먼저 queue에 넣는 좌표를 바꿔줬다면 visited도 바꿔줬어야지.
'''

from collections import deque


def bfs():
    visited = [0] * 101 # 1~6은 방문
    visited[1] = 1
    q = deque([(1,0)])


    while q:
        idx, depth = q.popleft()
        # 종료 조건
        if idx == 100:
            return depth

        # 뱀 또는 사다리가 있고, 방문하지 않은 점이라면!
        while obs[idx] > 0:
            idx = obs[idx]

        for i in range(1, 7):
            nxt = idx+i
            if nxt <= 100 and not visited[nxt]:
                visited[nxt] = 1
                q.append((nxt, depth+1))


N, M = map(int, input().split())
obs = [0]*101       # 뱀 또는 사다리가 있는 곳 관리
for _ in range(N+M):
    s, e = map(int, input().split())
    obs[s] = e

# bfs 탐색하면서 1~6 이동하는 경우 check
# 방문한 곳은 재방문 x
ans = bfs()
print(ans)

# 3 1
# 2 50
# 50 80
# 80 99
# 99 80
# 정답 10
# 최단 루트 : [1, 2, 52, 58, 64, 70, 76, 82, 88, 94, 100]


#
# 3 7
# 2 90
# 89 99
# 15 91
# 92 50
# 93 8
# 94 7
# 95 6
# 96 5
# 97 4
# 98 3