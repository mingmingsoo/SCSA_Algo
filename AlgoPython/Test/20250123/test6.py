# 키 순서대로 줄 섬
T = int(input())
for t in range(T):
    tmp = list(map(int, input().split()))
    tc = tmp[0]
    info = tmp[1:]
    cnt = 0
    for i in range(1,20):
        isBig = False
        for j in range(0,i):
            if(info[i]<info[j]):
                isBig= True
                break
        if(isBig==True):
            cnt += i
    print(tc, cnt)
