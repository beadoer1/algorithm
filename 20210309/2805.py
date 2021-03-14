# 문제
# 상근이는 나무 M미터가 필요하다. 근처에 나무를 구입할 곳이 모두 망해버렸기 때문에, 정부에 벌목 허가를 요청했다. 
# 정부는 상근이네 집 근처의 나무 한 줄에 대한 벌목 허가를 내주었고, 상근이는 새로 구입한 목재절단기를 이용해서 나무를 구할것이다.
# 목재절단기는 다음과 같이 동작한다. 먼저, 상근이는 절단기에 높이 H를 지정해야 한다. 높이를 지정하면 톱날이 땅으로부터 H미터 위로 올라간다. 
# 그 다음, 한 줄에 연속해있는 나무를 모두 절단해버린다. 따라서, 높이가 H보다 큰 나무는 H 위의 부분이 잘릴 것이고, 낮은 나무는 잘리지 않을 것이다. 
# 예를 들어, 한 줄에 연속해있는 나무의 높이가 20, 15, 10, 17이라고 하자. 
# 상근이가 높이를 15로 지정했다면, 나무를 자른 뒤의 높이는 15, 15, 10, 15가 될 것이고, 
# 상근이는 길이가 5인 나무와 2인 나무를 들고 집에 갈 것이다. 
# (총 7미터를 집에 들고 간다) 절단기에 설정할 수 있는 높이는 양의 정수 또는 0이다.
# 상근이는 환경에 매우 관심이 많기 때문에, 나무를 필요한 만큼만 집으로 가져가려고 한다. 
# 이때, 적어도 M미터의 나무를 집에 가져가기 위해서 절단기에 설정할 수 있는 높이의 최댓값을 구하는 프로그램을 작성하시오.
# 입력
# 첫째 줄에 나무의 수 N과 상근이가 집으로 가져가려고 하는 나무의 길이 M이 주어진다. (1 ≤ N ≤ 1,000,000, 1 ≤ M ≤ 2,000,000,000)
# 둘째 줄에는 나무의 높이가 주어진다. 나무의 높이의 합은 항상 M보다 크거나 같기 때문에, 상근이는 집에 필요한 나무를 항상 가져갈 수 있다. 
# 높이는 1,000,000,000보다 작거나 같은 양의 정수 또는 0이다.
# 출력
# 적어도 M미터의 나무를 집에 가져가기 위해서 절단기에 설정할 수 있는 높이의 최댓값을 출력한다.
# 입력             출력
# 4 7             15
# 20 15 10 17

# 풀이 1 : 아.. 다 온 거 같은데... 자꾸 틀렸다고 하시네..
# import sys

# num_tree,needed_length = map(int,sys.stdin.readline().split())

# length_trees = list(map(int,sys.stdin.readline().split()))

# length_trees.sort(reverse=True)

# def find_cut_tree_length(num,array,item):
#     low_in = 0
#     high_in = num-1
#     result_length = 0
    
#     while low_in <= high_in:
#         sum_length = 0

#         mid = int((high_in+low_in)/2)

#         for i in range(mid):
#             sum_length+=array[i]
        
#         result_length = sum_length-(mid*length_trees[mid])
#         index = mid
#         if result_length == item:
#             return [result_length, index]
#         elif result_length > item:
#             high_in = mid-1
#         else:
#             low_in = mid+1
    
#     return [result_length, index]

# result = find_cut_tree_length(num_tree, length_trees ,needed_length)

# if num_tree == 1:
#     print(length_trees[0] - needed_length)
# elif result[0] == 0:
#     print(int(length_trees[0]-(needed_length/(result[1]+1))))
# else:
#     if result[0]==needed_length:
#         print(length_trees[result[1]])
#     elif result[0]<needed_length:
#         print(result)
#     else:  
#         print(length_trees[result[1]] + int((result[0]-needed_length)/result[1]))

# 풀이 2 : 다시..ㅠ
import sys

num_tree,length_need = map(int,sys.stdin.readline().split())
trees = list(map(int,sys.stdin.readline().split()))
trees.sort(reverse=True)
# print(trees)
def find_cut_length(num,array,target):
    low_in = 0
    high_in = num-1
    result_length = 0
    while low_in <= high_in:
        length_sum = 0
        mid = int((high_in+low_in)/2)

        for i in range(mid):
            length_sum+=array[i]
        length_result=length_sum-(mid*trees[mid])
        index=mid
        if length_result == target:
            return [length_result, index]
        elif length_result > target:
            high_in = mid-1
        else:
            low_in = mid+1
    
    return [length_result, index]

result = find_cut_length(num_tree, trees, length_need)
length_result = result[0]
index_result = result[1]
if num_tree == 1:
    print(trees[0] - length_need)
else:
    if length_result==length_need:
        print(trees[index_result])
    elif length_result<length_need:
        print(int(trees[num_tree-1]-((length_need-length_result)/(index_result+1))))
    else:  
        print(int(trees[index_result]+((length_result-length_need)/index_result)))

# 풀이 3: 타인의 시선(돌아다니는 답안인 듯)
# import sys
# N, M = map(int, sys.stdin.readline().split())
# tree_list = list(map(int, sys.stdin.readline().split()))
# trees = sorted(tree_list)
# start = 1
# end = max(trees)
# while start <= end:
#     mid = (start + end) //2
#     print("mid "+str(mid))
#     check_data = 0
#     for i in trees:
#         if i >= mid:
#             check_data += i - mid
#     if check_data >= M:
#         start = mid + 1
#         print("start "+str(start))
#     else:
#         end = mid -1
#         print("end "+str(end))
# print(end)