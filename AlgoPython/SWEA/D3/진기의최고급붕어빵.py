T = int(input())

for tc in range(T):
    n, m, k = map(int, input().split())

    come = list(map(int, input().split()))
    maxNum = max(come)
    size = 12000
    timeline = [0] * size
    for i in range(n):
        timeline[come[i]] = 1
    print(f"#{tc+1} ", end = "")

    def bread():
        stk = []
        for i in range(0, size):
            if (i!=0 and i % m == 0):
                stk.append(k)
            if (timeline[i] == 1):
                if (not stk):
                    print("Impossible")
                    return
                else:
                    if (stk[-1] > 0):
                        stk[-1] -= 1
                        if (stk[-1] == 0):
                            stk.pop()
        print("Possible")


    bread()