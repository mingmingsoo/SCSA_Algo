'''
[규칙찾기]
    1 3 5 11 21 43 ...
    i는 i-2 번째에서 어떤 숫자를 더한 값.
    어떤 숫자는 4부터 시작해서 넘어갈때마다 *2가 된다.
[출력]
    출력은 %10_007
'''
import sys
input = sys.stdin.readline
n = int(input())
if(n==1):
    print(1)
else:
    dp = [0]*n
    dp[0] =1
    dp[1] =3
    num = 4
    for i in range(2,n):
        dp[i] = (dp[i-2]+num)%10_007
        num*=2
    print(dp[n-1]%10_007) #나머지를 안해서 틀렸다... 바보