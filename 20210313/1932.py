# 문제
#         7
#       3   8
#     8   1   0
#   2   7   4   4
# 4   5   2   6   5
# 위 그림은 크기가 5인 정수 삼각형의 한 모습이다.
# 맨 위층 7부터 시작해서 아래에 있는 수 중 하나를 선택하여 아래층으로 내려올 때, 
# 이제까지 선택된 수의 합이 최대가 되는 경로를 구하는 프로그램을 작성하라. 
# 아래층에 있는 수는 현재 층에서 선택된 수의 대각선 왼쪽 또는 대각선 오른쪽에 있는 것 중에서만 선택할 수 있다.
# 삼각형의 크기는 1 이상 500 이하이다. 삼각형을 이루고 있는 각 수는 모두 정수이며, 범위는 0 이상 9999 이하이다.
# 입력
# 첫째 줄에 삼각형의 크기 n(1 ≤ n ≤ 500)이 주어지고, 둘째 줄부터 n+1번째 줄까지 정수 삼각형이 주어진다.
# 출력
# 첫째 줄에 합이 최대가 되는 경로에 있는 수의 합을 출력한다.

# 풀이 : 이거라도 재귀로 풀어보자
import sys
memo = {}
def find_max_sum(i_n,i_l,tot_array):
    if i_l == 0:
        return tot_array[i_l][i_n]
    elif (i_n,i_l) in memo:
        return memo[(i_n,i_l)]
    elif i_n == 0 or i_n ==len(tot_array[i_l])-1:
        if i_n == 0:
            result = tot_array[i_l][i_n] + find_max_sum(i_n,i_l-1,tot_array)
            memo[(i_n,i_l)] = result
            return result
        else:
            result = tot_array[i_l][i_n] + find_max_sum(i_n-1,i_l-1,tot_array)
            memo[(i_n,i_l)] = result
            return result
    else:
        if find_max_sum(i_n-1,i_l-1,tot_array) > find_max_sum(i_n,i_l-1,tot_array):
            result = tot_array[i_l][i_n] + find_max_sum(i_n-1,i_l-1,tot_array)
            memo[(i_n,i_l)] = result
            return result
        else:
            result = tot_array[i_l][i_n] + find_max_sum(i_n,i_l-1,tot_array)
            memo[(i_n,i_l)] = result
            return result

num_lines = int(sys.stdin.readline())
line_list = []
for i in range(num_lines):
    line = list(map(int,sys.stdin.readline().split()))
    line_list.append(line)
max_sum = 0
for j in range(len(line_list)):
    sum_num = find_max_sum(j,len(line_list)-1,line_list)
    if sum_num > max_sum:
        max_sum = sum_num
print(max_sum)

# 풀이 2 : 프로그래머스 level 3 수준 이라는...
# loop = int(input())
# arr = []
# for x in range(loop):
#     layer = list(map(int, input().split()))
#     arr.append(layer)
#         7
#       10 15
#     18  16  15
#   2   7   4   4
# 4    5   2   6   5
# for x in range(1, len(arr)):
#     for y in range(x+1):
#         # 왼쪽
#         if y == 0:
#             arr[x][y] += arr[x-1][y]
#         elif y == x: # 오른쪽
#             arr[x][y] += arr[x-1][-1]
#         else: # 빈공간
#             arr[x][y] += max(arr[x-1][y-1], arr[x-1][y])
# print(max(arr[-1]))
