'''
사이클이 5번
한 사이클 돌 때마다 빼주는 값을 1로 초기화 해주는 로직 필요.
'''


def isRange(q):
    for i in range(8):
        if (q[i] <= 0):
            q[i] = 0
            return False
    return True


def cycle():
    while True:
        num = 1
        for i in range(5):
            left = q.pop(0)
            q.append(left - num)
            if (not isRange(q)): # 하나라도 음수가 나오면 0 처리 하고 return
                return  # return 처리 하려고 굳이 함수로 정의했음
            num += 1

T = 10
for tc in range(T):
    tnum = int(input())
    q = list(map(int, input().split()))

    cycle() # 돌아라!

    print(f"#{tnum}", end = " ")
    print(*q)
