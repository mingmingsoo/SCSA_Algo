'''
# 제출횟수: 4회
# 메모리: 293088 KB
# 시간: 792 ms
# 헷 pypy 시간 1등 꺄

문제설명
    T개 연산카드, 1 부터 2×109 이하의 자연수 자원 카드
    연산카드
        1. 아무일 일어나지 않고 연산카드 버림
        2. acquire n: 자원 카드 획득
            n이 적힌 자원카드가 공용공간에 있으면 자신의 공간으로 가져오고 연산 카드 버림
            만약 자원크다그 누군가의 공간에 있으면 카드를 버리지 않고 재사용
        3. release n: 자연수 n이 적힌 자원 카드를 공용 공간에 반납

    누가 무슨 카드를 가지고있냐가 아니라
    이 카드를 누가 가지고있냐임!!!!!!!!!!!!!!!!!!!!!!!!
'''
import sys
from collections import deque
input = sys.stdin.readline

n, game_num = map(int, input().split())  # 사람 수, 게임횟수
who_num = list(map(lambda x: int(x) - 1, input().split()))
private_card = dict()
id_list = deque()
order_list = deque()
have_acquire = [0] * n
ans = []
for game in range(game_num):
    tmp = list(input().split())
    id, order, card = -1, -1, -1
    if len(tmp) > 2:
        id, order, card = int(tmp[0]), tmp[1], int(tmp[2])
        id_list.append(id)
        order_list.append((order, card))
    else:
        id, order = int(tmp[0]), tmp[1]
        id_list.append(id)
        order_list.append((order, 0))

for game in range(game_num):
    who = who_num[game]
    id = id_list.popleft()
    order, card = order_list.popleft()
    # 어떤 카드가 들어오든 acquire 가 있으면 그거 먼저 처리해야함.
    if have_acquire[who]:
        origin_id, origin_card = have_acquire[who]
        order_list.appendleft((order, card))
        id_list.appendleft(id)
        if origin_card not in private_card:
            # 내가 가질 수 있으면
            private_card[origin_card] = who
            ans.append(origin_id)
            have_acquire[who] = 0
        else:
            ans.append(origin_id)
            have_acquire[who] = (origin_id, origin_card)
    else:
        if order == "next":
            ans.append(id)
            continue
        elif order == "acquire":
            # 즉 남의 공용공간에 없다면.
            if card not in private_card:
                # 내가 가질 수 있으면
                private_card[card] = who
                ans.append(id)
            else:
                ans.append(id)
                have_acquire[who] = (id, card)
        else:
            private_card.pop(card)
            ans.append(id)

print('\n'.join(map(str,ans)))