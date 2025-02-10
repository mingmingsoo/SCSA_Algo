n,m = map(int,input().split())

arr = list(map(int, input().split(",")))

ans = arr[:]
for i in range(m):
    ans = []
    for j in range(len(arr)-1):
        ans.append(arr[j+1]-arr[j])
    arr = ans[:]
print(",".join(map(str, ans)))