T = int(input())
for tc in range(T):
    n = int(input())
    if(1<=n<=3):
        print(1)
    elif(4<=n<=5):
        print(2)
    else:
        dp = [0] * (n)
        dp[0] = 1
        dp[1] = 1
        dp[2] = 1
        dp[3] = 2
        dp[4] = 2


        for i in range(5, n):
            dp[i] = dp[i - 1] + dp[i - 5]
        print(dp[-1])
