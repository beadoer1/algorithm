# 정수를 담은 이차원 리스트, mylist 가 solution 함수의 파라미터로 주어집니다. 
# mylist에 들은 각 원소의 길이를 담은 리스트를 리턴하도록 solution 함수를 작성해주세요.

# 제한 조건
# mylist의 길이는 100 이하인 자연수입니다.
# mylist 각 원소의 길이는 100 이하인 자연수입니다.
# 예시
# input               	output
# [[1], [2]]	        [1,1]
# [[1, 2], [3, 4], [5]]	[2,2,1]

# 풀이 1 : low level에 가까운 답이라고 한다.
# def solution(mylist):
#     answer = []
#     for i in range(len(mylist)):
#         answer.append(len(mylist[i]))
#     return answer

# 풀이 2 : 프로그래머스 강의 답안(파이썬다운 답이라고..)
def solution(mylist):
    return list(map(len,mylist))

# test case
testa = [[1], [2]]
testb = [[1, 2], [3, 4], [5]]
print(solution(testa))
print(solution(testb))