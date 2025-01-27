n = int(input())
q = []
for i in range(n):
    string = list(input().split())
    order = string[0]
    num = -1
    if(len(string)>1):
        num = string[1]
    if order == "push":
        q.append(num)
    elif order == "pop":
        if(len(q)==0):
            print(-1)
        else:
            print(q[0])
            del q[0]
    elif order == "size":
        print(len(q))
    elif order == "empty":
        if(len(q)==0):
            print(1)
        else:
            print(0)
    elif order == "front":
        if(len(q)==0):
            print(-1)
        else:
            print(q[0])
    elif order == "back":
        if(len(q)==0):
            print(-1)
        else:
            print(q[len(q)-1])

