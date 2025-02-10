# n , m = map(int, input().split())
#
# arr = list(map(int, input().split()))
# arr = sorted(list(set(arr)))
# # n개중   m 개를 고르는 데 중복조합임. -> visited가 필요 없다.
#
# ans = []
# sel = [0]*m
# n = len(arr)
# def duplePerm(idx,sidx):
#     if(sidx >= m):
#         print(*sel)
#         return
#     if(idx>=n):
#         return
#
#     for i in range(idx,n):
#         sel[sidx] = arr[i]
#         duplePerm(i,sidx+1)
#
# duplePerm(0,0)
#
