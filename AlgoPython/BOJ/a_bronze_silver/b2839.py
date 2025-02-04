'''
3x+5y = 18 이 되는 x,y 찾기
단 x+y가 작아야함.
'''
num = int(input())
ans = float("inf")
for i in range(num//3+1):
    for j in range(num//5+1):
        if(3*i+5*j == num):
            ans = min(ans, i+j)
if(ans == float("inf")):
    ans = -1
print(ans)