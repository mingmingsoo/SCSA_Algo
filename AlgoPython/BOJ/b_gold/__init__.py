'''
10 9 7
1
2
3
4
5
6
7
8
9

답 3

반례
'''


import heapq

end, n, m = map(int, input().split())
# 이분탐색인데 idx를

start = 0
tmp = [0]+[int(input()) for i in range(n)]+[end]
tmp.sort()
# print(tmp)
arr = [int(1e9)]

for i in range(len(tmp)-1):
    arr.append(tmp[i+1]-tmp[i])
arr.append(int(1e9))
# print(tmp)
# print(arr)

# print(arr)
ans = []
for mm in range(m):
    idx = -1
    info_arr = []
    for i in range(len(arr)):
        info_arr.append((arr[i],i))
    info_arr.sort()
    mini = info_arr[0][0]
    dist = 0
    start = 0
    end = 0
    start_idx = 0
    end_idx = 0
    for i in range(1,len(info_arr)):
        if info_arr[i][0] == mini:
            end = i
            if(end-start>dist):
                dist = end-start
            else:
                start = i

    idx = info_arr[start+(end-start)//2][1]
    print(tmp)
    print(arr)
    print(idx)
    if idx == 0:
        tmp.pop(idx+1)
    elif idx == len(arr)-1:
        tmp.pop(idx-1)
    else:
        tmp.pop(idx)
    arr = [int(1e9)]
    for i in range(len(tmp) - 1):
        arr.append(tmp[i + 1] - tmp[i])
    arr.append(int(1e9))
    heapq.heappush(ans,-min(arr))
    # print(tmp)
    # print(arr)
print(-heapq.heappop(ans))