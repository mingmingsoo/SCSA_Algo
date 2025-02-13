'''
[문제]
    가로,세로,대각선으로 갈 수 있을 때 획득할 수 있는 사탕의 최댓값
[구상]
0번째 가로, 0번째 세로는 누적해서 더하고 시작한다.
행과 열을 이동하면서 최댓값을 갱신한다.
'''

n,m = map(int,input().split())
grid = [list(map(int, input().split())) for i in range(n)]
dp = [[0]*m for i in range(n)]
dp[0][0] = grid[0][0]
for j in range(1,m):
    dp[0][j] = dp[0][j-1]+grid[0][j]
for i in range(1,n):
    dp[i][0] = dp[i-1][0]+grid[i][0]

for i in range(1,n):
    for j in range(1,m):
        dp[i][j] = max(dp[i-1][j]+grid[i][j], dp[i][j-1]+grid[i][j])
print(dp[n-1][m-1])