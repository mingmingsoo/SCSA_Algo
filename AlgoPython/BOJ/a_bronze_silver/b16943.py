'''
문제
    A에 포함된 숫자의 섞어 C를 만듬(순열)
    B보다 작으면서 가장 큰 값은?
구상
    1. A를 String으로 둔 채 순열을 돌린다.
    2. 순열들 중에 0으로 시작하면 return
    3. return 되지 않은 애들 중에 조건에 만족하는 애를 출력한다.
'''

a, b = input().split()
a = list(a)
a.sort(reverse = True)
b = int(b)
n = len(a)
sel = ["0"] * n # 내가 선택할 순열
visited = [False] * n
ans = -1

def perm(idx):
    global ans
    if(ans!=-1):
        return
    if( int(("".join(sel))) >b):
        return
    if (idx == n): # 순열 생성
        if (sel[0] == "0"): # 그런데 0으로 시작하면 안된다.
            return
        num = int(("".join(sel))) # 숫자로 변환
        if (num < b): # 조건을 만족하는애들 중에 가장 큰 값
            ans = max(ans, num)
        return
    for i in range(n):
        if not visited[i]:
            visited[i] = True
            sel[idx] = a[i]
            perm(idx + 1)
            visited[i] = False


perm(0)
print(ans)
