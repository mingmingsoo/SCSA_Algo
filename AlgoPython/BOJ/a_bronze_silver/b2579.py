n = int(input())

arr = [int(input()) for i in range(n)]
isOne = False
if(n==1):
    isOne = True
    print(arr[0])
if(isOne==False):
    arr.insert(0,0)
    dp = [0]*(n+1)
    dp[1]= arr[1]
    dp[2] = arr[1]+arr[2]
    for i in range(3,n+1):
        dp[i] = max(arr[i]+arr[i-1]+dp[i-3],dp[i-2]+arr[i])
    print(dp[n])