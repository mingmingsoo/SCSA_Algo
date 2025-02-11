'''
[문제 설명]
    부등호가 주어지는데 이 부등호를 만족시키는 숫자들 중 최댓값과 최솟값을 출력

[입력]
    부등호 갯수 n
    부등호 배열

[출력]
    부등호를 만족시키는 숫자의 최대, 최소

[구상]
    1.0~9개 중 n 개를 고른 순열 중
    2.부등호를 만족시키는 숫자를 찾는다.

'''

n = int(input())
gtlt = list(input().split())
m = n+1

visited = [False]*10
maxN = 0
ans_max = 0
minN = 9876543211
ans_min = 0
def perm(idx,num):
    global maxN, minN,ans_min, ans_max
    for i in range(len(num)-1):
        if (num[i] > num[i + 1] and gtlt[i] != ">"):
            return
        if (num[i] < num[i + 1] and gtlt[i] != "<"):
            return

    if(idx ==m):
        num_int = int(num)
        if(num_int<minN):
            ans_min = num
            minN = num_int
        if (num_int > maxN):
            ans_max = num
            maxN = num_int
        return
    for i in range(10):
        if not visited[i]:
            visited[i] = True
            perm(idx+1,num+str(i))
            visited[i] = False

perm(0,"")
print(ans_max)
print(ans_min)
