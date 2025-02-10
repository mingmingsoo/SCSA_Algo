'''
풀었던 문제라 visited 처리하는 법이 기억이 났었다.

그냥 수빈이랑 다른 이유는 경우의 수를 다 알아내야 하기 때문에
발견했다고 return 해버리면 안되고 다 탐색을 해야한다.

저번 코드랑 비슷한데 시간초가 나는 이유는 ans를 최솟값으로 갱신하는 로직 때문인 것 같다.

5 17
5 4 8 16 17
5 10 9 18 17

이렇게 두가지 경우의 수가 나오는데
17을 방문처리 해버리면 두번째 경우의수가 계산이 안된다.
그래서 각 숫자들마다 어디서 온 경로인지도 기입해줘야한다.

16-> 17로 가고싶을 때
if(not visited[17][1]) :
16 -> 17 로 갈때 visited[16][1]= True로 해준다
그러면 18 -> 17로도 갈 수 있다.

'''
from collections import deque

s, e= map(int, input().split())
size = 1000001
ans = size
total = 0

def bfs(start):
    global total
    global ans
    q = deque([(start,0)])
    visited = [[False]*3 for i in range(size)]
    visited[start][0], visited[start][1] , visited[start][2] = True, True, True
    # start에서 다른 숫자들로 다 보낼거기 때문에 방문처리 해놓는다.

    while q:
        cur, cnt = q.popleft()
        if(ans<cnt): # 같은 횟수가 아니라면 갈 필요도 없음 넘어갓!
            # print(cur,cnt,ans)
            continue
        if(cur==e):
            if(ans>cnt): # 맨 첫빠로 온애가 ans를 갱신해줌!
                ans = cnt
            # ans = min(ans,cnt)
            total+=1 # 만약 위에서 continue 처리가 안됐으면 (즉 온 횟수가 같으면 경우의 수 추가!)

        if(0<=cur-1 and not visited[cur-1][0]): # 다음 갈 숫자가 나한테서 온적 없다면
            visited[cur][0] = True # 나 간다! 거기로!
            q.append((cur-1,cnt+1))
        if(cur+1<size and not visited[cur+1][1]):
            visited[cur][1] = True
            q.append((cur+1,cnt+1))
        if(cur*2<size and not visited[cur*2][2]):
            visited[cur][2] = True
            q.append((cur*2,cnt+1))

bfs(s)

print(ans)
print(total)