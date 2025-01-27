arr = []
n = int(input())
for i in range(n):
    arr.append(input())
sett = set(arr)
arr2 = list(sett)
arr2.sort(key = lambda x:(len(x),x))
# print(arr2)
for _ in arr2:
    print(_)