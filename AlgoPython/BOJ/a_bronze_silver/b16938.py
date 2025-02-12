'''
문제설명
    문제를 선택했을 때 난이도가 L보다 크고 R보다 작거나 같아야! 함
    가장 어려운 문제와 쉬운 문제의 난이도 차이는 X보다 크거나 같아야!함

입력
    총 문제 갯수 N, 난이도 합 L, R, 차이 X
    난이도 리스트

구상
    부분집합으로 sel 길이가 2 이상인 애들의 조건을 따져서
    조건이 맞으면 갯수를 세준다.
'''

n, lt, gt, x = map(int, input().split())
arr = list(map(int, input().split()))


ans = 0
sel = [0]*n

def subset(idx):
    global ans
    if idx == n:
        if(sel.count(1)<2): # 선택을 2개 미만 했으면 return
            return

        # 내가 선택한 문제 배열
        pick = []
        for i in range(n):
            if sel[i] == 1:
                pick.append(arr[i])

        # 조건검사
        if not(lt<=sum(pick)<=gt):
            return
        if(max(pick)-min(pick)>=x):
            ans+=1
        return

    sel[idx] = 0
    subset(idx+1)
    sel[idx] = 1
    subset(idx+1)

subset(0)
print(ans)