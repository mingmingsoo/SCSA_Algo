T = 10
for tc in range(T):
    n, num = input().split()
    num = list(num)
    n = int(n)
    stack = []
    for i in range(0, n):
        if (not stack):
            stack.append(num[i])
        else:
            if (num[i] == stack[-1]):
                stack.pop()
            else:
                stack.append(num[i])

    print(f"#{tc + 1}", end=" ")
    for ele in stack:
        print(ele, end="")
    print()