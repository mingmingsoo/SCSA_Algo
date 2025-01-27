arr = [[0]*101 for i in range(101)]

T = int(input())
for t in range(T):
    r,c = map(int, input().split())
    for i in range(r, r+10):
        for j in range(c, c+10):
            arr[i][j] = 1;

ans = 0
for i in range(101):
    ans += arr[i].count(1)
print(ans)