'''
A의 수 재배열
'''

n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
ans = 0
while A:
    ans += A.pop(0)*max(B)
    B.remove(max(B))
print(ans)