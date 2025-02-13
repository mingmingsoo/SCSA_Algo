'''
[문제 설명]
    n번째 피보나치 수를 구하여라
[구상]
    dp를 사용해서 전에 계산한 값들을 더해준다.
'''

n = int(input())
dp = [0]*(n+1)
dp[0] = 0
dp[1] = 1
for i in range(2,n+1):
    dp[i] = dp[i-1] + dp[i-2]
print(dp[n])

