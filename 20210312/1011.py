# 문제
# 우현이는 어린 시절, 지구 외의 다른 행성에서도 인류들이 살아갈 수 있는 미래가 오리라 믿었다. 
# 그리고 그가 지구라는 세상에 발을 내려 놓은 지 23년이 지난 지금, 
# 세계 최연소 ASNA 우주 비행사가 되어 새로운 세계에 발을 내려 놓는 영광의 순간을 기다리고 있다.
# 그가 탑승하게 될 우주선은 Alpha Centauri라는 새로운 인류의 보금자리를 개척하기 위한 
# 대규모 생활 유지 시스템을 탑재하고 있기 때문에, 
# 그 크기와 질량이 엄청난 이유로 최신기술력을 총 동원하여 개발한 공간이동 장치를 탑재하였다. 
# 하지만 이 공간이동 장치는 이동 거리를 급격하게 늘릴 경우 기계에 심각한 결함이 발생하는 단점이 있어서, 
# 이전 작동시기에 k광년을 이동하였을 때는 k-1 , k 혹은 k+1 광년만을 다시 이동할 수 있다. 
# 예를 들어, 이 장치를 처음 작동시킬 경우 -1 , 0 , 1 광년을 이론상 이동할 수 있으나 
# 사실상 음수 혹은 0 거리만큼의 이동은 의미가 없으므로 1 광년을 이동할 수 있으며, 
# 그 다음에는 0 , 1 , 2 광년을 이동할 수 있는 것이다. 
# ( 여기서 다시 2광년을 이동한다면 다음 시기엔 1, 2, 3 광년을 이동할 수 있다. )
# 김우현은 공간이동 장치 작동시의 에너지 소모가 크다는 점을 잘 알고 있기 때문에 x지점에서 y지점을 향해 
# 최소한의 작동 횟수로 이동하려 한다. 
# 하지만 y지점에 도착해서도 공간 이동장치의 안전성을 위하여 
# y지점에 도착하기 바로 직전의 이동거리는 반드시 1광년으로 하려 한다.
# 김우현을 위해 x지점부터 정확히 y지점으로 이동하는데 필요한 공간 이동 장치 작동 횟수의 최솟값을 구하는 
# 프로그램을 작성하라.
# 입력
# 입력의 첫 줄에는 테스트케이스의 개수 T가 주어진다. 
# 각각의 테스트 케이스에 대해 현재 위치 x 와 목표 위치 y 가 정수로 주어지며, x는 항상 y보다 작은 값을 갖는다. 
# (0 ≤ x < y < 231)
# 출력
# 각 테스트 케이스에 대해 x지점으로부터 y지점까지 정확히 도달하는데 필요한 최소한의 공간이동 장치 작동 횟수를 출력한다.

# 풀이 1: 주어지는 거리  x가 (n-1)^2 와 n^2 사이에 있을 때 n이 1회 공간이동 거리의 최대값이며,
#       나머지 공간이동 거리는 기본 2이다.
#       최소 단계를 위한 나머지 공간이동 거리는 x를 n^2로 나눈 나머지를 
#       다시 (n-1)으로 나눈 몫을 2에 더한 값으로 나타낼 수 있다.
# -> 틀렸...ㅠㅠ 방법은 맞는 것 같은데 코드를 잘못 짠 것 같다.
# import sys
# import math
# def find_min_step(tot_distance):
#     steps_tot = 0
#     max_one_step = int(math.sqrt(tot_distance))
#     cur_steps = 1
#     steps_tot += cur_steps
#     cur_tot_distance = tot_distance-max_one_step**2
#     if max_one_step == 1:
#         steps_tot += cur_tot_distance
#     else:
#         cur_one_step = max_one_step - 1
#         while cur_one_step > 0:
#             cur_steps = (cur_tot_distance//cur_one_step) + 2
#             steps_tot += cur_steps

#             cur_tot_distance = cur_tot_distance-cur_one_step**2
#             cur_one_step -= 1
#     return steps_tot

# T = int(sys.stdin.readline())
# test_cases = []
# for i in range(T):
#     x,y = map(int,sys.stdin.readline().split())
#     test_cases.append(y - x)
# for test_case in test_cases:
#     print(find_min_step(test_case))

# 풀이 2 : 정답 -> 최대값까지 올라갔다 오는 cycle 부분과 나머지를 따로 구현
import sys
import math

def find_min_step(tot_distance): #18
    # 총 step 수를 세기 위한 tot_steps를 정의한다.
    tot_steps = 0
    # 최대값까지 갔다 1로 돌아오는데 필요한 one_cycle_steps를 구한다.
    max_num = int(math.sqrt(tot_distance)) # 4
    one_cycle_steps = max_num*2-1 # 4*2-1
    if max_num == 1:
        tot_steps = tot_distance
    else:
        tot_steps += one_cycle_steps
        # one_cycle 외 나머지 거리를 max_num에서 숫자를 하나씩 빼며 나눈 몫으로 구해준다.
        one_cycle_distance = max_num**2
        remain_distance = tot_distance - one_cycle_distance
        num = max_num
        while remain_distance > 0:
            steps = int(remain_distance/num)
            tot_steps += steps
            remain_distance = remain_distance - (steps*num)
            num = num-1
    return tot_steps

T = int(sys.stdin.readline())
test_cases = []
for i in range(T):
    x,y = map(int,sys.stdin.readline().split())
    test_cases.append(y - x)
for test_case in test_cases:
    print(find_min_step(test_case))


# 풀이 : 다른 사람 답안
import math
import sys
r = sys.stdin.readline

T = int(r())        #테스트케이스의 개수

def minimum_move(start, end):
    diff = end - start
    max_distance = math.ceil(diff**0.5)
    if diff <= max_distance*(max_distance-1):
        return 2 * max_distance - 2
    else:
        return 2 * max_distance - 1

for _ in range(T):
    a, b = map(int, r().split())
    print(minimum_move(a, b))

# 풀이 3 :
#우주광속 이동 문제(1011번)
import math
N = int(input())
count = 0                                    #최소 작동 횟수
result = []
for _ in range(N):
    a, b = map(int, input().split())
    distance = b - a                              #주어진 값들간의 거리
    num = math.floor(math.sqrt(distance))         #주어진 값들 사이의 거리에 루트 씌움 (제곱근) , floor처리되어 이미 정수임
    num_jegob = num**2                            # 정수를 제곱근으로 갖는 제곱수(ex. 9 : 9의 제곱근은 3)
    if distance == num_jegob:
        count = (num*2)-1
    elif num_jegob < distance <= num_jegob + num:
        count = (num*2)
    elif (num_jegob + num) < distance:
        count = (num*2) + 1
    elif distance < 4:
        count = distance
    result.append(count)
for x in result:
    print(x)
