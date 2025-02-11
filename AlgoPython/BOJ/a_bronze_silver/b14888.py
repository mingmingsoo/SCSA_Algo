'''
문제 설명
    연산자의 종류와 갯수가 주어질 때 구할 수 있는 값의 최대, 최소를 구해줘야 한다
    * 연산자 우선순위는 무시할 수 있다.

입력
    n개의 수
    수열
    연산자의 갯수(+ - * %)
'''
n = int(input())
arr = list(map(int, input().split()))

cal_tmp = list(map(int, input().split()))
# 쓸 수 있는 연산자 리스트를 만들기
# 0 +
# 1 -
# 2 *
# 3 %
cal_list = []
for i in range(4):
    while(cal_tmp[i]>0):
        cal_list.append(i)
        cal_tmp[i] -=1
# print(cal_list) # 얘네들을 수열로!

m = len(cal_list)
visited = [False]*m
sel = [0]*m
ans_min = 1_000_000_001
ans_max = -1_000_000_001

def btk(idx):
    global ans_min, ans_max
    if(idx==m):
        # 연산 시작
        rlt = arr[0]
        for i in range(m):
            if(sel[i]==0):
                rlt += arr[i+1]
            elif (sel[i] == 1):
                rlt -= arr[i+1]
            elif (sel[i] == 2):
                rlt *= arr[i+1]
            elif (sel[i] == 3):
                if(rlt<0 and arr[i+1]>0):
                    rlt *= -1
                    mok = rlt // arr[i + 1]
                    rlt = -mok
                else:
                    rlt //= arr[i+1]
        ans_min = min(rlt, ans_min)
        ans_max = max(rlt, ans_max)
        return

    for i in range(m):
        if not  visited[i]:
            visited[i] = True
            sel[idx] = cal_list[i]
            btk(idx+1)
            visited[i] = False

btk(0)
print(ans_max)
print(ans_min)

