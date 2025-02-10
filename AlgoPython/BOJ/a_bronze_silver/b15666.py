n, m = map(int, input().split())

arr = sorted(list(set(list(map(int, input().split())))))
n = len(arr)
# 중복은 없애고,,, 중복조합

sel = [0]*m

def btk(idx,sidx):
    if(sidx == m):
        print(*sel)
        return
    if(idx ==n):
        return

    sel[sidx] = arr[idx]
    btk(idx,sidx+1)
    btk(idx+1,sidx)

btk(0,0)