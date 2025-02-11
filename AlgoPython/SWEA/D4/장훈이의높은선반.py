T = int(input())
for tc in range(T):
    n, k = map(int, input().split())

    arr = list(map(int, input().split()))
    # 부분집합..
    ans = 200_000_001


    def subset(idx, sm):
        global ans
        if(sm>ans):
            return
        if (sm >= k):
            ans = min(ans, sm)
            return
        if (idx == n):
            return

        subset(idx + 1, sm + arr[idx])
        subset(idx + 1, sm)


    subset(0, 0)
    print(f"#{tc+1} {abs(ans - k)}")