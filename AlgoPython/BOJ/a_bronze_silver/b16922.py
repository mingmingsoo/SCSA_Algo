'''
[문제 설명]
    I, V, X, L : 1 5 10 50
    로마숫자 N개를 사용해서 나올 수 있는 경우의 수를 구해라
[입력]
    사용할 수 있는 갯수
[출력]
    경우의 수를 출력
[구상]
    0,1,2,3 으로 문자를 치환해서
    중복 조합을 생성한다.
    visted 배열을 사용해서 중복을 막는다
'''

m = int(input())
sel = [0]*m
cnt = 0
visited_num = [False]* (50*20+1) # 만들 수 있는 최대 숫자
def btk(sidx,idx):
    global cnt
    if(sidx==m):
        num = 0
        for i in range(m):
            if (sel[i] == 0):
                num += 1
            elif (sel[i] == 1):
                num += 5
            elif(sel[i]==2):
                num+=10
            else:
                num+=50
        if(not visited_num[num]):
            visited_num[num] = True
            cnt+=1
        return
    if(idx==4):
        return
    sel[sidx] = idx
    btk(sidx+1,idx) # 나는 날 선택해도 괜찮아
    btk(sidx,idx+1) # 돌아와서는 전보단 커야해




btk(0,0)

print(cnt)