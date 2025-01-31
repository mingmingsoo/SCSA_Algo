n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))
stack = []
for i in range(n-1,-1,-1):
    h = arr[i]
    if(not stack):
        stack.append(h)
    else:
        if(stack[-1]<h):
            stack.append(h)
print(len(stack))