'''
풀이시간
    26분
문제설명
    카드가 주어졌을 때, 합 / 결이 맞는지 판단해라
입력
    카드 정보
    합결 정보
조건
    합: 합 이면서 이전에 외친적없는 그림 조합이면 +1 아니면 -1 -> visited 필요
    결: 더이상 남은 합이 없을 때 결을 외침 -> 맞으면 3 아니면 -1
구상
    먼저 가능한 카드 조합을 answer_set에 담야아함..
    visited 필요함
    가능한 조합은 완탐

'''

card_list = []  # 모두 다른 조합이기에 set 가능인데 일단 lst -> 조회해야되서 안될듯

for i in range(9):
    card_list.append((tuple(input().split())))

hap_list = []  # 합이 될 수 있는 애들 미리 구하기
for i in range(9):
    for j in range(i + 1, 9):
        for w in range(j + 1, 9):
            a1, b1, c1 = card_list[i]
            a2, b2, c2 = card_list[j]
            a3, b3, c3 = card_list[w]

            # 모두 같을 떄
            if a1 == a2 == a3 and b1 == b2 == b3 and c1 == c2 == c3:
                hap_list.append((i + 1, j + 1, w + 1))

            # 2개 같고 1개 다를때
            elif a1 == a2 == a3 and b1 == b2 == b3 and (c1 != c2) and (c2 != c3) and (c1 != c3):
                hap_list.append((i + 1, j + 1, w + 1))
            elif a1 == a2 == a3 and c1 == c2 == c3 and (b1 != b2) and (b2 != b3) and (b1 != b3):
                hap_list.append((i + 1, j + 1, w + 1))
            elif b1 == b2 == b3 and c1 == c2 == c3 and (a1 != a2) and (a2 != a3) and (a1 != a3):
                hap_list.append((i + 1, j + 1, w + 1))

            # 1개 같고 2개 다를 때
            elif a1 == a2 == a3 and (b1 != b2) and (b2 != b3) and (b1 != b3) and (c1 != c2) and (c2 != c3) and (
                    c1 != c3):
                hap_list.append((i + 1, j + 1, w + 1))
            elif b1 == b2 == b3 and (a1 != a2) and (a2 != a3) and (a1 != a3) and (c1 != c2) and (c2 != c3) and (
                    c1 != c3):
                hap_list.append((i + 1, j + 1, w + 1))
            elif c1 == c2 == c3 and (a1 != a2) and (a2 != a3) and (a1 != a3) and (b1 != b2) and (b2 != b3) and (
                    b1 != b3):
                hap_list.append((i + 1, j + 1, w + 1))

            # 모두 다를 때
            elif (c1 != c2) and (c2 != c3) and (c1 != c3) and (a1 != a2) and (a2 != a3) and (a1 != a3) and (
                    b1 != b2) and (b2 != b3) and (b1 != b3):
                hap_list.append((i + 1, j + 1, w + 1))

score = 0  # 출력할 점수
visited = set()  # visited 관리
order = int(input())  # 부를 숫자
isKyul = False  # 결 성공 여부

for o in range(order):
    tmp = list(input().split())
    if tmp[0] == "H":
        number_list = [int(tmp[1]), int(tmp[2]), int(tmp[3])]
        number_list.sort()  # 동일여부를 확인하기 위해 sort

        if (number_list[0], number_list[1], number_list[2]) in hap_list:
            if (number_list[0], number_list[1], number_list[2]) not in visited:
                # 합이 맞고, 부른 적 없다면
                visited.add((number_list[0], number_list[1], number_list[2]))  # 방문처리
                score += 1  # 점수 +
            else:
                score -= 1  # 그게 아니면 점수 -
        else:
            score -= 1  # 그게 아니면 점수 -
    else:
        if len(visited) == len(hap_list) and not isKyul:
            # visited가 다 불려서 합리스트만큼 채워졌으면, 그리고 결성공한적 없으면
            score += 3  # 점수 += 3
            isKyul = True  # 결 처리
        else:
            score -= 1  # 아니면 점수 -
print(score)
