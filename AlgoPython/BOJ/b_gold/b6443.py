from collections import defaultdict

n = int(input())
for nn in range(n):
    arr = list(input())
    arr.sort()
    dict = defaultdict(int)
    for string in arr:
        dict[string] += 1
    n = len(arr)
    start_arr = list(dict.keys())


    def perm(idx):
        if idx == n:
            print("".join(sel))
            return
        for i in range(len(start_arr)):
            if dict[start_arr[i]] > 0:
                dict[start_arr[i]] -= 1
                sel[idx] = start_arr[i]
                perm(idx + 1)
                dict[start_arr[i]] += 1


    for start in start_arr:
        dict[start] -= 1
        sel = [0] * n
        sel[0] = start
        perm(1)
        dict[start] += 1
