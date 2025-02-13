import math
''''
제출횟수 14회

100 -> 1 이면
100 -> -100 -1 -> -100 -> 100 -1 -> 99 -> -99 -1 -> 99 -1 -> 98 ... 이렇게 모든 숫자가 될 수 있음
'''

T = int(input())
for tc in range(T):
    before, after = map(int, input().split())
    print("yes")