tmpking, tmpstone, T = input().split()

tmpking = list(tmpking)
tmpstone = list(tmpstone)

kingC = ord(tmpking[0]) - 65
kingR = int(tmpking[1]) -1

stoneC = ord(tmpstone[0]) - 65
stoneR = int(tmpstone[1]) -1


for t in range(int(T)):

    order = input()
    nextR = kingR
    nextC = kingC
    if (order == "R"):
        nextC += 1
    elif (order == "L"):
        nextC -= 1
    elif (order == "B"):
        nextR -= 1
    elif (order == "T"):
        nextR += 1
    elif (order == "RT"):
        nextR += 1
        nextC += 1
    elif (order == "LT"):
        nextR += 1
        nextC -= 1
    elif (order == "RB"):
        nextR -= 1
        nextC += 1
    elif (order == "LB"):
        nextR -= 1
        nextC -= 1

    rdis = nextR - kingR
    cdis = nextC - kingC
    isKingGo =False
    isStoneGo = False
    # 범위검사. 범위에 해당하면 이동.
    if(0<=nextR<8 and 0<=nextC<8):
        isKingGo = True
        if(nextR == stoneR and nextC == stoneC):
            isStoneGo = True
    if(isStoneGo):
        if not (0 <= stoneR + rdis < 8 and 0 <= stoneC + cdis < 8):
            isKingGo = False
            isStoneGo = False
    if(isKingGo):
        kingR = nextR
        kingC = nextC
        if(isStoneGo):
           stoneR += rdis
           stoneC += cdis


print(chr(kingC+65), end= "")
print(kingR+1)
print(chr(stoneC+65), end = "")
print(stoneR+1)

