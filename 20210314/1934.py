# 문제
# 두 자연수 A와 B에 대해서, A의 배수이면서 B의 배수인 자연수를 A와 B의 공배수라고 한다. 
# 이런 공배수 중에서 가장 작은 수를 최소공배수라고 한다. 
# 예를 들어, 6과 15의 공배수는 30, 60, 90등이 있으며, 최소 공배수는 30이다.
# 두 자연수 A와 B가 주어졌을 때, A와 B의 최소공배수를 구하는 프로그램을 작성하시오.
# 입력
# 첫째 줄에 테스트 케이스의 개수 T(1 ≤ T ≤ 1,000)가 주어진다. 
# 둘째 줄부터 T개의 줄에 걸쳐서 A와 B가 주어진다. (1 ≤ A, B ≤ 45,000)
# 출력
# 첫째 줄부터 T개의 줄에 A와 B의 최소공배수를 입력받은 순서대로 한 줄에 하나씩 출력한다.

# 풀이 1: 최소공배수를 구한 후에 최대공배수를 구하는 방식. '시간 초과'..하아
# import sys
# prime_num = []
# def find_divisor(num):
#     array = []
#     for i in range(1,num+1):
#         if num % i == 0:
#             array.append(i)
#     return array

# def find_maximum_common_divisor(num1,num2):
#     divisor_num1 = find_divisor(num1)
#     divisor_num2 = find_divisor(num2)
#     divisor_num1.sort(reverse=True)
#     max_com_divisor = 0
#     for i in divisor_num1:
#         if i in divisor_num2:
#             max_com_divisor = i
#             return max_com_divisor

# def find_minimum_common_multiple(num1,num2):
#     max_com_divisor = find_maximum_common_divisor(num1,num2)
#     diff_divisor_num1 = num1//max_com_divisor 
#     diff_divisor_num2 = num2//max_com_divisor 
#     min_com_multiple = max_com_divisor*diff_divisor_num1*diff_divisor_num2
#     return min_com_multiple

# tot_cases = int(sys.stdin.readline())
# num_list = []
# for i in range(tot_cases):
#     nums = list(map(int,sys.stdin.readline().split()))
#     num_list.append(nums)
# for j in range(len(num_list)):
#     print(find_minimum_common_multiple(num_list[j][0],num_list[j][1]))

# 풀이 2: 소수 구한 후에 나누어 구하는 방식으로 가야할 듯.


