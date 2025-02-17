'''
최대한 많은 갯수를 사용해서 동전을 계산
뒤에서부터 시작해서.. 백트래킹
★하나만 찾고 나가도 된다.★
'''
n = int(input()) # 만드려는 숫자
arr = list(map(int, input().split()))
arr = arr[::-1]
won = [1,5,10,50,100,500] # 최대한 많은 동전을 찾기 위해 동전을 작은순으로 나열
count = [0]*6
ans_count = [0]*6
find = False

def btk(idx,sm,cnt):
    global ans,find
    if(find): # 백트래킹, 찾았으면 그것이 동전 최댓값이기에 다 return
        return
    if(sm==n): # 조건 만족
        find = True
        print(cnt) # 정답 출력
        print(*count[::-1])
        return
    if(idx==6):
        return

    w = won[idx] # 얼마짜리 동전?
    num = arr[idx] # 몇개

    if(sm+w>n): # 동전을 쓸 수도 없으면 return (즉 동전이 너무 크면)
        return

    for j in range(num,-1,-1):
        if(sm+w*j<=n): # 가능만 하다면 동전 있는데로 다 넣을거임
            count[idx]+=j # 갯수 올려주고
            btk(idx+1,sm+w*j,cnt+j) # 다음 동전으로
            count[idx] -=j # 아니면 다시 돌아와..
        else:
            continue # 동전이 너무 크면 좀 줄이기
btk(0,0,0)
