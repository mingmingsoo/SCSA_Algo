'''
내가 못풀어서 답 보고 풀었음

[해결방안]
    1. dp는 1로 채운다. 왜냐하면 나부터 시작할 수 있으니까!
    2. 나보다 앞에 있는 애들 중에 내가 걔보다 크면
    -> 나는 걔 더하기 1과 전에 왔던 나중에 큰 값이된다!
'''

n = int(input())
arr = list(map(int,input().split()))
dp = [1]*n

for i in range(1,n):
    for j in range(i):
        if(arr[i]>arr[j]):
            dp[i] = max(dp[i], dp[j]+1)

# print(dp)
print(max(dp))
