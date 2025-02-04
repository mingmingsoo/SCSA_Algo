n, k = map(int, input().split())

mok = 1
mod = 1
for i in range(n,n-k,-1):
    mok *= i
for i in range(k,0,-1):
    mod *= i
print((mok//mod)%10007)