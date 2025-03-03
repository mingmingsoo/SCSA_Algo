'''
문제설명
    0에서 -1 누르면 변화 없음
    채널은 무한대
    N으로 이동하기 위해 최소?
    bfs?
    어렵당
    숫자로도 이동이 가능함
    end에서 from 에 따라 연산.


재구상
    두가지 연산을 비교해야함
    1. 100에서 갈 때
    2. 버튼 누를 때

    1은 ans =  abs(end-100) 으로 구하고
    2는 end에서 시작해서 +1, -1 해주면서 가능한 숫자조합을 찾아야함


'''
from collections import deque

possible = [True] * 10
end = int(input())
e = int(input())
if e > 0:
    tmp = list(map(int, input().split()))
    for i in range(e): # 가능한 숫자조합 만들기
        possible[tmp[i]] = False
ans = abs(end - 100)


def bfs():
    global ans
    visited = [False] * (999_999 + 1)
    q = deque([(end, 0)])
    visited[end] = True
    while q:
        cur, cnt = q.popleft()
        num = str(cur)
        for ele in num:
            if not possible[int(ele)]: # 불가능한 숫자조합이면 다음 탐색
                break
        else: # 만약 가능하다면 최솟값 갱신
            ans = min(ans, cnt + len(str(num)))
            return
        if cur - 1 >= 0 and not visited[cur - 1]:
            q.append((cur - 1, cnt + 1))
            visited[cur - 1] = True
        if cur + 1 < 999_999 + 1 and not visited[cur + 1]:
            q.append((cur + 1, cnt + 1))
            visited[cur + 1] = True


bfs()
print(ans)
