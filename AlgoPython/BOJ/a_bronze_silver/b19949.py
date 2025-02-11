'''
문제 설명
    1~5의 수열을 잘 조합해서 정답이 있을 때 5점 이상일 경우를 출력.
    숫자를 연속 3번은 조합하지 않는다.
입력
    시험의 정답
출력
    5점 이상의 경우의 수
'''
solve = list(map(int,input().split()))
sel = [0]*10
ans = 0
def btk(idx): # cnt가 연속된 갯수, last_num 마지막 수
    global ans
    if(idx==10):
        total = 0
        for i in range(10):
            if(solve[i]==sel[i]):
                total+=1
        if(total>=5):
            ans+=1
        return
    for i in range(1,6):
        if(idx>1 and sel[idx-1] == sel[idx-2]==i):
            continue
        sel[idx] = i
        btk(idx+1)
btk(0)
print(ans)