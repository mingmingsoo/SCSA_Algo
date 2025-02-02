'''
준영님. 서현님 아이디어 스틸후
아이디어를 구현해보기.

숫자 오름차순으로 넘버링해서 리스트에 담고
리스트에서 스택으로 하나씩 넣으면서 stk[-1]이랑 같으면 pop
아니면 append

시간초과난 이유:
in arr 검사시에 시간이 많이걸려서 set을 사용하면 단축시킬 수 있음.
'''


def checker():
    n = int(input())
    arr = set() # 시간초 빡빡하니 set 사용하기
    for i in range(n):
        x, r = map(int, input().split())
        left, right = x - r, x + r
        if left in arr or right in arr: # 이거 때문에 시간초과 났음.
            # list 대신 set 사용.
            print("NO")
            return
        arr.add((left, i))
        arr.add((right, i))
    arr = sorted(list(arr)) # 정렬을 위해서 list로 변환
    stk = []
    for i in range(len(arr)):
        idx = arr[i][1]
        if (not stk):
            stk.append(idx)
        else:
            if (idx == stk[-1]):
                stk.pop()
            else:
                stk.append(idx)
    if (not stk):
        print("YES")
        return
    else:
        print("NO")
        return


checker()

