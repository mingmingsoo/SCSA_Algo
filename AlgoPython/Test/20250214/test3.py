'''
문제설명
    1~N까지 직선구간에서 M초동안 이동한다
    초기크기는 1이고 시작위치는 0
    1. 밀기: 현재위치+1칸으로 이동 -> 현재위치+1칸 크기만큼 늘ㄹ어남
    2. 차기: 현재위치+2칸으로 이동 -> 현재크기는 절반으로 줄어들고, +2칸 크기만큼 늘어남

    끝지점에 도달한 경우 시간이 남아도 끝남.
    가장 큰 크기는??

구상
    bfs로 푸는 것 같은데... 최대경로라서.... return해주면 안될 것 같다.
    visited는 필요 없을 듯. 뒤로가지는 않으니까
    최대힙으로 풀 수 있을까?
'''
from collections import deque
def bfs(start, s): # 시작점0과 초기사이즈 1
    global ans
    q = deque([(start, s, 0)])  # 위치, 크기, 시간
    while q:
        qsize = len(q)
        for i in range(qsize):
            cur, size, time = q.popleft()
            ans = max(ans, size)

            if (time >= limit): # 시간이 끝났으면 q에 그만담아!!!!!!!!
                continue
            if (cur + 1 <= n):
                q.append((cur + 1, size + arr[cur + 1], time + 1))
            if (cur + 2 <= n):
                q.append((cur + 2, size // 2 + arr[cur + 2], time + 1))

T = int(input())
for tc in range(T):

    n, limit = map(int, input().split())
    arr = list(map(int, input().split()))
    arr.insert(0, 0)
    ans = 0  # 초기값.....
    d = [0]*(n+1)
    d[0] = 1
    bfs(0, 1)
    print(f"#{tc+1} {ans}")