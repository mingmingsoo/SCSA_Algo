n,m = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort()
visited= [False]*(n)
sel = [0]*m
def btk(idx,sidx):
    if(sidx == m):
        print(*sel)
        return

    if(idx == n):
        return

    sel[sidx] = arr[idx]
    btk(idx+1,sidx+1)
    btk(idx+1,sidx)

btk(0,0)
