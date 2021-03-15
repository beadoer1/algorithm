# 문제
#                                (N)
# 자연수 과 정수 가 주어졌을 때 이항 계수 (K)를 구하는 프로그램을 작성하시오.
# 입력
# 첫째 줄에 과 가 주어진다. (1 ≤ N ≤ 10, 0 ≤ K ≤ N)
# 출력
# (N)
# (K)를 출력한다.

# 이항 계수의 항등식 중 '파스칼의 법칙'을 적용하여 재귀식을 만들었다.
# 풀이 1: 동적계획법 없이 _ 메모리 : 28776 KB, 속도 : 64 ms
import sys
N, K = map(int,sys.stdin.readline().split())
memo = {}
def find_binomial_coefficient(N,K):
    if K == 0 or K == N:
        return 1
    else:
        return = find_binomial_coefficient(N-1,K) + find_binomial_coefficient(N-1,K-1)

print(find_binomial_coefficient(N,K))

# 풀이 2: 동적계획법 추가하여 _ 메모리 : 28776 KB, 속도 : 68 ms
# import sys
# N, K = map(int,sys.stdin.readline().split())
# memo = {}
# def find_binomial_coefficient(N,K):
#     if K == 0 or K == N:
#         return 1
#     elif (N,K) in memo:
#         return memo[(N,K)]
#     else:
#         memo[(N,K)] = find_binomial_coefficient(N-1,K) + find_binomial_coefficient(N-1,K-1)
#         return memo[(N,K)]

# print(find_binomial_coefficient(N,K))

# 풀이 3: 다른 분들 풀이
# n! / r!(n-r)!
# n, r = map(int, input().split())
# def binomial_theorem(x):
#     if x == 1 or x == 0:
#         return 1
#     return x * binomial_theorem(x-1)
# ans = binomial_theorem(n) / (binomial_theorem(r) * binomial_theorem(n-r))
# print(int(ans))

# 풀이 4: 다른 분들 풀이
#     n             n!
#    ㅡㅡ   =    ㅡㅡㅡㅡㅡㅡ
#     k         (n-k!)(k!)
# N, K = list(map(int, input().split()))
# up = 1
# for i in range(N, N-K, -1):   #(N-K-1)!   -> N!//(N-K)! 과 같음
#     up *= i
# down = 1
# for i in range(1, K+1):      # K!
#     down *= i
# print(up//down)