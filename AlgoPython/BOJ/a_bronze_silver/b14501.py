n = int(input())

weight = [0]*(n+1)
cost = [0]*(n+1)
for i in range(1, n+1):
    w,c  = map(int, input().split())
    weight[i] = w
    cost[i] = c
dp = [0]* (n+2)
for i in range(1,n+1): # 1~n까지 탐색
    dp[i] = max(dp[i], dp[i-1])
    if(i+weight[i]<=n+1):
        dp[i+weight[i]] = max(dp[i+weight[i]], cost[i]+dp[i])

print(max(dp))
