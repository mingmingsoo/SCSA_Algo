n = int(input())
arr = list(input())
arr_origin = arr[:]
def find():
    cycle = 0
    visited = set()
    for i in range(int(1e9)):
        if "".join(arr_origin) in visited:
            return cycle
        cycle+=1
        visited.add("".join(arr_origin))
        if len(arr_origin) % 2 == 0:
            for j in range(len(arr_origin) - 1, -1, -2):
                arr_origin.append(arr_origin.pop(j))
        else:
            for j in range(len(arr_origin) - 2, -1, -2):
                arr_origin.append(arr_origin.pop(j))

mod = find()

for i in range(n%mod):
    if len(arr) % 2 == 0:
        for j in range(len(arr) - 1, -1, -2):
            arr.append(arr.pop(j))
    else:
        for j in range(len(arr) - 2, -1, -2):
            arr.append(arr.pop(j))

print("".join(arr))
