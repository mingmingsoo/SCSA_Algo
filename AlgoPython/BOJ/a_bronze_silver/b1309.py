'''
다시 규칙을 찾겠습니다
i-1 번째 *2 + i-1번째
'''
n = int(input())
if(n==1):
    print(3)
else:
    dp=[0]*n
    dp[0] = 3
    dp[1] = 7

    for i in range(2,n):
        dp[i] = (dp[i-1]*2 + dp[i-2])%9901
    print(dp[n-1]%9901)