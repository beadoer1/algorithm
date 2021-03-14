# 하노이 탑 분류
# 문제
# 세 개의 장대가 있고 첫 번째 장대에는 반경이 서로 다른 n개의 원판이 쌓여 있다. 각 원판은 반경이 큰 순서대로 쌓여있다. 
# 이제 수도승들이 다음 규칙에 따라 첫 번째 장대에서 세 번째 장대로 옮기려 한다.
#   한 번에 한 개의 원판만을 다른 탑으로 옮길 수 있다.
#   쌓아 놓은 원판은 항상 위의 것이 아래의 것보다 작아야 한다.
# 이 작업을 수행하는데 필요한 이동 순서를 출력하는 프로그램을 작성하라. 단, 이동 횟수는 최소가 되어야 한다.
# 입력
# 첫째 줄에 첫 번째 장대에 쌓인 원판의 개수 N (1 ≤ N ≤ 100)이 주어진다.
# 출력
# 첫째 줄에 옮긴 횟수 K를 출력한다.
# N이 20 이하인 입력에 대해서는 두 번째 줄부터 수행 과정을 출력한다. 두 번째 줄부터 K개의 줄에 걸쳐 두 정수 A B를 빈칸을 사이에 두고 출력하는데, 
# 이는 A번째 탑의 가장 위에 있는 원판을 B번째 탑의 가장 위로 옮긴다는 뜻이다. N이 20보다 큰 경우에는 과정은 출력할 필요가 없다.

# 풀이
# 반복 절차 (함수)
# def move_plate_odd(num): # 홀짝이 바뀌는 번호가 다름, 앞으로 한 칸 돼서 다음에 들어가고, 뒤로 한 칸 돼서 그 다음에 들어감
#     if num <= 1:
#         a = [[1, 3]]
#         return a
#     elif num % 2 == 0: # even
#         receive_move_plate = move_plate_odd(num-1)
#         next_step_of_move_plate = [[1, 2]]+change_value_left(move_plate_odd(num-1))
#         total_move_plate = receive_move_plate + next_step_of_move_plate
#         return total_move_plate
#     else:              # odd
#         receive_move_plate = move_plate_odd(num-1)
#         next_step_of_move_plate = [[1, 3]]+change_value_right(move_plate_odd(num-1))
#         total_move_plate = receive_move_plate + next_step_of_move_plate
#         return total_move_plate

# def move_plate_even(num):      
#     if num <= 1:
#         a = [[1, 2]]
#         return a
#     elif num % 2 == 0: # even
#         receive_move_plate = move_plate_even(num-1)
#         next_step_of_move_plate = [[1, 3]]+change_value_right(move_plate_even(num-1))
#         total_move_plate = receive_move_plate + next_step_of_move_plate
#         return total_move_plate
#     else:              # odd
#         receive_move_plate = move_plate_even(num-1)
#         next_step_of_move_plate = [[1, 2]]+change_value_left(move_plate_even(num-1))
#         total_move_plate = receive_move_plate + next_step_of_move_plate
#         return total_move_plate            

# def change_value_left(arrays):
#     for index in range(len(arrays)):
#         for i in range(2):
#             if arrays[index][i] == 1:
#                 arrays[index][i] += 2
#             else:
#                 arrays[index][i] -= 1
#     return arrays

# def change_value_right(arrays):
#     for array in arrays:
#         for i in range(2):
#             if array[i] == 3:
#                 array[i] -= 2
#             else:
#                 array[i] += 1
#     return arrays

# # 프로그램 실행
# num_of_plate = int(input()) # 입력

# # 총 반복 횟수 출력
# total_cycle = 0
# for one_of_plate in range(num_of_plate):
#     total_cycle += 2**one_of_plate
# print(total_cycle)

# # 20 이하 반복 절차
# if num_of_plate <= 20:
#     if num_of_plate % 2 != 0:
#         result_of_move_plate = move_plate_odd(num_of_plate)
#     else:
#         result_of_move_plate = move_plate_even(num_of_plate)
#     for move_plate in result_of_move_plate:
#         print(move_plate[0],move_plate[1])

# 풀이 2 : 다른 사람 풀이 참고(이게 의도에 맞는 풀이 방법이라고 생각한다.)
# -> 재귀를 이용 -> n개의 탑을 a에서 c로 옮긴다 -> move_plate(n,a,b,c) 
def move_plate(n,a,b,c):
    if n == 1:
        print(a,c)
    else:
        move_plate(n-1,a,c,b)
        print(a,c)
        move_plate(n-1,b,a,c)

num = int(input())

total_cycle = 2**num-1
print(total_cycle)

if num <= 20:
    move_plate(num,1,2,3)
