n, k = map(int, input().split())

arr = []
for i in range(n):
    arr.append(int(input()))
arr.sort(reverse=True)
ans = 0
for num in arr:
    cnt = 0
    if(num<=k):
        cnt += (k//num)
        k -= (cnt * num)

    ans += cnt

    if(k <=0):
        break

print(ans)
