# 셀프 넘버는 1949년 인도 수학자 D.R. Kaprekar가 이름 붙였다. 
# 양의 정수 n에 대해서 d(n)을 n과 n의 각 자리수를 더하는 함수라고 정의하자. 예를 들어, d(75) = 75+7+5 = 87이다.
# 양의 정수 n이 주어졌을 때, 이 수를 시작해서 n, d(n), d(d(n)), d(d(d(n))), ...과 같은 무한 수열을 만들 수 있다. 
# 예를 들어, 33으로 시작한다면 다음 수는 33 + 3 + 3 = 39이고, 그 다음 수는 39 + 3 + 9 = 51, 다음 수는 51 + 5 + 1 = 57이다. 
# 이런식으로 다음과 같은 수열을 만들 수 있다.
# 33, 39, 51, 57, 69, 84, 96, 111, 114, 120, 123, 129, 141, ...
# n을 d(n)의 생성자라고 한다. 위의 수열에서 33은 39의 생성자이고, 39는 51의 생성자, 51은 57의 생성자이다. 
# 생성자가 한 개보다 많은 경우도 있다. 예를 들어, 101은 생성자가 2개(91과 100) 있다. 
# 생성자가 없는 숫자를 셀프 넘버라고 한다. 100보다 작은 셀프 넘버는 총 13개가 있다. 
# 1, 3, 5, 7, 9, 20, 31, 42, 53, 64, 75, 86, 97
# 10000보다 작거나 같은 셀프 넘버를 한 줄에 하나씩 출력하는 프로그램을 작성하시오.

# 입력
# 입력은 없다.

# 출력
# 10,000보다 작거나 같은 셀프 넘버를 한 줄에 하나씩 증가하는 순서로 출력한다.

# 풀이 1 실패.. raw 를 만들어 놓고 빼려고 했는데.. 너무 먼 길 이었다.
# from collections import deque

# result_ = []

# def removeSN(num,que):
#     if num < 10000:
#         num_sep_list = list(map(int,str(num)))
#         num = num+sum(num_sep_list)
#         if num > 10000:
#             return que
#         print(num)
#         if nu
#         que.remove(num)
#         return removeSN(num,que)
#     return que

# def removeAll(que):
#     while len(que) != 0:
#         num = que.popleft()
#         # print(num,que)
#         que = removeSN(num,que)
#         result_.append(num)

# a = deque()
# for i in range(0,10000):
#     a.append(i+1)
# # print(len(a))

# b = removeAll(a)
# # print(len(b))

# 풀이 2 : 시간초과.. 내가 계속 무식한 방법만 생각하는걸까..
# a = []
# b = []
# def appendN(num,li):
#     num_sep_list = list(map(int,str(num)))
#     num = num+sum(num_sep_list)
#     if num > 10000:
#         return li
#     li.append(num)
#     return appendN(num,li)

# for i in range(1,10000):
#     if i in a:
#         continue
#     appendN(i,a)


# for i in range(1,10000):
#     if i in a:
#         continue
#     b.append(i)
# print(b)

# 풀이 3 : set 을 활용 !! 성공성공!!
a = set()
b = set()
c = set()
def addN(num,se):
    num_sep_list = list(map(int,str(num)))
    num = num+sum(num_sep_list)
    if num > 10000:
        return se
    se.add(num)
    return addN(num,se)

for i in range(1,10001):
    addN(i,a)

for i in range(1,10001):
    b.add(i)

c = sorted(b - a)

for num in c:
    print(num)

# 풀이 4: 타인의 시각 (문태웅) 훨씬.. 빠르다..ㅠㅠ
# list1 = list()
# def d(N):
#     for j in str(N):
#         N+= int(j)
#     list1.append(N)
# for i in range(1,10000):
#     d(i)
#     if i not in list1:
#         print(i)
# print(len(list1))
