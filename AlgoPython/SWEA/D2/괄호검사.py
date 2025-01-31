T = int(input())
for tc in range(T):
    string = input()
    stack = []
    isBalance = True
    for i in range(len(string)):
        if (string[i] == "{" or string[i] == "("):
            stack.append(string[i])
        elif (string[i] == "}"):
            if (not stack):
                isBalance = False
                break
            else:
                if (stack[len(stack) - 1] == "{"):
                    stack.pop()
                else:
                    isBalance = False
                    break
        elif (string[i] == ")"):
            if (not stack):
                isBalance = False
                break
            else:
                if (stack[len(stack) - 1] == "("):
                    stack.pop()
                else:
                    isBalance = False
                    break
    print(f"#{tc+1}", end = " ")
    if (not isBalance or stack):
        print(0)
    else:
        print(1)