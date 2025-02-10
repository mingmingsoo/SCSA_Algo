n, m = map(int, input().split())

arr = list(range(1,n+1))

visited = [False]*n
sel = [0]*m
def perm(idx,sidx):
    if(sidx == m):
        print(*sel)
        return

    if(idx ==n):
        return

    for i in range(n):
        if(not visited[i]):
            visited[i] = True
            sel[sidx] = arr[i]
            perm(idx+1,sidx+1)
            visited[i] = False

perm(0,0)