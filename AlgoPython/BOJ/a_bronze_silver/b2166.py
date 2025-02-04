'''
신발끈 공식
음수로 들어오는 값들을 양수처리 해줘야함 +100000
'''
n = int(input())
arr = []
for i in range(n):
    x,y = map(lambda x:int(x)+100000, input().split())
    arr.append((x,y))
arr.append(arr[0])

area = 0

for i in range(0,n):
    area += (arr[i][0]*arr[i+1][1] - arr[i+1][0]*arr[i][1])

area = round(abs(area) / 2, 2)
print(f"{area:.1f}")