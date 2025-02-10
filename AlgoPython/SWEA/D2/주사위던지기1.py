# T = int(input())
# for tc in range(T):
#
#     m = int(input())
#     arr = list(range(1, 7))
#     sel = [0] * m
#
#     def perm(sidx):
#         if (sidx == m):
#             print(*sel)
#             return
#         for i in range(6):
#             sel[sidx] = arr[i]
#             perm(sidx + 1)
#
#     print(f"#{tc+1}")
#     perm(0)


T= int(input())

def btk(sidx,idx):
    if(sidx==m):
        print(*sel)
        return
    if(idx ==6):
        return
    sel[sidx] = arr[idx] # 값을 선택하고
    btk(sidx+1,idx) # 중복되도 괜찮아!
    btk(sidx,idx+1) # 근데 전의 값들은 idx가 전에보다 커야돼..

for tc in range(T):
    m = int(input())
    arr = list(range(1,7))
    sel = [0] * m
    print(f"#{tc+1}")
    btk(0,0)


T = int(input())


def btk(idx):
    if(idx ==m):
        if(sum(sel)==SUM):
            print(*sel)
        return

    for i in range(6):
        sel[idx] = arr[i] # 모든 경우의 수를 다 탐색해야된다.
        btk(idx+1) # 다음으로 넘어갓!

for tc in range(T):
    m, SUM = map(int, input().split())

    arr = list(range(1,7))
    sel = [0]*m
    print(f"#{tc+1}")
    btk(0)
