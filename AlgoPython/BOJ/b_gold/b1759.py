'''
[문제설명]
    최소 한개의 모음과 최소 두개의 자음으로 구성된 문자열을 만들어라.
    단 오름차순으로, 조합으로
[필요한 메서드]
combi: 조합
check: 조건만족 확인
'''

m,n = map(int, input().split())
arr = input().split()
arr.sort()

sel = [0]*m # 4라고 해놔서 1회 틀림
def check(sel):
    cnt = 0
    for s in sel:
        if(s in "aeiou"):
            cnt+=1
    not_cnt = m-cnt
    if(cnt>=1 and not_cnt>=2):
        return True
    return False

def combi(sidx,idx):
    if(sidx ==m):
        if(check(sel)):
            print("".join(sel))
        return

    if(idx==n):
        return

    sel[sidx] = arr[idx]
    combi(sidx+1,idx+1)
    combi(sidx,idx+1)

combi(0,0)
