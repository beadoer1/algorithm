# 문제
# 두 개의 자연수를 입력받아 최대 공약수와 최소 공배수를 출력하는 프로그램을 작성하시오.
# 입력
# 첫째 줄에는 두 개의 자연수가 주어진다. 이 둘은 10,000이하의 자연수이며 사이에 한 칸의 공백이 주어진다.
# 출력
# 첫째 줄에는 입력으로 주어진 두 수의 최대공약수를, 둘째 줄에는 입력으로 주어진 두 수의 최소 공배수를 출력한다.

# 풀이
import sys
import math
def find_divisor(num):
    divisor_list = []
    for i in range(1,int(math.sqrt(num))+1):
        if num % i == 0:
            divisor_list.append(i)
            divisor_list.append(num//i)
    return divisor_list

M,N = map(int,sys.stdin.readline().split())
# 약수를 찾아 넣는다.
divisor_list_M = find_divisor(M)
divisor_list_N = find_divisor(N)
# 내림차순으로 정렬(큰 것부터 비교하기 위함)
divisor_list_M.sort(reverse=True)
divisor_list_N.sort(reverse=True)
# 약수 중 큰 것부터 비교하여 공통되면 그 값을 저장한다.
for num in divisor_list_M:
    if num in divisor_list_N:
        greatest_common_divisor = num
        break
# 최소공배수 : 각 값을 최대공약수로 나누어 나온 몫들과 최소공배수를 곱한 값
least_common_multiple = M*N//greatest_common_divisor
# 최소공배수, 최대공약수 출력
print(greatest_common_divisor)
print(least_common_multiple)

# 다른 분들 풀이 '유클리드 호제법' 이라는 개념을 사용해야 한다고..
# x,y = map(int, input().split())
# a,b = x,y
# gcd = 0
# # 24 18
# while True:
#     z = x % y # 24 % 18 = 12, 18 % 12 = 6
#     if y % z == 0: # 18 % 12 = 6
#         gcd = z
#         lcd = z * y
#         break
#     x = y # x = 18
#     y = z # y = 12
# print(gcd)
# print(int(a * b / gcd))

# 다른 분들 풀이
# a, b = map(int, input().split())
# def gcd(a, b):                #유클리드 호제법
#     if a < b:
#         (a, b) = (b, a)
#     while b != 0:
#         (a, b) = (b, a % b)
#     return a
# c = gcd(a, b)   #최대공약수    
# d = (a//c) * (b//c) * c   #최소공배수 
# print(c, d, sep='\n')
