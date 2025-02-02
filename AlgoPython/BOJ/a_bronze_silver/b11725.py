'''
먼소리야ㅠ
각 노드의 부모를 구하래
문제 이해는 못했는데
감으로 품...

1. 양방향이면 안됨
2. 1은 부모를 가질 수 없어서 start가 1 이 들어오면 swap해줌.
3. 하나의 부모만 가지기에, 이미 부모였던적이 있는 애들이 start로 들어오면 swap 해줌


-> 아니고 양방향으로 받고 dfs로 풀리면 풀림..
-> 아님 메모리초과남 비상 비상
-> ans를 안만들고 해보겠습니다...
-> bfs로 풀어보겠습니다..........

'''
import sys
from collections import deque


n = int(sys.stdin.readline()) # 노드 갯수.
arr = [[] for i in range(n+1)]
for i in range(n-1):
    start, end =map(int, sys.stdin.readline().split())
    arr[start].append(end)
    arr[end].append(start)

visited = [0]*(n+1)
# def dfs(idx):
#     for i in (arr[idx]):
#         if(visited[i]==0):
#             visited[i] = idx
#             dfs(i)
# dfs(1) # 대왕 부모인 1부터 탐색.

def bfs(start):
    q = deque([start])
    while q:
        node = q.popleft()
        for i in arr[node]:
            if (visited[i]==0):
                visited[i] = node
                q.append(i)


bfs(1)

for i in range(2,n+1):
    print(visited[i])