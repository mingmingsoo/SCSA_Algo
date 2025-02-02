'''
문제 시작 15:54

문제 설명
원들의 정보가 주워졌을 때 교점이 존재하지 않는가?
교점이 존재하지 않으려면
1. 원안의 원(겹치는 부분이 있으면 안됨....)
2. 완전 밖의 원
3. 중심 좌표는 음수일 수 도 있음.

교점이 존재하지 않으면 Yes, 아니면 No 출력

필요한 배열
range_list, 각 원들의 끝점에 해당하는 좌표를 true 체크함.

이중포면까지 가면 안됨.

2 2
3 1
'''

info_list = []

n = int(input())
xylist = []
for i in range(n):
    x, r = map(int, input().split()) # 중심좌표와 반지름
    info_list.append((x,r))
    eleMin = x-r
    eleMax = x+r
    xylist.append((eleMin, eleMax))
# print(info_list)

ans = "YES"
def check():
    global  ans
    for i in range(n):
        x, r = info_list[i]
        eleMin = x - r
        eleMax = x + r
        # 교점이 생기는 경우
        # 끝값 사이에 하나라도 점이 있으면
        # print(eleMin, eleMax)
        # print(xylist)
        for j in range(i+1,n):
            # if(i==j):
            #     continue
            x1, x2 = xylist[j]
            # print(x1,x2,eleMin,eleMax)
            if(x1 == eleMax or x1 == eleMin or x2 == eleMax or x2 == eleMin):
                ans = "NO"
                return

            if(x1<=eleMin<=x2):
                if(x1<=eleMax<=x2):
                    continue
                else:
                    ans = "NO"
                    return
            if(x1<=eleMax<=x2):
                if(x1<=eleMax<=x2):
                    continue
                ans = "NO"
                return
check()
print(ans)
