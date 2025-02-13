'''
[문제]
    계단은 한번에 1, 2씩 오를 수 있음
    연속된 3개의 계단은 밟으면 안됨
    마지막은 반드시 밟아야함
[구상]
    내가 꼭대기면 나는 어디서부터 왔는가?
    1. -1,-3 에서 왔다.
    2. -2에서 왔다.
'''

n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))
if(n == 1): # 계단이 하나면 그냥 출력하고 나가기
    print(*arr)
else:
    arr.insert(0,0) # 바닥 넣어주기

    dp = [0]*(n+1) # dp
    dp[1] = arr[1]
    dp[2] = arr[1]+arr[2] # 초기값 설정

    # print(arr)
    for i in range(3,n+1):
        dp[i] = max(dp[i-2]+arr[i], arr[i-1]+dp[i-3]+arr[i])
    # print(dp)
    print(dp[n])