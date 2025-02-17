'''
문제
    큐 1개, stack 1개 를 사용해서 순차적으로 학생들을 빼내라
구상
    1. 줄 서는 곳 q
    2. 대기줄 q
    3. num (1부터시작)
    1,2의 0번째가 num이 되면 빼내기 가능
    1 -> 2 가능 2 -> 1 불가능
'''

n = int(input())
arr = list(map(int, input().split()))
wait = []

num = 1

# num이 n이 되면 다 넘어온 것
ans = "Sad"
stack = []
while num<=n:
    if(arr and arr[0]==num):
        arr.pop(0)
        num+=1
    elif(stack and stack[-1]==num):
        stack.pop()
        num+=1
    else:
        if arr:
            stack.append(arr.pop(0))
        else:
            break
if(not stack and not arr):
    ans = "Nice"
print(ans)
