n = int(input())
arr = list(map(int, input().split()))

ans = [0]*n
stack = [n-1]
for i in range(n-2,-1,-1):

    while stack and arr[i]> arr[stack[-1]]:
        ans[stack.pop()] = i+1
    stack.append(i)
print(*ans)