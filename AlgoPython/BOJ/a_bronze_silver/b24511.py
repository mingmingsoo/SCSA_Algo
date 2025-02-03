'''



- 문제설명
1. 자료구조에는 1개의 원소가 들어있음
2. 작동원리
    - x0 입력받음
    - 1번 자료구조에 삽입 후 1번 자료구조에서 pop -> x1
    - x1을 2번 자료구조에 삽입 -> 2번 자료구조에서 pop ->x2
    ...
    - x(N-1)을 N번 자료구조에 삽입 -> N번 자료구조에서 pop ->X(N)

길이 M의 수열 C를 가져와서.... 순서대로..

'''

n = int(input())
qs = list(map(int, input().split())) # stk 처럼 쓸것
arr = list(map(int, input().split()))
m = int(input())
qstack = list(map(int, input().split())) # stk 처럼 쓸것

for i in range(m):
