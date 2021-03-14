# 문제
# N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.
# 입력
# 첫째 줄에 수의 개수 N(1 ≤ N ≤ 1,000,000)이 주어진다. 둘째 줄부터 N개의 줄에는 숫자가 주어진다. 
# 이 수는 절댓값이 1,000,000보다 작거나 같은 정수이다. 수는 중복되지 않는다.
# 출력
# 첫째 줄부터 N개의 줄에 오름차순으로 정렬한 결과를 한 줄에 하나씩 출력한다.

import sys

def merge(array1,array2):
    array_sorted = []
    array1_in = 0
    array2_in = 0
    while array1_in <= len(array1)-1 and array2_in <= len(array2)-1:
        if array1[array1_in] < array2[array2_in]:
            array_sorted.append(array1[array1_in])
            array1_in +=1
        else:
            array_sorted.append(array2[array2_in])
            array2_in +=1
    if array1_in > len(array1)-1:
        array_sorted += array2[array2_in:]
    elif array2_in > len(array2)-1:
        array_sorted += array1[array1_in:]
    return array_sorted

def merge_sort(array):
    if len(array) <= 1:
        return array
    array1 = merge_sort(array[:len(array)//2])
    array2 = merge_sort(array[len(array)//2:])
    return merge(array1,array2)

num_tot = int(sys.stdin.readline())
num_list = []
for i in range(num_tot):
    num = int(sys.stdin.readline())
    num_list.append(num)
result_list = merge_sort(num_list)
for num in result_list:
    print(num)


