# 문제
# N개의 정수 A[1], A[2], …, A[N]이 주어져 있을 때, 이 안에 X라는 정수가 존재하는지 알아내는 프로그램을 작성하시오.
# 입력
# 첫째 줄에 자연수 N(1 ≤ N ≤ 100,000)이 주어진다. 다음 줄에는 N개의 정수 A[1], A[2], …, A[N]이 주어진다. 
# 다음 줄에는 M(1 ≤ M ≤ 100,000)이 주어진다. 다음 줄에는 M개의 수들이 주어지는데, 이 수들이 A안에 존재하는지 알아내면 된다. 
# 모든 정수의 범위는 -231 보다 크거나 같고 231보다 작다.
# 출력
# M개의 줄에 답을 출력한다. 존재하면 1을, 존재하지 않으면 0을 출력한다.

# 풀이
import sys

def check_in_tot(n,tot_array):
    low_in = 0
    high_in = len(tot_array)-1
    while low_in <= high_in:
        mid_in = (low_in + high_in)//2
        if tot_array[mid_in] == n:
            return True
        elif tot_array[mid_in] > n:
            high_in = mid_in - 1
        else:
            low_in = mid_in + 1
    return False

N = int(sys.stdin.readline())
tot_num_list = list(map(int,sys.stdin.readline().split()))
M = int(sys.stdin.readline())
check_list = list(map(int,sys.stdin.readline().split()))
tot_num_list.sort() # 정렬을 빼먹지 말자..
for num in check_list:
    # print(num)
    check = check_in_tot(num,tot_num_list)
    if check == True:
        print(1)
    else:
        print(0)

