# 문제
# 철수의 토마토 농장에서는 토마토를 보관하는 큰 창고를 가지고 있다. 
# 토마토는 아래의 그림과 같이 격자 모양 상자의 칸에 하나씩 넣어서 창고에 보관한다. 
# 창고에 보관되는 토마토들 중에는 잘 익은 것도 있지만, 아직 익지 않은 토마토들도 있을 수 있다. 
# 보관 후 하루가 지나면, 익은 토마토들의 인접한 곳에 있는 익지 않은 토마토들은 익은 토마토의 영향을 받아 익게 된다. 
# 하나의 토마토의 인접한 곳은 왼쪽, 오른쪽, 앞, 뒤 네 방향에 있는 토마토를 의미한다. 
# 대각선 방향에 있는 토마토들에게는 영향을 주지 못하며, 토마토가 혼자 저절로 익는 경우는 없다고 가정한다. 
# 철수는 창고에 보관된 토마토들이 며칠이 지나면 다 익게 되는지, 그 최소 일수를 알고 싶어 한다.
# 토마토를 창고에 보관하는 격자모양의 상자들의 크기와 익은 토마토들과 익지 않은 토마토들의 정보가 주어졌을 때, 
# 며칠이 지나면 토마토들이 모두 익는지, 그 최소 일수를 구하는 프로그램을 작성하라. 
# 단, 상자의 일부 칸에는 토마토가 들어있지 않을 수도 있다.
# 입력
# 첫 줄에는 상자의 크기를 나타내는 두 정수 M,N이 주어진다. M은 상자의 가로 칸의 수, N은 상자의 세로 칸의 수를 나타낸다. 
# 단, 2 ≤ M,N ≤ 1,000 이다. 둘째 줄부터는 하나의 상자에 저장된 토마토들의 정보가 주어진다. 
# 즉, 둘째 줄부터 N개의 줄에는 상자에 담긴 토마토의 정보가 주어진다. 
# 하나의 줄에는 상자 가로줄에 들어있는 토마토의 상태가 M개의 정수로 주어진다. 
# 정수 1은 익은 토마토, 정수 0은 익지 않은 토마토, 정수 -1은 토마토가 들어있지 않은 칸을 나타낸다.
# 토마토가 하나 이상 있는 경우만 입력으로 주어진다.
# 출력
# 여러분은 토마토가 모두 익을 때까지의 최소 날짜를 출력해야 한다. 
# 만약, 저장될 때부터 모든 토마토가 익어있는 상태이면 0을 출력해야 하고, 토마토가 모두 익지는 못하는 상황이면 -1을 출력해야 한다.

# 풀이 2: 다른 사람 풀이 참고 후 재작성(21.03.18)
from collections import deque # BFS 활용을 위해 queue 사용
M,N = map(int,input().split())
tot_boxes = [list(map(int,input().split())) for _ in range(N)]

to_visit = deque([])
for i in range(N): # 현재 익어있는 토마토를 to_visit에 넣어준다.(들러서 주변 애들 익힐 예정)
    for j in range(M):
        if tot_boxes[i][j] == 1:
            to_visit.append([i,j])

dx = [1,-1,0,0] # 좌우상하에 있는 토마토들을 확인하기 위한 좌표 +,- 설정
dy = [0,0,1,-1]

while to_visit:
    row, col = to_visit.popleft() # 이와 같은 방식으로 [row,col] 값을 빼낼 수 있다.

    for i in range(4): # 좌우 상하에 대한 반복문(코드가 엄청 보기 좋아진다.)
        _row = row + dx[i]
        _col = col + dy[i]

        if 0<=_row < N and 0<=_col < M and tot_boxes[_row][_col] == 0: # indexError 방지를 위함과 덜익은 토마토 확인 조건문
            tot_boxes[_row][_col] = tot_boxes[row][col] + 1 # 덜 익어있으면 익은 토마토보다 +1하여 저장한다.(단계를 구분하기 위함)
            to_visit.append([_row,_col]) # to_visit에 넣어줘 다음 단계를 밟을 수 있게 함

result = -2 # 단계를 구분할 때 비교값. 토마토가 들어있지 않은 경우 -1 이므로 -2를 넣어줌
check_tot = False # 아직 덜 익은 토마토가 박스에 남아있는지 확인하기 위함
for i in tot_boxes: # 토마토 박스에 덜익은 토마토가 있는지 확인하고, 없을 시 최대 단계가 몇단계인지 확인
    for j in i:
        if j == 0:
            check_tot = True
        elif j > result:
            result = j
       

if check_tot == True: # 덜 익은 토마토(0)가 있는 경우 -1 반환
    print(-1)
elif result == -1: # 모든 수가 -1인 경우를 대비하여 별도 조건문 만들어 줌
    print(0)
else: # 1단계 : 2 , 2단계 : 3 , ... 순서로 들어가므로 1 빼주고 출력
    print(result-1)


# 풀이 1: 실패(정확한 방법에 대해 아예 감을 잡지 못함)
# import sys

