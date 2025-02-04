'''
9
3 2 3 5 1 7 6 4 1
'''

n = int(input())
arr = list(map(int, input().split()))
dp = [0]* (n)
arr.append(1000000) # 그냥 큰값
dp.append(1000000)
print(arr)
for i in range(n-1,-1,-1):
    if(arr[i]< arr[i+1]):
        dp[i] = arr[i]+dp[i+1]
        if(dp[i]>1000000):
            dp[i] -= 1000000
    else:
        dp[i] = max(arr[i],dp[i+1])
dp.pop()
print(dp)
print(max(dp))