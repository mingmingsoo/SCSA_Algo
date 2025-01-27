n = int(input())
dict = {}
arr = list(map(int, input().split()))
for _ in arr:
    dict[_] = 0
for _ in arr:
    dict[_] =  dict[_]+1
# print(dict)

m = int(input())
arr2 = list(map(int, input().split()))
for i in arr2:
    if(i in dict.keys()):
        print(dict[i], end = " ")
    else:
        print(0, end = " ")

