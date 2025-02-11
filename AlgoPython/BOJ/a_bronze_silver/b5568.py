'''
문제 설명
    카드들 중 k개를 선택
    이 선택된 카드들을 자유롭게 나열했을 때
    몇개의 경우의 수가 발생하는가?

    1. 선택해서 나열하는 것은 순열 1,2 랑 2,1 은 다르다
        1. 이 때 중복체크가 필요하다.
        
    중복체크를 visited로 일차원 리스트를 썼는데 ... 
    만들 수 있는 숫자가 커서 메모리초과가 난 것 같다
    -> set으로 해결

'''

n = int(input())
m = int(input())
arr = []
for i in range(n):
    arr.append(input())

result = set()
visited = [False]*n
def btk(idx,num):
    if(idx ==m):
        if(num not in result):
            result.add(num)
        return
    for i in range(n):
        if not visited[i]:
            visited[i] = True
            btk(idx+1,num+str(arr[i]))
            visited[i] = False

btk(0,"")
print(len(result))