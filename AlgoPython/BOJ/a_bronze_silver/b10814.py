arr = []

n = int(input())
for i in range(n):
    age, name = input().split()
    age = int(age)
    arr.append([i,age,name])

arr.sort(key=lambda x:(x[1],x[0]))
for _ in arr:
    print(_[1], _[2])
