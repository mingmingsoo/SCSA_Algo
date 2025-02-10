n, m = map(int,input().split())

arr = list(map(int, input().split()))
arr.sort()
sel = [0]*m

def btk(idx,sidx):
    if(sidx ==m):
        print(*sel)
        return
    if(idx ==n):
        return

    sel[sidx] = arr[idx]
    btk(idx,sidx+1) # 나는 중복되도 됩니다.
    btk(idx+1,sidx) # 그래도 넘겨줄때는 전보단 커야해요

btk(0,0)