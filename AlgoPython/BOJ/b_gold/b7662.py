from queue import PriorityQueue
T = int(input())

for tc in range(T):
    n = int(input())

    q = PriorityQueue()
    for i in range(n):
        order, num = input().split()
        # print(order, num)
        num = int(num)
        # print(q.queue)
        if(order=="I"):
            q.put((-num,num))
        else:
            if(q.qsize()==0):
                continue
            if(num == 1):
                q.get()[1]
                # print(q.get()[1]) # 최댓값
            else:
                q.get()[0]
                # print(q.get()[0])
        print(q.queue)
    if(q.qsize()==0):
        print("EMPTY")
    elif(q.qsize()==1):
        tmp = q.get()[1]
        print(tmp, tmp)
    else:
        print(-q.get()[0], q.get()[1])



