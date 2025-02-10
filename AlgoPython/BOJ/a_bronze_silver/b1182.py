'''
부분집합..
'''

n, target = map(int, input().split())
arr = list(map(int, input().split()))

sel = [0]*n
empty = [0]*n
ans = 0

def subset(idx):
    global ans
    if(idx ==n):
        if sel == empty:
            return
        ele_sum = 0
        for i in range(n):
            if(sel[i]==1):
                ele_sum+=arr[i]
        if(ele_sum==target):
            ans+=1
        return

    sel[idx] = 1
    subset(idx+1)
    sel[idx] = 0
    subset(idx+1)

subset(0)
print(ans)