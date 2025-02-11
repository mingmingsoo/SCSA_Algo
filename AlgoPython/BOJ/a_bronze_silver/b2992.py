'''
[문제 설명]
    X가 주어졌을 때 수를 이루는 숫자가 같으면
    X보다 큰 수중 가장 작은 수 출력
    즉 123 과 321은 구성이 같다
[입력]
    X
[출력]
    구성이 같으면서 X보다 크면서 가장 작은 값
[구상]
    123 을 배열 1,2,3, 으로 만들어서 순열을 생성
    출력해야 하는 값 갱신

'''
origin = int(input())
arr = list(str(origin))
ans = 1000000
n = len(arr)
visited = [False]*n
def btk(idx,num):
    global ans
    if(idx==n):
        num = int(num)
        if(num>origin):
            ans = min(ans,num)
        return
    for i in range(n):
        if(not visited[i]):
            visited[i] = True
            btk(idx+1,num+arr[i])
            visited[i] = False

btk(0,"")
if(ans == 1000000):
    print(0)
else:
    print(ans)