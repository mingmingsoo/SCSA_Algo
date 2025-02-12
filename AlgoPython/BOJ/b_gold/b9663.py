'''
[문제 설명]
    외웠던 문제라 잔상이....

    점을 선택했을 때
    행 같으면 안됨, 열 같으면 안됨, 대각선 안됨

[구상]
    어차피 같은 행은 공격받으므로 열단위로 관리할 것임.

'''

n = int(input())

ans = 0
def isok(jdx): # 이 행이 진짜로 위치할 수 있는가?
    for i in range(jdx): # 지금까지 열 들 중에서
        if(arr[i]==arr[jdx]): # 같은 행이 있다면 아웃!
            return False
        if(abs(i-jdx)==abs(arr[i]-arr[jdx])): # 대각선이랑 같이 있어도 아웃!
            return False
    return True

def nqueen(jdx): # 열기준으로 할것임
    global cnt
    if(jdx==n): # 열 끝까지 왔으면
        cnt+=1 # 경우의 수 추가!
        return
    for i in range(n): # 얘는 행임
        arr[jdx] = i # 행을 넣어주고
        if(isok(jdx)): # 행이 있어도 되는 것인지 검사.
            nqueen(jdx+1) # 있을 수 있다면 다음 열로 넘어감.

cnt = 0
arr = [0]*n
nqueen(0) # 0->n으로 가서 중복되는 점이 없게끔 할것임
print(cnt)