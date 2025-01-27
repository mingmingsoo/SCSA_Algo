# # dfs로 풀어야할 것 같은디용 시간초과 안될라낭
#
# n = int(input())
#
# time = [list(map(int, input().split()) )for i in range(n)]
#
# ans = 0
#
#
# def dfs(index, start, end,cnt):
#     global ans
#     if(index >= n-1):
#         ans = max(cnt,ans)
#         return
#     for i in range(index+1, n):
#         if(time[i][0]>=end):
#             dfs(i, time[i][0], time[i][1], cnt+1)
#
#
#
# for i in range(11):
#     dfs(i,time[i][0], time[i][1],1)
# print(ans)


# dp로 풀기
n = int(input())

time = [list(map(int, input().split()) )for i in range(n)]

dp = [1]*(n)

for i in range(n):
    t = time[i]
    closeJ = i
    closemax = 0
    for j in range(0,n):
        if(i==j):
            continue
        beforeT = time[j]
        if(t[0]>=beforeT[1]):
            if(closemax < dp[j]):
                closemax = dp[j]
                closeJ = j
    if(closeJ != i):
        dp[i] = dp[closeJ] +1
print(max(dp))