'''
어려운데....
원자가 없어질떄까지 관리야..?원자가 범위 넘어가면 충돌 안한다는 거니까 그런애들은 romove해주고
원자가 없어질때까지 해줘야되네
1. 검사할 거
    - 격자밖으로 벗어나냐? - 없애줌
    - 나랑똑같은애들 뒤에서부터 찾아서 없애줌-> 인덱스 담아놓기
    - 나랑 r,c가 뭐 하나 같고 1 차이나는데 방향이 반대면 걔도 없애줌
시초날 수도
시초다.
3차원으로 풀었는데 더 느림, 다시 빠꾸
4
-1 0 3 5
1 0 2 3
0 1 1 7
0 -1 0 9

2
1 1 3 3
4 1 2 3


14
-6 5 3 1
-3 5 2 1
-5 2 1 1
3 5 3 1
5 7 1 1
6 7 3 1
7 5 2 1
5 3 0 1
-4 -4 1 1
-4 -6 0 1
5 -3 2 1
6 -4 1 1
4 -6 0 1
9 -7 2 1
'''
T = int(input())
row = [0, 0, -0.5, 0.5]
col = [0.5, -0.5, 0, 0]
for tc in range(T):
    n = int(input())
    atom_dict = {}
    for i in range(n):
        r, c, d, power = map(int, input().split())
        atom_dict[(r, c)] = [d, power, 1]
    ans = 0
    while atom_dict:
        new_atom_dict = {}
        for k, v in atom_dict.items():
            d, power, num = v
            r, c = k
            nr = r + row[d]
            nc = c + col[d]
            if (-1000 <= nr <= 1000 and -1000 <= nc <= 1000):
                if (nr, nc) in new_atom_dict:
                    new_atom_dict[(nr, nc)][2] += 1
                    new_atom_dict[(nr, nc)][1] += power
                else:
                    new_atom_dict[(nr, nc)] = [d, power, 1]

        real_new_dict = {}
        for k, v in new_atom_dict.items():
            if v[2] > 1:
                ans += v[1]
            else:
                real_new_dict[k] = v

        atom_dict = real_new_dict
    print(f"#{tc + 1} {ans}")
