n = int(input())
arr = list(map(int, input().split()))
if n == 1:
    print(sum(arr) - max(arr))
else:
    up, down, front, back, left, right = arr[3], arr[2], arr[0], arr[5], arr[4], arr[1]

    # 몇 면이 보이는지 갯수
    two_face = 4 * (n - 1) + (n - 2) * 4
    three_face = 4
    one_face = 4 * (n - 1) * (n - 2) + (n - 2) ** 2

    total = 0
    # 한 면
    total += one_face * min(arr)

    # 세 면
    two_list = [min(up, down), min(front, back), min(left, right)]
    total += three_face * (two_list[0] + two_list[1] + two_list[2])

    # 두 면
    max_two = max(two_list)
    two_list.remove(max_two)
    total += two_face * (two_list[0] + two_list[1])

    print(total)
