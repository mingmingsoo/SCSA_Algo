'''
애초에 visited 가 필요가 없음.
*2 는 모조건 홀수고
1을 더하는 것은 무조건 전의 값들보다 커지기 때문
중복될 수 가 없음.

'''
from collections import deque
start, end = map(int, input().split())

q = deque([(start,1)])
ans = -1
while q:
    cur, cnt = q.popleft()
    if(cur==end):
        ans = cnt
        break
    cur_add_1 = int(str(cur)+"1")

    if(cur*2<=end):
        q.append((cur*2, cnt+1))
    if(cur_add_1<=end):
        q.append((cur_add_1,cnt+1))

print(ans)



