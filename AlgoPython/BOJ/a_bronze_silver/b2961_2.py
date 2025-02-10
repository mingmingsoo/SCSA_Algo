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

ans = float("inf")


def subset(idx, a, b, cnt):
    global ans
    if (idx == n):
        if (cnt > 0):
            ans = min(ans, abs(b - a))
        return
    subset(idx + 1, a * A[idx], b + B[idx], cnt + 1)
    subset(idx + 1, a, b, cnt)


subset(0, 1, 0, 0)  # idx,a,b,cnt
print(ans)
