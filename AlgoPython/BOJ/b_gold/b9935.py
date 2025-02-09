from collections import deque
import sys
input = sys.stdin.readline
line = list(input())
bomb = list(input())

q = deque([])
for i in range(len(line)):
    s = line[i]
    # 일단 넣고
    q.append(s)
    # q에서 c4인 애들을 찾아
    isBomb = False
    if(len(q)>=len(bomb)):
        isBomb = True
        for j in range(len(q)-1,len(q)-len(bomb)-1,-1): #1,0
            if(q[j]!=bomb[j-len(q)+len(bomb)]):
                isBomb = False
                break
    if(isBomb):
        for j in range(len(bomb)):
            q.pop()

if(not q):
    print("FRULA")
else:
    print("".join(q))
