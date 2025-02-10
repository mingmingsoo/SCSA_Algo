n,m = map(int, input().split())
arr = list(range(1,n+1))
sel = [0]*m

visited = [False]*n
def combi(idx,sidx):
    if(sidx == m):
        print(*sel)
        return
    if(idx ==n):
        return

    sel[sidx] = arr[idx]
    combi(idx+1,sidx+1)
    combi(idx+1,sidx)

combi(0,0)