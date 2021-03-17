# 문제
# 수를 처리하는 것은 통계학에서 상당히 중요한 일이다. 
# 통계학에서 N개의 수를 대표하는 기본 통계값에는 다음과 같은 것들이 있다. 단, N은 홀수라고 가정하자.
# 산술평균 : N개의 수들의 합을 N으로 나눈 값
# 중앙값 : N개의 수들을 증가하는 순서로 나열했을 경우 그 중앙에 위치하는 값
# 최빈값 : N개의 수들 중 가장 많이 나타나는 값
# 범위 : N개의 수들 중 최댓값과 최솟값의 차이
# N개의 수가 주어졌을 때, 네 가지 기본 통계값을 구하는 프로그램을 작성하시오.
# 입력
# 첫째 줄에 수의 개수 N(1 ≤ N ≤ 500,000)이 주어진다. 그 다음 N개의 줄에는 정수들이 주어진다. 입력되는 정수의 절댓값은 4,000을 넘지 않는다.
# 출력
# 첫째 줄에는 산술평균을 출력한다. 소수점 이하 첫째 자리에서 반올림한 값을 출력한다.
# 둘째 줄에는 중앙값을 출력한다.
# 셋째 줄에는 최빈값을 출력한다. 여러 개 있을 때에는 최빈값 중 두 번째로 작은 값을 출력한다.
# 넷째 줄에는 범위를 출력한다.

# 풀이 1: 이게 이렇게 어려울 일인가..ㅠㅠ
import sys
tot_num = int(sys.stdin.readline())
num_list = []
for i in range(tot_num):
    num = int(sys.stdin.readline())
    num_list.append(num)
num_list.sort()

# 산술평균
avg_res = sum(num_list)/tot_num
avg_int = sum(num_list)//tot_num
avg_remain = avg_res-avg_int
if avg_remain >= 0.5:
    print(avg_int+1)
else:
    print(avg_int)

# 중앙값
mid_in = len(num_list)//2
print(num_list[mid_in])

# 최빈값_여러 개 있을 때에는 최빈값 중 두 번째로 작은 값 출력
if len(num_list) == 1: # list index가 하나 뿐일 때 indexError 방지를 위함
    print(num_list[0])
else:
    list_fre = {}
    count = 1
    for i in range(1,len(num_list)):
        if num_list[i] == num_list[i-1]:
            count += 1
            if i == len(num_list)-1:
                list_fre[num_list[i]] = count
        else:
            list_fre[num_list[i-1]] = count
            count = 1
            if i == len(num_list)-1:
                list_fre[num_list[i]] = count
    max_fre = max(list_fre.values())
    max_fre_nums = sorted([k for k, v in list_fre.items() if v == max_fre])
    if len(max_fre_nums) > 1:
        print(max_fre_nums[1])
    else:
        print(max_fre_nums[0])

# 범위
range_num = max(num_list)-min(num_list)
print(range_num)
    

# 최빈값 : 틀렸다니...ㅠ
# def find_max_frequency(num_list):
#     if len(num_list) == 1: # list index가 하나 뿐일 때 indexError 방지를 위함
#         print(num_list[0])
#         return

#     list_fre = []
#     count = 1
#     for i in range(1,len(num_list)):
#         if num_list[i] == num_list[i-1]:
#             count += 1
#             if i == len(num_list)-1:
#                 count += 1
#                 list_fre.append([count,num_list[i]])
#         else:
#             list_fre.append([count,num_list[i-1]])
#             count = 1 # count 초기화
#             if i == len(num_list)-1:
#                 list_fre.append([count,num_list[i]])

#     if len(list_fre) == 1: # list index가 하나 뿐일 때 indexError 방지를 위함
#         print(list_fre[0][1])
#         return

#     list_fre.sort(reverse=True) # 빈도수가 높은 값부터 비교하기 위해 역순 정렬
#     if list_fre[0][0] > list_fre[1][0]:
#         print(list_fre[0][1])
#     else:
#         for j in range(2,len(list_fre)):
#             if j == len(list_fre)-1:
#                 if list_fre[j][0] == list_fre[j-1][0]:
#                     print(list_fre[j-1][1])
#                     return
#                 else:
#                     print(list_fre[j-2][1])
#                     return
#             elif list_fre[j][0] == list_fre[j-1][0]:
#                 continue
#             else:
#                 print(list_fre[j-2][1])
#                 return
#     return

# 풀이 2: 다른 분들 답변

