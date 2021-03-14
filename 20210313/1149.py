# 문제
# RGB거리에는 집이 N개 있다. 거리는 선분으로 나타낼 수 있고, 1번 집부터 N번 집이 순서대로 있다.
# 집은 빨강, 초록, 파랑 중 하나의 색으로 칠해야 한다. 각각의 집을 빨강, 초록, 파랑으로 칠하는 비용이 주어졌을 때, 
# 아래 규칙을 만족하면서 모든 집을 칠하는 비용의 최솟값을 구해보자.
# 1번 집의 색은 2번 집의 색과 같지 않아야 한다.
# N번 집의 색은 N-1번 집의 색과 같지 않아야 한다.
# i(2 ≤ i ≤ N-1)번 집의 색은 i-1번, i+1번 집의 색과 같지 않아야 한다.
# 입력
# 첫째 줄에 집의 수 N(2 ≤ N ≤ 1,000)이 주어진다. 
# 둘째 줄부터 N개의 줄에는 각 집을 빨강, 초록, 파랑으로 칠하는 비용이 1번 집부터 한 줄에 하나씩 주어진다. 
# 집을 칠하는 비용은 1,000보다 작거나 같은 자연수이다.
# 출력
# 첫째 줄에 모든 집을 칠하는 비용의 최솟값을 출력한다.

# 풀이 : '틀렸습니다.' ㅠ,.ㅠ
# import sys
# def find_min_cost(rgb_in,house_array):
#     first_cost = house_array[0][rgb_in]
#     min_cost = first_cost
#     for i in range(1,len(house_array)):
#         if rgb_in == 0:
#             rgb_in1 = 1
#             rgb_in2 = 2
#         elif rgb_in == 1:
#             rgb_in1 = 2
#             rgb_in2 = 0
#         else:
#             rgb_in1 = 0
#             rgb_in2 = 1
            
#         if house_array[i][rgb_in1] > house_array[i][rgb_in2]:
#             min_cost += house_array[i][rgb_in2]
#             rgb_in = rgb_in2
#         else:
#             min_cost += house_array[i][rgb_in1]
#             rgb_in = rgb_in1
#     return min_cost

# N = int(sys.stdin.readline())
# total_list = []
# for i in range(N):
#     rgb_list = list(map(int,sys.stdin.readline().split()))
#     total_list.append(rgb_list)
# cost_min_0 = find_min_cost(0,total_list)
# cost_min_1 = find_min_cost(1,total_list)
# cost_min_2 = find_min_cost(2,total_list)
# if cost_min_0 < cost_min_1 and cost_min_0 < cost_min_2:
#     print(cost_min_0)
# elif cost_min_1 < cost_min_0 and cost_min_1 < cost_min_0:
#     print(cost_min_1)
# else:
#     print(cost_min_2)

# 풀이 2 : 재귀로 풀어보자. -> 시간초과 발생,  필요하면 동적계획법 넣고. -> 런타임 에러 발생
# 백준에서는 깊이가 1000개 이상이 되면 런타임 에러가 발생한다. 아마 이런 이유로 런타임 에러가 발생한 듯 하다.
# 입력값 기준이 2 <= N <= 1000 인 이유가 재귀를 사용하지 말라는데 있나보다..
# => import를 안넣고 돌렸었다...다시 해보니 그냥 틀린 답이다.
import sys

memo = {}

def find_min_cost(i,num,array_tot):
    # 3가지 index를 정의
    if i == 0:
        j = 1
        k = 2
    elif i == 1:
        j = 2
        k = 0
    else:
        j = 0
        k = 1
    # tot_list에서 0번째(처음)에 다다르면 각 값을 회신
    if num == 0:
        if array_tot[0][j] < array_tot[0][k]:
            return array_tot[0][j]
        else:
            return array_tot[0][k]
    # memo 안에 미리 저장된 key가 있는 경우 그 value를 바로 반환
    elif (i,num)in memo:
        return memo[(i,num)]
    # 재귀 함수_ 맨 마지막 집에서 선택 시 앞 집까지는 이미 최소합이라는 가정
    else:
        if find_min_cost(j,num-1,array_tot) < find_min_cost(k,num-1,array_tot):
            result = array_tot[num][i] + find_min_cost(j,num-1,array_tot)
            memo[(i,num)] = result
            return result
        else:
            result = array_tot[num][i] + find_min_cost(k,num-1,array_tot)
            memo[(i,num)] = result
            return result    

tot_list = []
N = int(sys.stdin.readline())
for i in range(N):
    rgb_list = list(map(int,sys.stdin.readline().split()))
    tot_list.append(rgb_list)

min_cost_in_0 = find_min_cost(0,len(tot_list)-1,tot_list)
min_cost_in_1 = find_min_cost(1,len(tot_list)-1,tot_list)
min_cost_in_2 = find_min_cost(2,len(tot_list)-1,tot_list)

if min_cost_in_0 <= min_cost_in_1 and min_cost_in_0 <= min_cost_in_2:
    print(min_cost_in_0)
elif min_cost_in_1 <= min_cost_in_2 and min_cost_in_1 <= min_cost_in_0:
    print(min_cost_in_1)
else:
    print(min_cost_in_2)


# 풀이 3_정찬엽 님
# 재귀 문제 -> for문 풀이 짚고 넘어가자.
# 3
# 26 40 83
# 89 86 83
# 96 172 188
loop = int(input())
arr = [0 for x in range(loop+1)]
for x in range(1, loop+1):
    arr[x] = list(map(int, input().split())) # [0][1][2]
#print(arr)
for x in range(2, loop+1):
    arr[x][0] = arr[x][0] + min(arr[x-1][1], arr[x-1][2])
    arr[x][1] = arr[x][1] + min(arr[x-1][0], arr[x-1][2])
    arr[x][2] = arr[x][2] + min(arr[x-1][0], arr[x-1][1])
print(arr)    
#print(min(arr[loop][0], arr[loop][1], arr[loop][2]))
