# 문제
# 수열 A가 주어졌을 때, 가장 긴 증가하는 부분 수열을 구하는 프로그램을 작성하시오.
# 예를 들어, 수열 A = {10, 20, 10, 30, 20, 50} 인 경우에 
# 가장 긴 증가하는 부분 수열은 A = {10, 20, 30, 50} 이고, 길이는 4이다.
# 입력
# 첫째 줄에 수열 A의 크기 N (1 ≤ N ≤ 1,000)이 주어진다.
# 둘째 줄에는 수열 A를 이루고 있는 Ai가 주어진다. (1 ≤ Ai ≤ 1,000)
# 출력
# 첫째 줄에 수열 A의 가장 긴 증가하는 부분 수열의 길이를 출력한다.

# 풀이 2(21.03.18 재풀이) : dp를 이용해 앞에서 뒤로 달려보자. -> 방법까지 도달하는게 어려운 문제였다.
import sys

tot_num = int(sys.stdin.readline())
num_seq = list(map(int, sys.stdin.readline().split()))  # 살펴볼 전체 수열

dp = [1]*tot_num # 맨 앞 부터 본인까지 '최대 수열 길이 값'을 저장하는 별도 list

for i in range(tot_num):
    max_seq = 1
    for j in range(i+1):
        if j == i:
            dp[i] = max_seq
        # 앞에 있는 본인보다 작은 수의 dp 데이터(본인까지의 최대 수열 길이)를 확인해 거기에 + 1 해주는게 포인트.    
        elif num_seq[j] < num_seq[i] and dp[j] >= max_seq: 
            max_seq = dp[j] + 1
print(max(dp))

# 풀이 1: max 값을 저장해 놓고 앞으로 가는건 방법이 틀렸다.

# import sys
# memo = []
# def find_longest_increasing_sequence(n,array):
#     max_count = 0
#     for i in range(n):
#         if i in memo:
#             continue
#         else:
#             count = 0
#             max_num = 0
#             for seq_index in range(i,len(array)):
#                 if array[seq_index] > max_num:
#                     max_num = array[seq_index]
#                     count += 1
#                     memo.append(seq_index)
#             if count > max_count:
#                 max_count = count
#     return max_count

# # num = int(sys.stdin.readline())
# num = 5
# # sequence = list(map(int,sys.stdin.readline().split()))
# sequence = [2,6,9,1,3]
# print(find_longest_increasing_sequence(num,sequence))





