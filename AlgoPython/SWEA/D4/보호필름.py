T = int(input())
for tc in range(T):
    '''
    풀었던 문제
    시작 15:27
    종료 16:27
    
    무한루프 돌아서 전에 푼 풀이 힐끔 봤음 아놔.
    
    문제 설명
    행 D, 열 W
    A, B의 특성
    합격기준 K
    각 열마다 동일한 특성 셀이 K개 이상 연속적으로 있는 경우에만 통과함.

    기준을 통과하기 위해서 약품을 사용할 수 있음
    약품은 각 행에 투입함. 선택된 행은 모두 A가 되거나 모두 B가 될 수 있음

    일단 K번 약품 쏘면 무조건 합격은 할 수 있음
    약품 쏘는 최소값을 구해라.

    0이면 A, 1이면 B

    1. 검사 : 각 열마다 연속된 셀이 ok만큼 있으면 재귀 안타도됨.
    2. 약물 투입 : 각 행마다 약물투입하고 return, 그 다음 투입하고 return, .. 부분집합이라고 생각하면 될듯
    '''
    import copy

    n, m, ok = map(int, input().split())  # 좌표와 pass 기준
    grid = [list(map(int, input().split())) for i in range(n)]
    ans = ok


    def valid(j):
        # 각 열마다 연속되는 애들이 ok만큼 있는가?
        if (j == m):
            return True  # 여기까지 왔으면 다 통과했음.
        i = 0
        while i <= n - ok:
            cur = grid[i][j]
            isOk = True
            for ii in range(i + 1, i + ok):
                if (cur != grid[ii][j]):
                    i = ii
                    isOk = False
                    break
            if (isOk):
                return valid(j + 1)
            else:
                continue
        return False


    def fill(idx, num):
        for j in range(m):
            grid[idx][j] = num

    def restore(idx, originGrid):
        grid[idx] = originGrid

    def dfs(idx, cnt):
        global ans

        if (valid(0)):
            ans = min(ans, cnt)
            return
        if(cnt>=ok-1): # 굳이 ok 까지 안가도됨.
            return
        if (idx >= n):
            return

        originGrid = grid[idx][:]
        # idx 행에 A로 약 투입.
        fill(idx, 0)
        dfs(idx + 1, cnt + 1)
        # restore(idx, originGrid)
        # 여기서 없고 마지막에만 복구하면 되는 이유
        # : dfs 타고 들어가는데, 복구해버리면 배열이 유지가 안됨.

        # idx 행에 B로 약 투입.
        fill(idx, 1)
        dfs(idx + 1, cnt + 1)
        restore(idx, originGrid)

        # 약 투입 안함.
        dfs(idx + 1, cnt)


    if (valid(0)):  # 초기검사.
        print(f"#{tc+1} 0")
    else:
        dfs(0, 0)  # idx, 투약횟수
        print(f"#{tc+1} {ans}")



