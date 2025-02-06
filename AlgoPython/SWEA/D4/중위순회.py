T = 10
for tc in range(T):
    '''
    이진트리가 주어지면
    중위순회로 출력해라
    중위: left root right
    어렵게 푼 느낌
    '''
    V = int(input())
    roots = [0] * (V + 1)
    lefts = [0] * (V + 1)
    rights = [0] * (V + 1)

    for i in range(V):
        tmp = list(input().split())
        if (len(tmp) == 4):
            root = int(tmp[0])
            word = tmp[1]
            left = int(tmp[2])
            right = int(tmp[3])

            roots[root] = word
            lefts[root] = left
            rights[root] = right
        elif (len(tmp) == 3):  # 왼쪽 자식만 있음
            root = int(tmp[0])
            word = tmp[1]
            left = int(tmp[2])
            roots[root] = word
            lefts[root] = left
        else:  # 말단애들
            root = int(tmp[0])
            word = tmp[1]
            roots[root] = word
    # print(roots)
    # print(lefts)
    # print(rights)

    visited = [False]*(V+1)
    def inorder(parent):
        if (lefts[parent] != 0):
            inorder(lefts[parent])
        if (lefts[parent] == 0):
            if(not visited[parent]):
                print(roots[parent], end="")
                visited[parent] = True
            return

        if (not visited[parent]):
            print(roots[parent], end="")
            visited[parent] = True


        if (rights[parent] != 0):
            inorder(rights[parent])
        if (rights[parent] == 0):
            if (not visited[parent]):
                print(roots[parent], end="")
                visited[parent] = True
            return
    print(f"#{tc+1} ",end="")
    inorder(1)
    print()

