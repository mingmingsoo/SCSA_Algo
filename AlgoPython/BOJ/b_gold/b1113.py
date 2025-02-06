'''

사방을 검사해서 나보다 큰 애들 중 제일 작은 만큼 채울 수 잇음
-> 반례가 있음

최소점이 아닌 점에서 bfs로 덩어리가 된다면 그 안에 애들은 물 찰 수 있음
그 덩어리 안에서 덩어리보다 낮은 애들은 수영장이 될 수 잇음

맵이 작아서 괜찮을 듯

아님.

내가 갇혀있네? 를 어떻게 알지?

모든 점에서 bfs 돌리는데
나보다 같거나 작은애들만 q에 넣어주는데 그게 범위를 벗어나면 물이 흘러가서 웅덩이 가 안됨
나보다 큰 애들을 만나면 q에 넣지 않고 최대 높이만 갱신해줌 (가장 작은 값으로)
이제 수영장 되는애들을
visited 처리하고 연산해서 두번다신 못가게함.

'''
import copy
from collections import deque

n,m = map(int, input().split())

grid = [list(map(int, input())) for i in range(n)]


row = [-1,1,0,0]
col = [0,0,1,-1]
ans = 0
for i in range(n):
    for j in range(m):
        minH = 10
        bfs(i,j)
