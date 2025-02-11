n, m = map(int, input().split())

# # (5) 순열
# arr = list(map(int, input().split()))
# arr.sort()
#
# visited = [False]*(n)
# sel = [0]*m
#
# def perm(sidx):
#     if(sidx==m):
#         print(*sel)
#         return
#     for i  in range(n):
#         if(not visited[i]):
#             visited[i] =True # 나는 오면 안돼서 visited 필요
#             sel[sidx] = arr[i]
#             perm(sidx+1)
#             visited[i] = False
# perm(0)


# # (6) 다 넘겨버렷 조합
# arr = list(map(int, input().split()))
# arr.sort()
# sel = [0]*m
#
# def combi(sidx,idx):
#     if(sidx ==m):
#         print(*sel)
#         return
#     if(idx ==n):
#         return
#     sel[sidx] = arr[idx]
#     combi(sidx+1,idx+1)
#     combi(sidx,idx+1)
# combi(0,0)

# (7) 순열 중복 오케이
arr = list(map(int, input().split()))
arr.sort()
sel = [0]*m
def perm(sidx):
    if(sidx ==m):
        print(*sel)
        return


    for i in range(n):
        sel[sidx] = arr[i]
        perm(sidx+1)

perm(0)

# (8) 조합인데 나는 내가 돼도 괜찮아
arr = list(map(int, input().split()))
arr.sort()
sel = [0]*m

combi(0,0)