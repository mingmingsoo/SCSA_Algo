T = int(input())
for tc in range(T):
    string = input()

    stack = []
    for i in range(len(string) - 1, -1, -1):
        if (not stack):
            stack.append(string[i])
        elif (stack[len(stack) - 1] != string[i]):
            stack.append(string[i])
        else:
            stack.pop()
    print(f"#{tc+1} {len(stack)}")