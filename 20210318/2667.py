# 문제
# <그림 1>과 같이 정사각형 모양의 지도가 있다. 1은 집이 있는 곳을, 0은 집이 없는 곳을 나타낸다. 
# 철수는 이 지도를 가지고 연결된 집의 모임인 단지를 정의하고, 단지에 번호를 붙이려 한다. 
# 여기서 연결되었다는 것은 어떤 집이 좌우, 혹은 아래위로 다른 집이 있는 경우를 말한다. 
# 대각선상에 집이 있는 경우는 연결된 것이 아니다. <그림 2>는 <그림 1>을 단지별로 번호를 붙인 것이다. 
# 지도를 입력하여 단지수를 출력하고, 각 단지에 속하는 집의 수를 오름차순으로 정렬하여 출력하는 프로그램을 작성하시오.
# 입력
# 첫 번째 줄에는 지도의 크기 N(정사각형이므로 가로와 세로의 크기는 같으며 5≤N≤25)이 입력되고, 그 다음 N줄에는 각각 N개의 자료(0혹은 1)가 입력된다.
# 출력
# 첫 번째 줄에는 총 단지수를 출력하시오. 그리고 각 단지내 집의 수를 오름차순으로 정렬하여 한 줄에 하나씩 출력하시오.
# 입력 예      출력 예
# 7           3
# 0110100     7
# 0110101     8
# 1110101     9
# 0000111
# 0100000
# 0111110
# 0111000

# 풀이 2: 단지를 구분해야 하므로 DFS가 더 어울리는 문제라고 생각한다.
# 예상 순서 : 1을 찾는다 -> 첫 번째 찾은 1부터 DFS로 따라 들어가며 숫자를 2로 바꾼다.
#         -> 다 바꿨다면 다시 1을 찾는다 -> 이번엔 3으로 바꿔본다. -> 더이상 1이 없을 때까지 반복
import sys
N = int(sys.stdin.readline())
tot_list = [list(map(int,input())) for _ in range(N)]
houses = [] # to_visit의 역할

complex_num = 2 # 0,1 로 구성되어 있으니 2부터 번호 메겨줌
for i in range(N):
    for j in range(N):
        if tot_list[i][j] == 1:
            houses.append([i,j])
            # DFS 시작
            while houses:
                # 첫번째 방문할 곳을 pop() 하고 그 숫자를 2로 바꿔줌
                row,col = houses.pop()
                tot_list[row][col] = complex_num
                # 방문하는 집의 좌우상하 구현을 준비
                dx = [1,-1,0,0] # [x+1][y],[x-1][y],[x][y+1],[x][y-1] 조작을 위함
                dy = [0,0,1,-1]
                for k in range(4):
                    _row = row + dx[k]
                    _col = col + dy[k]
                    if 0<=_row < N and 0<=_col < N and tot_list[_row][_col] == 1:
                        houses.append([_row,_col])
            complex_num+=1 # 단지 별로 숫자를 달리 해주기 위해 +=1 을 해준다.
            # DFS 끝~~
    
result = {} # 단지 별 집의 빈도수를 기록하기 위한 dictionary
count = 0
for i in tot_list:
    for j in i:
        if j not in result and j != 0:
            result[j] = 1
        elif j in result and j != 0:
            result[j] += 1
fre_list = sorted(result.values()) # 집의 수 오름차순 출력을 위한 정렬
print(len(result)) # 총 단지 수 출력
for i in fre_list: # 단지 별 집의 수 출력
    print(i)

# 풀이 1: 단지를 구분해야 하므로 DFS가 더 어울리는 문제라고 생각한다.
# 예상 순서 : 1을 찾는다 -> 첫 번째 찾은 1부터 DFS로 따라 들어가며 숫자를 2로 바꾼다.
#         -> 다 바꿨다면 다시 1을 찾는다 -> 이번엔 3으로 바꿔본다. -> 더이상 1이 없을 때까지 반복
# 문제점 : 단지 수가 줄의 수를 넘어가는 부분을 캐치 못함, 2중 for 문에서 i가 for문 속에 여러개인 경우 캐치 못함
# import sys
# N = int(sys.stdin.readline())
# tot_list = [list(map(int,input())) for _ in range(N)]
# # 2차원 배열 생성
# houses = [] # to_visit의 역할

# complex_num = 2 # 0,1 로 구성되어 있으니 2부터 번호 메겨줌
# for i in range(N):
#     for j in range(N):
#         if tot_list[i][j] == 1:
#             houses.append([i,j])
#             # break # 하나를 찾으면 아래에서 DFS를 실행하기 위해 break를 걸어줌 # 반례 : 줄의 길이를 넘어가는 수의 단지일 경우 i를 넘어가게 되어 for 문을 끊으면 안된다.
#     # DFS 시작
#     while houses:
#         # 첫번째 방문할 곳을 pop() 하고 그 숫자를 2로 바꿔줌
#         row,col = houses.pop()
#         tot_list[row][col] = complex_num
#         # 방문하는 집의 좌우상하 구현을 준비
#         dx = [1,-1,0,0] # [x+1][y],[x-1][y],[x][y+1],[x][y-1] 조작을 위함
#         dy = [0,0,1,-1]
#         for i in range(4):
#             _row = row + dx[i]
#             _col = col + dy[i]
#             if 0<=_row and _row< N and 0<=_col and _col < N and tot_list[_row][_col] == 1:
#                 houses.append([_row,_col])
#     complex_num+=1 # 단지 별로 숫자를 달리 해주기 위해 +=1 을 해준다.
#             # DFS 끝~~
    
# result = {} # 단지 별 집의 빈도수를 기록하기 위한 dictionary
# count = 0
# for i in tot_list:
#     for j in i:
#         if j not in result and j != 0:
#             result[j] = 1
#         elif j in result and j != 0:
#             result[j] += 1
# fre_list = sorted(result.values()) # 집의 수 오름차순 출력을 위한 정렬
# print(len(result)) # 총 단지 수 출력
# for i in fre_list: # 단지 별 집의 수 출력
#     print(i)
