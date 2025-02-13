'''
[문제 설명]
    X를 연산해서 1을 만드는데 최소 연산 횟수를 구하여라.
[구상]
    bfs로도 풀어보고, dp로도 풀어보기
    1부터 시작해서 ex) 10으로 만드는 횟수를 계산하기!
'''
from collections import deque

n = int(input())

dp = [0]*(n+1)
dp[1] = 0
for i in range(2,n+1):
    dp[i] = dp[i-1]+1 # 1씩 더하면 무조건 만들 수는 있음.
    if(i%3==0): # 그런데 3으로 나눌 수 있으면
        dp[i] = min(dp[i//3]+1, dp[i]) # 나눈 3에서 +1 해서 비교하기
    if(i % 2 == 0):
        dp[i] = min(dp[i//2] + 1, dp[i])
print(dp[n])