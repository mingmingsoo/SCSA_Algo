# T = 10
# for t in range(T):
#
#     n = int(input())
#     arr = list(map(int, input().split()))
#     ans =0
#     for i in range(2,n-2): # 3
#         isView = True
#         maxheight = 0
#         for j in range(i-2, i+3): # 1~5
#             if(i==j):
#                 continue
#             if(arr[i]-arr[j]<=0):
#                 isView = False
#                 break
#             maxheight = max(maxheight, arr[j])
#         if(isView):
#             # print(i,arr[i]-maxheight)
#             ans+= (arr[i]-maxheight)
#     print(f'#{t+1} {ans}')



for test_case in range(3):
    T_length = int(input())
    lst = list(map(int, input().split()))
    total = 0

    for i in range(2, len(lst)-2):
        tmp = 0
        for j in range(i-2, i+3):
            if j==i:
                continue
            if (lst[j] >= lst[i]):
                tmp = 0
                break
            else:
                if lst[j] > tmp:
                    tmp = lst[j]
        # print(lst[i])
        if tmp != 0:
            total += lst[i] - tmp
    print(f'#{test_case+1} {total}')