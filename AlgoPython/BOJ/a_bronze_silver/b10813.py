n , m = map(int, input().split())
# list =[]
# for i in range(n):
#     list.append(i+1)

list = list(range(1,n+1))

for _ in range(m):
    i, j =  map(int, input().split())
    i-=1
    j-=1
    list[i], list[j] = list[j], list[i]
print(" ".join(map(str, list)))
