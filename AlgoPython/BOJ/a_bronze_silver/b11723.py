import sys
arr =[]
arr_origin = list(range(1,21))
T  = int(input())
for t in range(T):
    order = sys.stdin.readline().rstrip().split()
    if(order[0]=="add"):
        num = int(order[1])
        if(arr.__contains__(num) == False):
            arr.append(num)
    elif(order[0]=="remove"):
        num = int(order[1])
        if(arr.__contains__(num) == True):
            arr.remove(num)
    elif (order[0] == "check"):
        num = int(order[1])
        if(arr.__contains__(num) == True):
            print(1)
        else:
            print(0)
    elif (order[0] == "toggle"):
        num = int(order[1])
        if(arr.__contains__(num) == True):
            arr.remove(num)
        else:
            arr.append(num)
    elif (order[0] == "all"):
        arr = arr_origin[:]
    elif (order[0] == "empty"):
        arr =[]
    # print(arr)