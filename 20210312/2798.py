# 문제
# 카지노에서 제일 인기 있는 게임 블랙잭의 규칙은 상당히 쉽다. 카드의 합이 21을 넘지 않는 한도 내에서, 
# 카드의 합을 최대한 크게 만드는 게임이다. 블랙잭은 카지노마다 다양한 규정이 있다.
# 한국 최고의 블랙잭 고수 김정인은 새로운 블랙잭 규칙을 만들어 상근, 창영이와 게임하려고 한다.
# 김정인 버전의 블랙잭에서 각 카드에는 양의 정수가 쓰여 있다. 
# 그 다음, 딜러는 N장의 카드를 모두 숫자가 보이도록 바닥에 놓는다. 그런 후에 딜러는 숫자 M을 크게 외친다.
# 이제 플레이어는 제한된 시간 안에 N장의 카드 중에서 3장의 카드를 골라야 한다. 
# 블랙잭 변형 게임이기 때문에, 플레이어가 고른 카드의 합은 M을 넘지 않으면서 M과 최대한 가깝게 만들어야 한다.
# N장의 카드에 써져 있는 숫자가 주어졌을 때, M을 넘지 않으면서 M에 최대한 가까운 카드 3장의 합을 구해 출력하시오.
# 입력
# 첫째 줄에 카드의 개수 N(3 ≤ N ≤ 100)과 M(10 ≤ M ≤ 300,000)이 주어진다. 
# 둘째 줄에는 카드에 쓰여 있는 수가 주어지며, 이 값은 100,000을 넘지 않는 양의 정수이다.
# 합이 M을 넘지 않는 카드 3장을 찾을 수 있는 경우만 입력으로 주어진다.
# 출력
# 첫째 줄에 M을 넘지 않으면서 M에 최대한 가까운 카드 3장의 합을 출력한다.

# 풀이 1: result_list를 list(중복 O, 순서 O)로 풀이 -> 메모리 : 71429 KB, 시간 : 500ms
# 5 6 7 8 9 입력 시 result_list. len() : 60
# [18, 19, 20, 20, 21, 18, 22, 19, 20, 20, 21, 22, 21, 22, 18, 23, 19, 21, 20, 
# 22, 23, 18, 19, 20, 24, 20, 21, 21, 22, 24, 18, 20, 21, 21, 22, 18, 22, 23, 24, 
# 19, 20, 22, 21, 23, 19, 24, 20, 21, 20, 21, 22, 22, 23, 20, 24, 21, 22, 22, 23, 24]
# import sys
# import collections
# N,M = map(int, sys.stdin.readline().split())
# num_list = collections.deque(map(int,sys.stdin.readline().split()))
# result_list = []
# for i in range(len(num_list)):
#     num_1 = num_list.popleft()
#     for j in range(len(num_list)):
#         num_2 = num_list.popleft()
#         for k in range(len(num_list)):
#             num_3 = num_list.popleft()
#             result_list.append(num_1+num_2+num_3)
#             num_list.append(num_3)
#         num_list.append(num_2)
#     num_list.append(num_1)

# result_num = -1
# for sum_num in result_list:
#     if sum_num == M:
#         result_num = sum_num
#         break
#     elif sum_num > result_num and sum_num < M:
#         result_num = sum_num
    
# print(result_num)

# 풀이 2 : set(집합_중복 X, 순서 X) 로 풀이 -> 메모리 : 41160 KB, 시간 : 472ms
# 5 6 7 8 9 입력 시 result_set. len() : 7
# {18, 19, 20, 21, 22, 23, 24}
# ※ 현저하게 작다. 메모리와 속도 모두 낮아짐. 
# 당연할 수 있지만^^; 브루트포스(전수 대입) 시 중복이 예상되면 set을 사용하는게 좋을 듯
import sys
import collections
N,M = map(int, sys.stdin.readline().split())
num_list = collections.deque(map(int,sys.stdin.readline().split()))
result_set = set({})
for i in range(len(num_list)):
    num_1 = num_list.popleft()
    for j in range(len(num_list)):
        num_2 = num_list.popleft()
        for k in range(len(num_list)):
            num_3 = num_list.popleft()
            result_set.add(num_1+num_2+num_3)
            num_list.append(num_3)
        num_list.append(num_2)
    num_list.append(num_1)

result_num = -1
for sum_num in result_set:
    if sum_num == M:
        result_num = sum_num
        break
    elif sum_num > result_num and sum_num < M:
        result_num = sum_num
    
print(result_set)