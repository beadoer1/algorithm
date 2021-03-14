# 문제
# M이상 N이하의 소수를 모두 출력하는 프로그램을 작성하시오.
# 입력
# 첫째 줄에 자연수 M과 N이 빈 칸을 사이에 두고 주어진다. (1 ≤ M ≤ N ≤ 1,000,000) M이상 N이하의 소수가 하나 이상 있는 입력만 주어진다.
# 출력
# 한 줄에 하나씩, 증가하는 순서대로 소수를 출력한다.
# 입력    출력  
# 3 16   3
#        5
#        7
#        11
#        13

# 풀이 1 : 결과는 출력이 되지만 이중 loop를 돌아 그런지 '시간 초과' 가 뜬다. + 틀린 답이기도 함
# def prime_num(num):
#     for i in range(2,num):
#         if (num % i) == 0:
#             return # 함수를 빠져나가기 위함
#     print(num)

# 풀이 2 : 앞에서 걸러진 소수로만 나눈다면 결과가 달라질까? '시간 초과' 아직 길다. + 틀린 답이기도 함
#        애초에 잘못 짰었구나.. 시작값을 넣지 않았다..
# prime_list = []
# def prime_num(num):
#     if num == 1:
#         return
#     elif num == 2:
#         prime_list.append(num)
#         print(num)
#         return
#     for i in prime_list:
#         if (num % i) == 0:
#             return
#     prime_list.append(num)
#     print(num)
    

# m,n = map(int,input().split())
# for i in range(m,n+1):  # m 이상 n '이하' 이므로 + 1
#     prime_num(i)

# 풀이 3 : '출력 초과' 생각보다 따져봐야할 경우의 수가 많다... 다시 첨부터 하자.
# wiki '소수' 검색을 통한 힌트
# 어떤 자연수 n이 소수임을 판정하기 위해서 root(n)까지만 진행하면 되는데,  <- 이게 중요했구만..
# 수가 수를 나누기 위해서는 그 몫이 항상 필요하며 나누는 수와 몫 중 어느 하나는 반드시 root(n) 이하이기 때문이다.
# 소수를 골라내기 위한 방법은 다음과 같다. 이 방법을 이용해 소수를 어느 정도 골라낼 수 있다.
# 2와 5를 제외하면, 모든 소수의 일의 자리 수는 1, 3, 7, 9이다.
# 어떤 자연수 n이 소수임을 판정하기 위해선 root(n)까지의 수 중 1을 제외하고 그 자연수의 약수가 있는지 확인하면 된다.
# 배수의 성질을 이용하면 쉽게 구할 수도 있다.
# import math

# prime_list = [2]

# def prime_add(num): # 시작점이 3보다 클 때 3~num 까지의 수 중 소수를 list에 넣기 위한 함수
#     if num == 3:
#         prime_list.append(num)
#     else:
#         _sqrt = math.sqrt(num)
#         for i in prime_list:
#             if i > _sqrt: # for문을 root(n)까지만 진행
#                 break
#             elif (num % i) == 0:
#                 return
#             prime_list.append(num)

# def prime_print(num): # 3 초과의 소수 구분/출력 함수
#     if num == 3:
#         prime_list.append(num)
#         print(num)
#     else:
#         _sqrt = math.sqrt(num)
#         for i in prime_list:
#             if i > _sqrt: # for문을 root(n)까지만 진행 # root(3)이 2보다 작고 그 다음이 없어 그냥 지나감
#                 break
#             elif (num % i) == 0:
#                 return
#             prime_list.append(num)
#             print(num)

# def prime_all(first,last):
#     if first == 1 and last ==1: # 1 1 입력 대비
#         return
#     elif first <= 2 and last >= 2: # 1 2, 2 2 입력 대비
#         print(2)
#         if last > 2: 
#             for num in range(first,last+1):  # start 이상 last '이하' 이므로 + 1
#                 prime_print(num)            
#     elif first == 3:
#         for num in range(first,last+1):  # m 이상 n '이하' 이므로 + 1
#             prime_print(num)
#     else:
#         for num in range(3, first):
#             prime_add(num)
#         for num in range(first,last+1):  # m 이상 n '이하' 이므로 + 1
#             prime_print(num)

# m,n = map(int,input().split())
# prime_all(m, n)

# 풀이 4 : 아... 구현했는데 '시간 초과'
# import math

# prime_list = [2]

# def prime_add(num): # 2를 제외한 나머지 소수에 적용
#     prime = 1 # while 문 시작 시 3을 통과시키기 위해 1.7보다 작은 수로 배정
#     _sqrt = math.sqrt(num)
#     while prime < _sqrt:
#         for prime in prime_list:
#             if num % prime == 0: # 여기서 2는 걸러짐
#                 return    
#         prime_list.append(num)

# def prime_print(num): # 2를 제외한 나머지 소수에 적용
#     prime = 1 # while 문 시작 시 3을 통과시키기 위해 1.7보다 작은 수로 배정
#     _sqrt = math.sqrt(num)
#     if num == 2:
#         print(2)
#     while prime < _sqrt:
#         for prime in prime_list:
#             if num % prime == 0: # 여기서 2는 걸러짐
#                 return    
#         prime_list.append(num)
#         print(num)

# def prime_all(start, last):
#     if start > 3:
#         for i in range(3,start):
#             prime_add(i)
#         for j in range(start,last+1):
#             prime_print(j)
#     else:
#         for k in range(start, last+1):
#              prime_print(k)
        
# m,n = map(int,input().split())
# prime_all(m, n)

# 풀이 5 : 맞았다..ㅠㅠ!!
# import math

# prime_list = [2] # 2 보다 큰 수 중 짝수를 거르기 위한 소수

# def prime_add(num): # 2를 제외한 나머지 소수에 적용
#     _sqrt = math.sqrt(num)
#     if num == 1 and num == 2:
#         return
#     for prime in prime_list:
#         if prime > _sqrt:
#             break
#         if int(num % prime) == 0: # 여기서 2가 걸러지기는 하나, 앞에서 걸러주는게 더 빠름
#             return
#     prime_list.append(num)

# def prime_print(num): # 2를 제외한 나머지 소수에 적용
#     # prime = 1 # while 문 시작 시 3을 통과시키기 위해 1.7보다 작은 수로 배정
#     _sqrt = math.sqrt(num)
#     if num == 1:
#         return
#     elif num == 2:
#         print(2)
#         return
#     for prime in prime_list:
#         if prime > _sqrt:
#             break
#         if int(num % prime) == 0: # 여기서 2가 걸러져서 별도 출력 필요
#             return
#     prime_list.append(num)
#     print(num)

# def prime_all(start, last):
#     if start > 3:
#         for i in range(3,start):
#             prime_add(i)
#         for j in range(start,last+1):
#             prime_print(j)
#     else:
#         for k in range(start, last+1):
#              prime_print(k)
        
# m,n = map(int,input().split())
# prime_all(m, n)

# 문제 6 : 타인의 시선(문태웅) -> 내 코드보다 약 10배 가량 빠르다..ㅠㅠ
m, n = map(int, input().split())
def prime_number(m, n):
    n+= 1
    prime = [True] * n
    for i in range(2, int(n**0.5)+1):
        if prime[i]== True:
            for j in range(2*i, n, i):
                prime[j] = False
    for i in range(m, n):
        if i > 1 and prime[i] == True:
            print(i)
prime_number(m, n)