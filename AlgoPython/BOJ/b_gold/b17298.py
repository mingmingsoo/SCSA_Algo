# n = int(input())
# arr = list(map(int, input().split()))
# stack = [0]
# ans = [-1] * n
#
# for i in range(1,n):
#
#     while stack and arr[stack[-1]]< arr[i]:
#         ans[stack.pop()] = arr[i]
#     stack.append(i)
#
# print(*ans)

n = int(input())
arr = list(map(int, input().split()))
stack = [arr[-1]]
ans = [-1]*n
for i in range(n-2,-1,-1):
    # stack에 있는 값이 나보다 작으면 다 빼낸다.
    while( stack and arr[i]>=stack[-1]):
        stack.pop()
    # 나보다 큰놈이 있으면(== 스택이 남아있으면) 그게 오큰수다.
    # print(stack)
    if(stack):
        ans[i] = stack[-1]
    # 내 왼쪽 값들은 나보다 작을 수 있어서 stack에 넣어준다.
    stack.append(arr[i])
print(*ans)