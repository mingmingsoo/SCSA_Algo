import copy

L,N,T = map(int, input().split())

balls = []

# 값들로만 연산하면 되는데 2차원 배열까정 만들어서 진짜 공들을 이동시켰다
# -> 충돌처리도 어렵고 만나는 공ㄷ들이 순차적으로 이동해서 움직이게 하는게 안됨
# 굳이 배열에 위치시켜서 이동시킬 피룡가 없다. 리스트로 처리하면 된당

# 벽은 0,과 8 임
bomb = 0
for i in range(N):
    idx, dir = input().split()
    idx = int(idx)
    balls.append([idx,dir])
# print(balls)
for t in range(T):
    # 일딘 이동시키고
    for i in range(N):
        idx,dir = balls[i]
        if(dir =="R"):
            balls[i][0] = idx+1
        if(dir =="L"):
            balls[i][0] = idx-1
    # 벽 맞는지 검사
    for i in range(N):
        idx,dir = balls[i]
        if(dir =="R" and idx == L):
            balls[i][1] =  "L"
        if(dir =="L" and idx == 0):
            balls[i][1] =  "R"
    # 부닥치는지 검사
    for i in range(N):
        idx, idir = balls[i]
        for j in range(i+1,N):
            jdx, jdir = balls[j]
            if(idx==jdx):
                balls[i][1], balls[j][1] = balls[i][1], balls[j][1]
                bomb+=1
# print(balls)
print(bomb)