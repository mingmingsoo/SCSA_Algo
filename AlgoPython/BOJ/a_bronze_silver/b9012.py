T = int(input())
for t in range(T):
    ans = True
    arr = list(input())
    stack = []
    for s in arr:
        if (s == "("):
            stack.append(s)
        if (s == ")"):
            if(len(stack) ==0):
                ans = False
                break
            if (len(stack) != 0 and stack[len(stack) - 1] == '('):
                stack.pop()
    if(len(stack)==0 and ans == True):
        print("YES")
    else:
        print("NO")
