n , m= map(int, input().split())
list = [0]*n
# for _ in range(n):
#     list.append(0)
for _ in range(m):
    i,j,k = map(int, input().split())
    i -= 1
    j -= 1
    for x in range(i,j+1):
        list[x] = k

print(" ".join(map(str, list)))