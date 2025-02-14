'''
적어도 M미터의 나무를 가져가기 위해 절단기에 설정할 수 있는 높이의 최댓값.
최대한 높이..
일단 조건을 만족하는 높이를 구하고. 높이를 조금씩 올려가기

반례
4 80
20 20 20 20

나무를 다 잘라야 하는 수가 있음
그래서 ans 를 0을 초깃값으로 설정해줘야함

'''
n,m = map(int, input().split())
arr = list(map(int, input().split()))

start = 0 # 여기서  틀림!
end = max(arr)

ans = 0 # 최댓값 출력이므로,

def isOk(middle):
    add = 0
    for tree in arr:
        if(tree>middle):
            add += tree-middle
    if add >= m:
        return True
    else:
        return False

while start<=end:
    middle = (start+end)//2

    if(isOk(middle)): # 집에갈 수 있어 -> start를 좀만 높여보자.
        ans = middle
        start = middle+1
    else: # 좀만 낮혀보자
        end  = middle-1

print(ans)