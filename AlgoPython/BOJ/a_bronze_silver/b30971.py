'''
b30971
문제설명
    순열에 따른 감칠맛의 최대를 구해라
'''

n, limit = map(int, input().split())
info = [list(map(int, input().split())) for i in range(3)]
# 0행 단맛, 1행 짠맛, 2행 눈치


sel = [0]*n
visited = [False]*n
umami = -1

def perm(idx):
    global umami
    if idx ==n:
        # sel 순서대로 감칠맛 최대
        uma = 0

        for i in range(1,n):
            before = sel[i-1]
            cur = sel[i]
            nunchi = info[2][before]*info[2][cur]
            if nunchi<=limit:
                uma += (info[0][before]*info[1][cur])
            else:
                return
        umami = max(uma, umami)




        return

    for i in range(n):
        if not visited[i]:
            sel[idx] = i
            visited[i] = True
            perm(idx+1)
            visited[i] = False


perm(0)
print(umami)