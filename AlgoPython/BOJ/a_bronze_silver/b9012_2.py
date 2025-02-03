n = int(input())


def stack():
    for nn in range(n):
        ans = "YES"
        stk = []
        line = list(input())
        for char in line:
            if (char == "("):
                stk.append(char)
            else:
                if (stk):
                    stk.pop()
                else:
                    ans = "NO"
                    break
        if (stk):
            ans = "NO"
        print(ans)


stack()
