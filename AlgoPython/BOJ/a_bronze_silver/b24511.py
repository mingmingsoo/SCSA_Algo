'''
문제시작: 07:55
문제종료 08:27
문제 중단 09:14 아직도 시간초과를 잡지 못했음. 구글링하겠음 ㅠㅠ 졌다.
문제 종료 09:30

- 문제설명
1. 자료구조에는 1개의 원소가 들어있음
2. 작동원리
    - x0 입력받음
    - 1번 자료구조에 삽입 후 1번 자료구조에서 pop -> x1
    - x1을 2번 자료구조에 삽입 -> 2번 자료구조에서 pop ->x2
    ...
    - x(N-1)을 N번 자료구조에 삽입 -> N번 자료구조에서 pop ->X(N)

자료구조 유형대로 pop을 어떻게 하는지 정해주면 된다.


---- 구글링 보고 나서 -----
아이디어: q인 애들만 list 만들어서 쓰는 것이다.......
stack인 애들은 어차피 알아서 들어온 원소가 나가므로 신경쓰지 않아도 된다.!!! 이건 캐치했는데 ㅠㅠ
Q인 애들은 앞, 뒤 만 빼주면 됨 ㅠㅠ

'''

import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
qs = list(map(int, input().split())) # 자료구조의 정보 0이면 q 1이면 stack

tmp = list(map(int, input().split()))
m = int(input()) # 자료구조에 넣어줄 리스트의 크기
arr = list(map(int, input().split())) # 그 리스트 요소들

QStack = deque()

for i in range(n):
    if(qs[i]==0):
        QStack.append((tmp[i]))

if(QStack):
    for i in range(m):
        print(QStack.pop(), end = " ")
        QStack.insert(0,arr[i])
else:
    print(*arr)

