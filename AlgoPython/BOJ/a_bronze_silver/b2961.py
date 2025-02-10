'''
10분
신 곱
쓴 합

신- 쓴 가장 적게

부분집합......
'''

n = int(input())

A = []
B = []
for i in range(n):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)
sel = [0]*n
empty = [0]*n
ans = float("inf")
def subset(idx):
    global ans
    if(idx ==n):
        if(sel == empty):
            return
        a = 1
        b = 0
        for i in range(n):
            if(sel[i]==1):
                a*=A[i]
                b+=B[i]
        diff = abs(a-b)
        ans = min(ans, diff)
        return

    sel[idx] = 1
    subset(idx+1)
    sel[idx] = 0
    subset(idx + 1)

subset(0)
print(ans)