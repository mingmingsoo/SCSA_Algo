'''
중복되지 않는 경우의 수를 구해야한다
-> 순열을 생각...
'''
T = int(input())
for tc in range(T):
    n, m, SUM = map(int, input().split())

    arr = list(map(int, input().split()))
    sel = [0] * m

    visited = [False] * (n)
    ans = 0


    def btk(sidx, idx):
        global ans
        if (sidx == m):
            if (sum(sel) == SUM):
                # print(sel)
                ans += 1
            return
        if (idx == n):
            return

        sel[sidx] = arr[idx] # 담아!
        btk(sidx + 1, idx + 1) # 둘 다 넘어가야지. 중복되면 안돼!
        btk(sidx, idx + 1) # 전의 값들도 살펴봐줘야하는데 중복되면 안되니까 idx+1

    btk(0, 0)
    print(f"#{tc+1} {ans}")