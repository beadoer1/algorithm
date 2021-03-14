# 문제
# 베르트랑 공준은 임의의 자연수 n에 대하여, n보다 크고, 2n보다 작거나 같은 소수는 적어도 하나 존재한다는 내용을 담고 있다.
# 이 명제는 조제프 베르트랑이 1845년에 추측했고, 파프누티 체비쇼프가 1850년에 증명했다.
# 예를 들어, 10보다 크고, 20보다 작거나 같은 소수는 4개가 있다. (11, 13, 17, 19) 
# 또, 14보다 크고, 28보다 작거나 같은 소수는 3개가 있다. (17,19, 23)
# 자연수 n이 주어졌을 때, n보다 크고, 2n보다 작거나 같은 소수의 개수를 구하는 프로그램을 작성하시오. 
# 입력
# 입력은 여러 개의 테스트 케이스로 이루어져 있다. 각 케이스는 n을 포함하는 한 줄로 이루어져 있다.
# 입력의 마지막에는 0이 주어진다.
# 출력
# 각 테스트 케이스에 대해서, n보다 크고, 2n보다 작거나 같은 소수의 개수를 출력한다.
# 제한
# 1 ≤ n ≤ 123,456

# 풀이 : 동적 계획법 이용할 예정 '정답~~~~~!'
import sys

prime_num = { 

}
# 쌓아놓은 데이터베이스(prime_num)에서 확인 후 count 반환
def find_prime_num(num):
    count = 0    
    for i in range(num+1,2*num+1): # num+1 부터 2*num 까지
        if prime_num[i] == 1:
            count+=1
    return count

# 입력된 수 중 가장 큰 수까지의 소수를 정리하는 함수(전체에서 소수가 아닌 것(n의 배수)의 value를 0으로 만듬)
def filtering_prime(num):
    for i in range(2,num+1):
        prime_num[i] = 1
    for i in range(2,num+1):
        if prime_num[i] == 1:
            n = 2
            while n * i <= num:
                prime_num[n*i] = 0
                n += 1
        else:
            continue
    return prime_num

check_list = []
while True:
    num = int(sys.stdin.readline())
    if num == 0:
        break
    check_list.append(num)
filtering_prime(max(check_list)*2)
for i in check_list:
    print(find_prime_num(i))

# 풀이 2_이정주 님
#베르트랑 공준
#4948번 
# import math                 101 = 10.xxxx % 10 != 0   
# N = 123456 * 2 + 1
# prime_numbers = [True] * N
# for i in range(2, int(math.sqrt(N))+1):
#     if prime_numbers[i]:                    # N까지의 모든 숫자들의 제곱근이 범위인데 그것들을 돌예정
#         for j in range(2*i, N, i):        # N까지의 모든 i 배수들을 False 처리한다. i 는 예외
#             prime_numbers[j] = False       # 에라토스테네스의 체 원리를 제대로 구현한 문장, 모든 수는 소수들의 배수이니까.. N까지의 제곱근 단위에 배수하면 나머지는 전부 소수가아니니
# def get_prime_num_count(value):                 # 입력값의 지정된 범위안의 소수 갯수를 출력하는 함수
#     count = 0
#     for i in range(value + 1, (value*2) + 1):    # N보다 크고 2N 보다는 작거나 같은 소수 구하기위한 범위 설정
#         if prime_numbers[i]:
#             count += 1
#     return count
# result = []
# while True:
#     value = int(input())
#     if value == 0:
#         break
#     result.append(get_prime_num_count(value))
# for i in result:
#     print(i)




