'''
순서를 바꾼다음
최댓값을 연산한다.

1 2 3
3 2 1
다르기에 순열이라 생각한다.

최댓값을 구하려면 배열을 다 선택한 다음 계산할 수 있어서
가지치기는 어렵다.

'''

n = int(input())
arr = list(map(int, input().split()))

sel = [0]*n
visited = [False]*n
ans = -100*8-1
def btk(idx):
    global ans
    if(idx==n):
        # print(sel)
        # 연산해주는 과정
        total = 0
        for i in range(n-1):
            total += abs(sel[i]-sel[i+1])
        ans = max(ans, total) # 최댓값 갱신

    for i in range(n):
        if(not visited[i]):
            visited[i] = True
            sel[idx] = arr[i]
            btk(idx+1)
            visited[i] = False


btk(0)

print(ans)