'''
문제설명
    1~N까지 직선구간에서 M초동안 이동한다
    초기크기는 1이고 시작위치는 0
    1. 밀기: 현재위치+1칸으로 이동 -> 현재위치+1칸 크기만큼 늘ㄹ어남
    2. 차기: 현재위치+2칸으로 이동 -> 현재크기는 절반으로 줄어들고, +2칸 크기만큼 늘어남

    끝지점에 도달한 경우 시간이 남아도 끝남.
    가장 큰 크기는??

구상
    bfs로 푸는 것 같은데... 최대경로라서.... return해주면 안될 것 같다.
    visited는 필요 없을 듯. 뒤로가지는 않으니까
    최대힙으로 풀 수 있을까? 안될듯...
'''
import heapq
def bfs(start, s): # 시작점0과 초기사이즈 1
    global ans
    q = []
    heapq.heappush(q, (-s,start,0)) # 크기, 위치, 시간
    while q:
        size, cur, time = heapq.heappop(q)
        size *= -1
        # if(size < d[cur]):
        #     continue
        if (time >= limit): # 시간이 끝났으면 q에 그만담아!!!!!!!!
            continue
        if (cur + 1 <= n):
            if(d[cur+1] < size + arr[cur + 1]):
                d[cur+1] = size + arr[cur + 1]
                heapq.heappush(q, (-(size + arr[cur + 1]), cur + 1, time + 1))
        if (cur + 2 <= n):
            if(d[cur+2] < size // 2 + arr[cur + 2]):
                d[cur+2] = size // 2 + arr[cur + 2]
                heapq.heappush(q, (-(size // 2 + arr[cur + 2]), cur + 2, time + 1))

T = int(input())
for tc in range(T):

    n, limit = map(int, input().split())
    arr = list(map(int, input().split()))
    arr.insert(0, 0)
    d = [0]*(n+1) # 크기를 담는 배열, 작은값으로 초기화
    d[0] = 1 # 시작 크기는 1
    bfs(0, 1)
    print(d)