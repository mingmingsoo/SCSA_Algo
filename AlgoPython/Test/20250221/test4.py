'''
문제설명
    1. 벨트가 칸 위에 있는 로봇들과 함께 한 칸 회전한다.
    2.  로봇이 벨트가 가는 방향으로 한 칸 이동할 수 있으면 이동.
        (이동하려는 칸에 로봇이 없고 내구도가 1 이상)
    3. 내구도가 0이면 로봇 못올림
    4. 내구도가 0인 칸의 갯수가 k 개 이상이면 종료 아니면 1번으로 돌아감

구상
    1. 올려!
    2. 이동!
    3. 회전
    4. 검사
'''
import sys
input = sys.stdin.readline
n, k = map(int, input().split())
arr = list(map(int, input().split()))
visited = [0]*n
time = 0
while True:
    time +=1
    # 내려!
    if visited[n-1]:
        visited[n-1] = 0
    # 회전
    last = arr.pop()
    arr.insert(0,last)

    last_visited = visited.pop()
    visited.insert(0,last_visited)

    # 내려!
    if visited[n-1]:
        visited[n-1] = 0

    for i in range(n-1,-1,-1):
        if visited[i] == 0 and arr[i]>0 and i-1>=0 and visited[i-1]==1:
                arr[i]-=1 # 이동!
                visited[i] = 1
                visited[i-1] = 0

    if(arr[0]>0):
        arr[0] -=1 # 올려!
        visited[0] = 1



    # 검사

    if arr.count(0)>=k:
        break
print(time)




