# 문제
# 아래 <그림 1>과 같이 여러개의 정사각형칸들로 이루어진 정사각형 모양의 종이가 주어져 있고, 
# 각 정사각형들은 하얀색으로 칠해져 있거나 파란색으로 칠해져 있다. 
# 주어진 종이를 일정한 규칙에 따라 잘라서 다양한 크기를 가진 정사각형 모양의 하얀색 또는 파란색 색종이를 만들려고 한다.
# 전체 종이의 크기가 N×N(N=2k, k는 1 이상 7 이하의 자연수) 이라면 종이를 자르는 규칙은 다음과 같다.
# 전체 종이가 모두 같은 색으로 칠해져 있지 않으면 가로와 세로로 중간 부분을 잘라서 <그림 2>의 I, II, III, IV와 같이 
# 똑같은 크기의 네 개의 N/2 × N/2색종이로 나눈다. 
# 나누어진 종이 I, II, III, IV 각각에 대해서도 앞에서와 마찬가지로 모두 같은 색으로 칠해져 있지 않으면 
# 같은 방법으로 똑같은 크기의 네 개의 색종이로 나눈다. 이와 같은 과정을 잘라진 종이가 모두 하얀색 또는 모두 파란색으로 칠해져 있거나, 
# 하나의 정사각형 칸이 되어 더 이상 자를 수 없을 때까지 반복한다.
# 위와 같은 규칙에 따라 잘랐을 때 <그림 3>은 <그림 1>의 종이를 처음 나눈 후의 상태를, 
# <그림 4>는 두 번째 나눈 후의 상태를, <그림 5>는 최종적으로 만들어진 다양한 크기의 9장의 하얀색 색종이와 7장의 파란색 색종이를 보여주고 있다.
# 입력으로 주어진 종이의 한 변의 길이 N과 각 정사각형칸의 색(하얀색 또는 파란색)이 주어질 때 잘라진 하얀색 색종이와 파란색 색종이의 
# 개수를 구하는 프로그램을 작성하시오.
# 입력
# 첫째 줄에는 전체 종이의 한 변의 길이 N이 주어져 있다. N은 2, 4, 8, 16, 32, 64, 128 중 하나이다. 
# 색종이의 각 가로줄의 정사각형칸들의 색이 윗줄부터 차례로 둘째 줄부터 마지막 줄까지 주어진다. 
# 하얀색으로 칠해진 칸은 0, 파란색으로 칠해진 칸은 1로 주어지며, 각 숫자 사이에는 빈칸이 하나씩 있다.
# 출력
# 첫째 줄에는 잘라진 햐얀색 색종이의 개수를 출력하고, 둘째 줄에는 파란색 색종이의 개수를 출력한다.

# 예제 입력               예제 출력
# 8                     9
# 1 1 0 0 0 0 1 1       7
# 1 1 0 0 0 0 1 1
# 0 0 0 0 1 1 0 0       ※ 1 개수 출력 구현 예(4개 모두 1일 때 1로 변경)
# 0 0 0 0 1 1 0 0
# 1 0 0 0 1 1 1 1       1 0 0 1 
# 0 1 0 0 1 1 1 1       0 0 1 0  
# 0 0 1 1 1 1 1 1       0 0 1 1      0 0  
# 0 0 1 1 1 1 1 1  ->   0 1 1 1  ->  0 1  ->  0
#      2 개         <-    4 개    <-  1 개  <- 0 개
#                  4개 모두 1인 경우 제외

# 풀이
import sys

def find_square_num(1,square): # n: 색종이 색으로 1 또는 0, square: 전체 list
    tot_count = 0
    if n == 1:
        m = 0
    else:
        m = 1

    if len(square) == 1:
        if square[0][0] == 1:
            tot_count += 1
        return tot_count

    # result_square = [[]*(len(square)//2)]*(len(square)//2) # 이렇게 만들지 말 것..!
    result_square = []
    for i in range(0,len(square),2):
        line = []
        for j in range(0,len(square[i]),2):
            count = 0
            if square[i][j] == n:
                count+=1
            if square[i][j+1] == n:
                count+=1
            if square[i+1][j] == n:
                count+=1
            if square[i+1][j+1] == n:
                count+=1
            if count == 4:
                line.append(n)
                # result_square[i//2].append(n) # 이렇게 넣으면 포함하고 있는 모든 list에 다 삽입된다..(왜지..ㅠ)
            else:
                tot_count += count
                line.append(m)
                # result_square[i//2].append(m)
        result_square.append(line)
                
    tot_count += find_square_num(n,result_square)
    return tot_count

length_side = int(sys.stdin.readline())
tot_square = []
for i in range(length_side):
    color_list = list(map(int,sys.stdin.readline().split()))
    tot_square.append(color_list)
print(find_square_num(0,tot_square))
print(find_square_num(1,tot_square)) # 7

# 풀이 2 : 다른 분들 답변
from sys import stdin
n = int(stdin.readline())
matrix = [0] * n
result = []
for x in range(n):
    arr = list(map(int, stdin.readline().split()))
    matrix[x] = arr
#         n * n
#     x,y 0 0 0      x,y+n/2 0 0 0
#       0 0 0 0            0 0 0 0
#       0 0 0 0            0 0 0 0
#       0 0 0 0            0 0 0 0
# x+n/2,y 0 0 0  x+n/2,y+n/2 0 0 0
#       0 0 0 0            0 0 0 0
#       0 0 0 0            0 0 0 0
#       0 0 0 0            0 0 0 0
def foo(x,y,n):
    color = matrix[x][y]
    for a in range(x, x+n):
        for b in range(y, y+n):
            if color != matrix[a][b]:
                foo(x, y, n//2)
                foo(x, y + n//2, n//2)
                foo(x + n//2, y, n//2)
                foo(x + n//2, y + n//2, n//2)
                return
    if color == 0:
        result.append(0)
    else:
        result.append(1)
foo(0,0,n)
print(result.count(0))
print(result.count(1))