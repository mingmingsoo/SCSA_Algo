n = int(input())
arr = list(map(int, input().split()))
ans = [-1]* n
stk = [arr[-1]]
for i in range(n-2,-1,-1):

    while stk and arr[i]>=stk[-1]: # 부호때문에 한번  틀렷음
        stk.pop()
    if stk and arr[i]<stk[-1]:
        ans[i] = stk[-1]
    stk.append(arr[i])
for char in ans:
    print(char, end = " ") # 출력때문에 한번 틀렸음.