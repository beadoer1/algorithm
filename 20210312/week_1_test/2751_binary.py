# 문제
# N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.
# 입력
# 첫째 줄에 수의 개수 N(1 ≤ N ≤ 1,000,000)이 주어진다. 둘째 줄부터 N개의 줄에는 숫자가 주어진다. 
# 이 수는 절댓값이 1,000,000보다 작거나 같은 정수이다. 수는 중복되지 않는다.
# 출력
# 첫째 줄부터 N개의 줄에 오름차순으로 정렬한 결과를 한 줄에 하나씩 출력한다.

import sys

num_tot = int(sys.stdin.readline())
num_list = []
num_zero_in = int(sys.stdin.readline())
num_list.append(num_zero_in)
for i in range(1,num_tot):
    num = int(sys.stdin.readline())
    low = 0
    high = len(num_list)-1
    while low <= high:
        mid = (low + high)//2
        if num > num_list[mid]:
            low = mid + 1
        else:
            high = mid - 1
    if low > high: 
        num_list.insert(high,num)
for num in num_list:
    print(num)



