n = int(input())
time_list = []
pay_list = []
for i in range(n):
    t, p = map(int, input().split())
    time_list.append(t)
    pay_list.append(p)
time_list.append(1) # 마지막 날까지 일 할 수 있음!! 그래서 append 해줌
pay_list.append(0)
ans =0
def btk(day, pay):
    global ans
    if(day>n): # 넘어가면 안되고
        return
    ans = max(ans, pay) # 최댓값은 계속 계산해줌
    btk(day+time_list[day], pay+pay_list[day])
    btk(day+1, pay)

btk(0,0) # 날짜와 pay
print(ans)