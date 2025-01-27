n,m = map(int, input().split())

list = list(range(1,n+1))

for _ in range(m):
    i, j = map(int, input().split())
    i -=1
    j -=1
    k = i+j
    for _ in range(i, int((i+j)/2)+1):
        list[_] , list[k-_] = list[k-_], list[_]

print(" ".join(map(str, list)))
