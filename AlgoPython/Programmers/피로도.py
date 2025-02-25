def solution(k, dungeons):
    '''
    문제설명
        최소필요피로도, 소모피로도를 잘 맞춰서 최대한 많은 던전 탐색
    구상
        이것은. 순열이다.
    가지치기
        이미 max면 find하고 return
        피통 이미 없으면 return
    '''

    hp = k
    n = len(dungeons)

    sel = [0]*n
    visited = [False]*n
    total = 0
    find = False
    def perm(idx):
        nonlocal total, find
        if find:
            return
        if idx == n:
            start_hp = hp
            ele_total = 0
            for num in sel:
                start, minus = dungeons[num][0], dungeons[num][1]
                if(start_hp<start or start_hp-minus<0):
                    return
                start_hp -= minus
                ele_total+=1
                total = max(ele_total, total)
            find =True
            return
        for i in range(n):
            if not visited[i]:
                sel[idx] = i
                visited[i] = True
                perm(idx+1)
                visited[i] = False


    perm(0)
    return total