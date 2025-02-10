n, m = map(int, input().split())

arr = list(map(int, input().split()))
arr.sort()
sel = [0]*m
visited = [False]*(n)
ans = set()
def btk(sidx,idx):
    if(sidx ==m):
        ans.add(tuple(sorted(sel)))
        return
    if(idx ==n):
        return

    for i in range(idx,n):
        if(not visited[i]):
            visited[i]= True
            sel[sidx] = arr[i]
            btk(sidx+1,idx+1)
            visited[i]= False
btk(0,0)
ans = sorted(list(set(ans)))
for row in ans:
    print(*row)