# tomatoes = {

# }
# ready = []
# empty = []
# def days_tomatoes_all_ready():
#     to_ready = ready
#     count = 0
#     while to_ready:
#         one_cycle = len(to_ready)
#         for tom in range(one_cycle):            
#             x,y = map(int,to_ready.pop(0).split('_'))
#             line_tot[x][y] = 1
#             if line_tot[x+1][y] != None and line_tot[x+1][y] == 0:
#                 to_ready.append(str(x+1)+"_"+str(y))
#             if line_tot[x-1][y] != None and line_tot[x-1][y] == 0:
#                 to_ready.append(str(x-1)+"_"+str(y))
#             if line_tot[x][y+1] != None and line_tot[x][y+1] == 0:
#                 to_ready.append(str(x)+"_"+str(y+1))
#             if line_tot[x][y-1] != None and line_tot[x][y-1] == 0:
#                 to_ready.append(str(x)+"_"+str(y-1))    
#         count += 1
#     return count    
            
# M,N = map(int,sys.stdin.readline().split())
# line_tot = []
# for i in range(N):
#     line = list(map(int,sys.stdin.readline().split()))
#     line_tot.append(line)
# for i in range(M):
#     for j in range(N):
#         if line_tot[i][j] == 1:
#             ready.append(str(i)+"_"+str(j))
#         elif line_tot[i][j] == -1:
#             empty.append(str(i)+"_"+str(j))

# print(days_tomatoes_all_ready())

# 풀이 : 다른 사람 풀이(이를 통해 BFS를 이해해보자.) ↓↓↓아래 코드의 과정↓↓↓
# 6 4
# 0 -1 0 0      0 -1 0 0      0 -1 0 0      0 -1 0 4      0 -1 5 4  결과 : 0이 있네.-> True -> -1 출력
# -1 0 0 0  ->  -1 0 0 0  ->  -1 0 0 3  ->  -1 0 4 3  ->  -1 5 4 3
# 0 0 0 0       0 0 0 2       0 0 3 2       0 4 3 2       5 4 3 2
# 0 0 0 1       0 0 2 1       0 3 2 1       4 3 2 1       4 3 2 1

from collections import deque # BFS 에 유리한 queue 사용을 위한 collections import

M, N = map(int, input().split()) # 입력을 받는다. M : 상자의 가로 칸 수, N : 상자의 세로 칸 수
tots = [list(map(int, input().split())) for _ in range(N)] # 각 줄의 상자들을 입력 받는다.
queue = deque() # to_visit 의 개념으로 현재 이미 익어있는 토마토의 좌표를 먼저 저장하고 향후 새로 익은 토마토를 추가로 넣어줄 용도

for i in range(N): # 이미 익어있는 토마토들에 우선 방문하기 위해 좌표 list [i,j]를 append 해준다.
    for j in range(M):
        if tots[i][j] == 1:
            queue.append([i, j])

# 상하좌우 체크를 위한 x,y 좌표에 더해줄 값 list ★★★★★, BFS 하려면 모르면 안될 내용일듯.(코드가 엄청 깔끔해진다.)         
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

# 여기부터 bfs
while queue:
    row, col = queue.popleft() # 익어있는(1) 토마토에 방문하기 위해 popleft(). ★list [row,col]을 좌측과 같이 받을 수 있다.★
    
    for k in range(4):
        _row = row + dy[k]     # 익어있는 토마토 상하좌우(dx,dy)를 확인하기 위한 변수 _row, _col
        _col = col + dx[k]
        
        # 안익은게 있다면, 익은 것으로 바꿔준다.
        if 0 <= _row < N and 0 <= _col < M and tots[_row][_col] == 0: # indexError 방지를 위한 조건 과 안익은 토마토인지 확인하는 조건
            tots[_row][_col] = tots[row][col] + 1 # 안 익은 토마토를 익은 토마토로 바꿔 준다.(단계 표현을 위해 + 1 해준다. 첫 날:2,둘 째 날:3, ..)
            queue.append([_row, _col]) # 이제 익은 토마토를 향후에 방문하기 위해 큐에 넣어 준다.
# bfs 끝------

result = -2 # -1이 존재해서 -2 값으로 비교

check_tot = False # 안익은게 있는지 체크하기 위한 bool 변수

for i in tots: # tots list 안에 있는 list들의 변수 i
    for j in i: # tots list 안에 i list 안에 원소들의 변수 j
        if(j == 0): # 남아있는 원소들 중 0이 있으면
            check_tot = True # True로 변경
        result = max(result, j) # j가 1인 경우에는??
        
if check_tot: # 남아있는 원소들 중에 0이 있는 경우 
    print(-1)
elif result == -1: # 처음부터 모두 -1일 때를 대비한 조건
    print(0)
else: 
    print(result - 1) # 모두 익은 상황이면 제일 큰 숫자에서 -1 (첫 날 모두 익어있는 상태라면 1이 최대값이므로, 첫 날 익은 토마토에 숫자 2 넣어주므로)