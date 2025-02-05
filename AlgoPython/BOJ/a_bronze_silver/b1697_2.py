'''
풀었던 문제
가장 빠른 시간 출력 이므로
bfs로 찾자마자 return
'''
from collections import deque
max_size = 100001 # 앗 이거때문에 1번 틇림
start, end = map(int, input().split())

def bfs(start, end):

    q = deque([(start, 0)])
    visited = [False] * max_size

    while q:
        cur, dist = q.popleft()
        if (cur == end):
            return dist

        if (cur - 1 >= 0 and not visited[cur - 1]):
            visited[cur - 1] = True
            q.append((cur - 1, dist+1))

            # 범위 때문에 1번 틀림 ㅠ <=max_size 였음
        if (cur + 1 < max_size and not visited[cur + 1]):
            visited[cur + 1] = True
            q.append((cur + 1, dist+1))
        if (cur * 2 < max_size and not visited[cur * 2]):
            visited[cur * 2] = True
            q.append((cur * 2, dist+1))


ans = bfs(start, end)
print(ans)
