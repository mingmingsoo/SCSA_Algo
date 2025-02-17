'''
곡괭이 순서를 순열로
최소 피로도를 출력
'''

picks =[1, 3, 2]
minerals = ["diamond", "diamond", "diamond", "iron", "iron", "diamond", "iron", "stone","diamond", "diamond", "diamond", "iron", "iron", "diamond", "iron", "stone","diamond", "diamond", "diamond", "iron", "iron", "diamond", "iron", "stone"]
minerals_list = []
piro_list = [[1, 1, 1], [5, 1, 1], [25, 5, 1]]
for m in minerals:
    if (m == "diamond"):
        minerals_list.append(0)
    elif (m == "iron"):
        minerals_list.append(1)
    else:
        minerals_list.append(2)
# print(minerals_list)

arr = []
idx = 0
for num in picks:
    for j in range(num):
        arr.append(idx)
    idx += 1
arr_len = min(len(arr), len(minerals_list)//5+1)
arr = arr[:arr_len]
sel = [0] * len(arr)
ans = float("inf")
visited = [False] * len(arr)
total_set = set()


def perm(idx):
    global ans
    if (idx == len(arr)):
        piro = 0
        have = []
        for x in sel:
            for j in range(5):
                have.append(x)
        for i in range(len(have)):
            if (i >= len(minerals_list)):
                break
            piro += piro_list[have[i]][minerals_list[i]]
            if (piro >= ans):
                return
        ans = min(ans, piro)
        return
    for i in range(len(arr)):
        if not visited[i]:
            visited[i] = True
            sel[idx] = arr[i]
            perm(idx + 1)
            visited[i] = False

ans = float("inf")
perm(0)
print(ans)
