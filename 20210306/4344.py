# 문제
# 대학생 새내기들의 90%는 자신이 반에서 평균은 넘는다고 생각한다. 당신은 그들에게 슬픈 진실을 알려줘야 한다.
# 입력
# 첫째 줄에는 테스트 케이스의 개수 C가 주어진다.
# 둘째 줄부터 각 테스트 케이스마다 학생의 수 N(1 ≤ N ≤ 1000, N은 정수)이 첫 수로 주어지고, 이어서 N명의 점수가 주어진다. 
# 점수는 0보다 크거나 같고, 100보다 작거나 같은 정수이다.
# 출력
# 각 케이스마다 한 줄씩 평균을 넘는 학생들의 비율을 반올림하여 소수점 셋째 자리까지 출력한다.
# 입력                                  출력
# 5 
# 5 50 50 70 80 100                    40.000%
# 7 100 95 90 80 70 60 50              57.143%
# 3 70 90 80                           33.333%
# 3 70 90 81                           66.667%
# 9 100 99 98 97 96 95 94 93 91        55.556%

# 풀이 2(21.03.18 재풀이) : 코드를 간소화 해보자.
import sys
class_num = int(sys.stdin.readline())
for i in range(class_num):
    class_score = list(map(int,sys.stdin.readline().split()))
    avg = sum(class_score[1:])/class_score[0]
    count = 0
    for j in range(1,len(class_score)):
        if class_score[j] > avg:
            count+=1
    print('{:.3f}%'.format(count/class_score[0]*100))

# 풀이 1: '평균을 넘는 학생의 비율!'
# 총 class 수 입력
# cl_num = int(input())
# per_tot = list()
# for 0 in range(cl_num):
#     # 각 class 별 정보 입력 ('index:0'은 총 인원수)
#     globals()['cl_0'] = list(map(int,input().split())) # cl_i 라는 동적변수에 input() 받은 list 지정
#     cl = globals()['cl_'+str(i)] # 코드 간소화를 위한 변수 지정
    
#     # 평균을 구하고,
#     length = len(cl) # for문을 돌리기 위해 list의 길이 지정
#     sum = 0
#     for j in range(1,length):
#         sum += cl[j]
#     avg = sum / cl[0]
#     # 각 학생의 점수와 비교
#     count = 0
#     for k in range(1,length):
#         if cl[k] > avg:
#             count += 1
    
#     # 전체 학생에 대한 비율을 구하고 소수점 셋째자리 % 형태로 출력 
#     rate = count/cl[0]
#     per = rate * 100
#     per_tot.append(per) # per_tot list에 저장

# # 서식지정자를 통해 요구사항에 맞게 출력
# for i in per_tot:
#     print('{:.3f}%'.format(i))


# 다른 사람 풀이
# cases_ = int(input())
# for i in range(cases_):
#     k = list(map(int, input().split()))
#     _average = (sum(k) - k[0]) / k[0]
#     _count = 0
#     for j in range(1, k[0]+1):
#         if k[j] > _average:
#             _count += 1
#     print("{0:.3f}".format(_count/k[0]*100))







