T = int(input())
for tc in range(T):
    '''
    순회해라
    '''

    V = int(input())
    ans = [0] * (V + 1)

    cnt = 1


    def ord(n):
        global cnt
        if (n > V):
            return
        ord(2 * n)
        ans[n] = cnt
        cnt += 1
        ord(2 * n + 1)


    ord(1)
    print(f"#{tc+1} {ans[1]} {ans[V // 2]}")