'''
[문제설명]
    열이 중복되지 않게 선택해서 행의 최대합을 구해라.
[구상]
    dp는 i-1의 j-1, j+1 에서 날 더한 값이 작은걸 선택한다.
    즉 대각선 양옆위를 비교하는 것!
'''
n = int(input())

grid = [list(map(int, input().split())) for i in range(n)]

dp = [[0]*3 for i in range(n)]
dp[0] = grid[0][:] # 첫줄은 일딴 원래값.

for i in range(1,n):
    for j in range(3): # 파이썬이여서 음수 처리를 안해줘도 된다 다른 언어였으면 (j+3-1)%3 이 필요하다.
        dp[i][j]  = min(dp[i-1][j-1]+grid[i][j], dp[i-1][(j+1)%3]+grid[i][j])

print(min(dp[n-1]))