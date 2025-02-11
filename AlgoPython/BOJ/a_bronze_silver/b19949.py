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
ans = 0
sel = [0]*10
def btk(idx, after, cnt):
    global ans
    if(idx ==10):
        score = 0
        print(sel)
        for i in range(10):
            if(solve[i]==sel[i]):
                score+=1
        if(score>=5):
            ans+=1
        return
    for i in range(1,6):
        sel[idx] = i
        btk(idx+1, after, cnt+1)


btk(0,0,0,0)
print(ans)