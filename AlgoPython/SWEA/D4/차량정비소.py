T = int(input())
for tc in range(T):
    '''
    어렵당. 관리할 자료구조가....
    '''
    import heapq
    from collections import defaultdict

    in_num, out_num, people_num, ans1, ans2 = map(int, input().split())
    in_time = list(map(int, input().split()))
    out_time = list(map(int, input().split()))
    tmp = list(map(int, input().split()))
    people_time = defaultdict(list)
    for idx, t in enumerate(tmp):
        people_time[t].append(idx)
    ining = [0] * in_num
    outing = [0] * out_num
    in_who = [-1] * in_num
    out_who = [-1] * out_num
    people_when_out_come = [-1] * people_num
    wait_in = list(range(people_num))
    wait_out = []

    people_info = [[0] * 2 for i in range(people_num)]
    time = 0
    all_end = []
    while len(all_end) != people_num:
        people_time[time].sort()
        come = people_time[time]
        for num in come:
            for i in range(in_num):
                if in_who[i] == -1:
                    people_info[num][0] = i
                    wait_in.remove(num)  # q로 바꿀까
                    ining[i] += 1
                    in_who[i] = num
                    break
            else:
                people_time[time + 1].append(num)

        for i in range(in_num):
            if ining[i] == in_time[i]:
                people_when_out_come[in_who[i]] = time
                wait_out.append(in_who[i])
                ining[i] = 0
                in_who[i] = -1
            elif ining[i]:
                ining[i] += 1  # 시간 증가

        if wait_out:
            fast = []
            for num in wait_out:
                fast.append((people_when_out_come[num], people_info[num][0], num))
            fast.sort()
            for time_, in_info, num in fast:
                for i in range(out_num):
                    if out_who[i] == -1:
                        people_info[num][1] = i
                        wait_out.remove(num)
                        outing[i] += 1
                        out_who[i] = num
                        break

        for i in range(out_num):
            if outing[i] == out_time[i]:
                outing[i] = 0
                all_end.append(out_who[i])
                out_who[i] = -1
            elif outing[i]:
                outing[i] += 1  # 시간 증가
        time += 1

    ans = 0

    for idx, info in enumerate(people_info):
        if info == [ans1 - 1, ans2 - 1]:
            ans += idx + 1

    # for i in range(people_num):
    #     print("몇번 사람:", i+1, "정보:", people_info[i][0]+1,people_info[i][1]+1)

    if ans == 0:
        print(f"#{tc+1} -1")
    else:
        print(f"#{tc+1} {ans}")


# 1
# 2 2 8 2 1
# 10 3
# 2 9
# 0 2 3 3 4 6 6 7