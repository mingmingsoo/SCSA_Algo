n = int(input())
arr = [int(input()) for i in range(n)]
change_lst = []  # idx,color
for i in range(n - 1):
    if arr[i] != arr[i + 1]:
        change_lst.append((i, arr[i + 1]))
        change_lst.append((i + 1, arr[i]))
ans = n


def pang(arr_origin):
    global ans
    arr = arr_origin[:]
    while True:
        arr.append(-1)
        new_arr = []
        tmp = []
        same = -1
        find = False
        cnt = 1
        for i in range(len(arr)):
            if arr[i] == same:
                cnt += 1
                tmp.append(arr[i])
            elif arr[i] != same:
                if cnt < 4:
                    new_arr.extend(tmp)
                else:
                    find = True
                same = arr[i]
                cnt = 1
                tmp = [arr[i]]
        arr = new_arr
        if not find:
            break
    ans = min(ans, len(arr))


for idx, color in change_lst:
    origin = arr[idx]
    arr[idx] = color
    pang(arr)
    arr[idx] = origin
print(ans)
