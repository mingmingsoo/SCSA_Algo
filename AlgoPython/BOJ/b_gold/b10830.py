n, b = map(int,input().split())

arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))

print(arr)

square_arr = [[0]*n for i in range(n)]

for x in range(n):
    for y in range(n):
        for i in range(n):
            square_arr[x][y] += arr[x][i] * arr[i][y]
print(square_arr)



