'''
[문제설명]
    연속된(1개이상) 수의 합 중 가장 큰 값은?

[구상]
    dp[0] = arr[0]으로 하고 => 초기값
    dp = max(dp[i-1], dp[i-1]+arr[i] 로 갱신하면 될 것 같다.
    여기까지 하고........ 해맸다.............

    전까지 더한값 vs 지금의 나
'''

n = int(input())
arr = list(map(int,input().split()))

dp = [0]*n
dp[0]= arr[0]
for i in range(1,n):
    dp[i] = max(dp[i-1]+arr[i],arr[i])
print(max(dp))