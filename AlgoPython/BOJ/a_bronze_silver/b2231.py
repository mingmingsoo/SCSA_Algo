n = int(input())
isOk = False
for i in range(n):
    string = str(i)
    sum = i
    for s in string:
        sum += int(s)
    if(sum == n):
        isOk = True
        print(i)
        break
if(isOk == False):
    print(0)
