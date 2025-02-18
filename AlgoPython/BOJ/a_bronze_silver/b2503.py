'''
문제 설명
    영수 : 1~9 3개 생각
    민혁 : 영수에게 3개 숫자 질문
    숫자들 중 동일한 위치에 위치하면 스트라이크
    숫자는 있으나 다른 위치면 볼
    3스트라이크면 게임이 끝남
    가능한 숫자의 경우의 수는?
구상
    111~999.. 검사..?ㅎ...
'''

arr = set()
for i in range(111,1000):
    st = str(i)
    if "0" not in st:
        test_set = set(st)
        if(len(test_set)==3):
            arr.add(st)
n = int(input())
grid = []
for i in range(n):
    num, strike,ball = input().split()
    grid.append((num, int(strike),int(ball)))
ans = 0
arr = sorted(list(arr))
# print(arr)

def isOk(num):

    for guess, strike, ball in grid:

        # guess = "123"
        total = 0
        ele_strike = 0

        num_copy = list(num)

        # 총 같은 갯수
        for ele_num in guess:
            if ele_num in num_copy:
                num_copy.remove(ele_num)
                total+=1

        for i in range(3):
            if(num[i]==guess[i]):
                ele_strike+=1

        ele_ball = total-ele_strike

        if(strike==ele_strike and ball==ele_ball):
            continue
        else:
            return False
    return True

for num in arr:
    if(isOk(num)):
        # print(num)
        ans+=1
print(ans)


# 2
# 121 2 0
# 111 3 0

# 2
# 111 2 0
# 222 1 0