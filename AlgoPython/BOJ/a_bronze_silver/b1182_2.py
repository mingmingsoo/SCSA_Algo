'''
부분집합..
5 0
1 2 3 4 5
이 때는 어떻게 처리해주지?
'''

n, target = map(int, input().split())
arr = list(map(int, input().split()))

ans = 0

def subset(idx, sm):
    global ans
    if(idx ==n):
        if(sm==target):
            ans+=1
        return

    subset(idx+1,sm+arr[idx])
    subset(idx+1,sm)

if(target==0):
    ans -=1
subset(0,0) # idx, sum
print(ans)



'''
부분집합..
5 0
1 2 3 4 5
이 때는 어떻게 처리해주지?
'''

n, target = map(int, input().split())
arr = list(map(int, input().split()))

ans = 0

def subset(idx, sm, cnt):
    global ans
    if(idx ==n):
        if(sm==target and cnt>0):
            ans+=1
        return

    subset(idx+1,sm+arr[idx],cnt+1)
    subset(idx+1,sm,cnt)

subset(0,0,0) # idx, sum, cnt
print(ans)