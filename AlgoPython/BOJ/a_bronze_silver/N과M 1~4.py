n,m = map(int, input().split())

# # (1) 순열
# # 다시 돌아오는 로직이 필요
# sel = [0]*m
# visited = [False]*n
# def perm(sidx):
#     if(sidx == m):
#         print(*sel)
#         return
#     for i in range(n):
#         if not visited[i]:
#             visited[i] = True
#             sel[sidx] = i+1
#             perm(sidx+1)
#             visited[i] = False
# perm(0)

# # (2) 조합 다 넘어가버려잇
# sel = [0]*m
# def combi(sidx,idx):
#     if(sidx ==m):
#         print(*sel)
#         return
#     if(idx == n):
#         return
#
#     sel[sidx] = idx+1
#     combi(sidx+1,idx+1)
#     combi(sidx,idx+1)
# combi(0,0)

# # (3) 본인도 포함하는 순열
# sel = [0]*m
# def perm(sidx):
#     if(sidx == m):
#         print(*sel)
#         return
#     for i in range(n):
#         sel[sidx] = i+1
#         perm(sidx+1)
# perm(0)

# # (4) 전에껀 안가요 조합
#
# sel = [0]*m
#
# def combi(sidx,idx):
#     if(sidx==m):
#         print(*sel)
#         return
#     if(idx == n):
#         return
#
#     sel[sidx] = idx+1
#     combi(sidx+1,idx) # 나는 내가 될 수 있어요
#     combi(sidx,idx+1) # 근데 다시 돌아왔을 땐 나보다 커야해
#
# combi(0,0)

