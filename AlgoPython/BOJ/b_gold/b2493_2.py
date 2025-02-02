n = int(input())
arr = list(map(int, input().split()))

stk = [0]
ans = [0]*n
for i in range(1, n):
    while stk and arr[i]>arr[stk[-1]]:
        stk.pop()
    if(stk):
        ans[i] = stk[-1]+1
    stk.append(i)
print(*ans)
