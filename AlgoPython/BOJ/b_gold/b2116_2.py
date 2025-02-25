'''
세번째 풀이
    max값 나오면 break
두번째 풀이
    굳이 재귀안타고 내가 할 수 있는 선에서 다시 풀어보기
문제설명
    주사위를 쌓을 수 있는 모든 경우의 수에서 옆면의 최댓값을 구해라
구상
    1. 맨 밑에 뭘 쌓을지 정한다
        - >어느면이 윗면이 될지는 경우의 수 6개
        -> 그러면 나머지는 맞춰가야하는거라 정해짐
'''

n = int(input())
dice = [list(map(int, input().split())) for i in range(n)]
final_max = n*6
maxi = 0

index_list = [5,3,4,1,2,0]

def find_maxi(idx,top_idx,bottom_idx):
    face = 0
    for i in range(6):
        if i!= top_idx and i!=bottom_idx:
            face = max(face, dice[idx][i])
    return face


for i in range(6):
    top = dice[0][i]  # 윗면
    bottom = dice[0][index_list[i]]
    face_maxi = find_maxi(0,i,index_list[i])

    for j in range(1,n): # 다음 주사위들
        next_bottom = top
        next_bottom_idx = dice[j].index(next_bottom)
        next_top_idx = index_list[next_bottom_idx]
        next_top = dice[j][next_top_idx]
        face_maxi += find_maxi(j,next_top_idx, next_bottom_idx)
        top = next_top
        bottom = next_bottom

    maxi = max(maxi, face_maxi)
    if(maxi==find_maxi):
        break

print(maxi)
