# 키 순서대로 줄 섬
T = int(input())
for t in range(T):
    tmp = list(map(int, input().split()))
    tc = tmp[0]
    info = tmp[1:]
    cnt = 0
    for i in range(0,20):
        isBig = False
        pos = i
        for j in range(0,i):
            if(info[i]<info[j]):
                isBig= True
                pos = j
                break
        if(isBig==True):
            key = info[i]
            del info[i]
            info.insert(pos,key)
            cnt+=(i-j)
        # print(info)
    print(tc, cnt)