import math

T = int(input())
for tc in range(T):
    before, after = map(int, input().split())
    if(before == 1 and after == 1):
        print("yes")
        continue
    if(before == 1 and after == 0):
        print("yes")
        continue
    if(before == 0 and after == 0):
        print("yes")
        continue

    def check(before, after):
        num = int(math.sqrt(abs(before)))+1
        for i in range(-num,num+1,1):
            if i==0:
                continue
            if(before//i +i ==after):
                return True
        return False

    if (check(before,after) or check(after,before)):
        print("yes")
    else:
        print("no")
