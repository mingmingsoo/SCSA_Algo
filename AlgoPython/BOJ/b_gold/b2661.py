'''
[문제설명]
    123으로만 이루어진 수열
    임의의 길이의 인접한 두 개의 부분 수열이 동일하면 나쁜 수열
    N 길이의 수열들 중에 좋은 수열이면서 가장 작은 수열은?
[구상]
    sel에 살이 붙을때마다 검사해서
    좋은 수열이 하나라도 발견되면 return 되게 해서 시간을 줄인다.
'''

n = int(input())
arr = [1,2,3]

sel = []
find = False

def isBadPerm():
    m = len(sel)
    start = 0
    end = m
    while m >=2: # 검사할 것이 2개 남았을 떄까지 비교
        front = []
        back = []
        m = end - start
        for i in range(start,start+m//2):
            front.append(sel[i])
        for i in range(start+m//2,end):
            back.append(sel[i])
        if(front == back):
            return False
        start += 1 # 하나씩 늘려가면서 다 검사해줘야함.
    return True
def perm(idx):
    global find
    if(find):
        return
    if(len(sel)>1 and not isBadPerm()):
        return # 좋은 수열 검사
    if(idx==n):
        find = True
        print("".join(map(str,sel)))
        return
    for i in range(3):
        sel.append(arr[i])
        perm(idx+1)
        sel.pop()

perm(0)