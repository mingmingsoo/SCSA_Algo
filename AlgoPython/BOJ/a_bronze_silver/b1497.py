'''
[문제설명]
    기타를 선택해서 최대 많은 곡을 낼 수 있다면
    필요한 기타 갯수를 출력

[입력]
    기타 이름과 연주 유무
[출력]
    최대 많은 곡 중 필요한 최소 기타 갯수
[구상]
    기타 부분집합.. 해야하지 않을까요..?
[백트래킹]
    만약 선택한게 1인데 전부 연주할 수 있으면
    1출력해버리고 return
'''
import heapq

n, songs = map(int, input().split())
isSong = [[False]* songs for i in range(n)]
for i in range(n):
    name, tmp = input().split()
    for j in range(len(tmp)):
        if(tmp[j]=="Y"):
            isSong[i][j] = True
# print(isSong)
sel = [0]*n
q = []

def subset(idx):
    global isok, total_tar
    if(idx ==n):
        song_list = [False]*songs
        # 기타갯수는?
        ele_tar = 0
        for tar in sel:
            if(tar==1):
                ele_tar+=1

        for i in range(len(sel)):
            if(sel[i]==1): # 0001 i가 3
                for j in range(songs):
                    if(isSong[i][j]):
                        song_list[j] = True

        ele_ok = 0
        for ok in song_list:
            if(ok):
                ele_ok+=1
        heapq.heappush(q,(-ele_ok, ele_tar))
        # if(ele_ok==5):
        #     print(song_list)
        #     print(sel, ele_tar)
        return
    sel[idx] = 0
    subset(idx+1)
    sel[idx] = 1
    subset(idx+1)

subset(0)
ans = heapq.heappop(q)[1]
if(ans==0):
    print(-1)
else:
    print(ans)
