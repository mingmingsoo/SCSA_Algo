list = []
for _ in range(9):
    list.append(int(input()))
max = max(list)
print(max)
print(list.index(max)+1)