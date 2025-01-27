arr = [list(map(int, input().split())) for i in range(9)]

r = -1
c = -1
max = -1
for i in range(9):
    for j in range(9):
        if(arr[i][j]>max):
            r = i
            c = j
            max = arr[i][j]
print(f'{max}\n{r+1} {c+1}')