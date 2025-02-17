'''
초밥을 줄 때 무조건 1번손님부터 줘서(작은번호의 손님부터)
힙 큐를 사용해서 초밥을 관리한다
'''

import heapq
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
size = 200_001 # 최대 초밥 갯수
chobab = {}
for i in range(size):
    chobab[i]  = [] # 초밥을 힙큐로 관리할 것임

for i in range(N):
    tmp = list(map(int,input().split()))
    for j in range(1,len(tmp)):
        heapq.heappush(chobab[tmp[j]], i) # 초밥 번호마다 손님 번호를 기록해줌

order= list(map(int, input().split()))
count = [0]*N
for num in order:
    if(chobab[num]): # 초밥시키신 빠른 손님
        count[heapq.heappop(chobab[num])]+=1 # 나오세요
print(*count)