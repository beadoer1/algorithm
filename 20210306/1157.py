# 문제
# 알파벳 대소문자로 된 단어가 주어지면, 이 단어에서 가장 많이 사용된 알파벳이 무엇인지 알아내는 프로그램을 작성하시오. 
# 단, 대문자와 소문자를 구분하지 않는다.
# 입력
# 첫째 줄에 알파벳 대소문자로 이루어진 단어가 주어진다. 주어지는 단어의 길이는 1,000,000을 넘지 않는다.
# 출력
# 첫째 줄에 이 단어에서 가장 많이 사용된 알파벳을 대문자로 출력한다. 
# 단, 가장 많이 사용된 알파벳이 여러 개 존재하는 경우에는 ?를 출력한다.
# 입력 예시        출력 예시
# Mississipi     ?
# zZa            Z
# z              Z
# baaa           A

# 풀이 1 : 시간 초과..
# word_check = list(input().upper()) # input()을 받아 대문자로 바꿔 char 단위로 분리
# char_max = ''  # 판별을 위한 변수 ↓
# count_max = -1
# # 판별 시작
# for char1 in word_check:       
#     count = 0
#     for char2 in word_check:   # 비교 대상
#         if char1 == char2:     # 같으면
#             count = count + 1  # count
#     if count == count_max and char1 != char_max: # count가 최대값과 같고 char와 다른 Alpha 면 '?'
#         char_max = '?'
#     elif count > count_max:    # count 가 최대값보다 크면 
#         count_max = count      # 최대값 바꿔주고
#         char_max = char1      # 최대 char도 바꿔줘
# print(char_max)

# 풀이 2 : count(val) 을 활용했으나 시간 초과 _ 아무래도 전체 반복문 자체를 돌리면 안되는 듯
# from collections import Counter
# char_list = list(input().upper()) # input()을 받아 대문자로 바꿔 char 단위로 분리
# char_max = ''  # 판별을 위한 변수 ↓
# count_max = -1
# for char in char_list:
#     count_char = char_list.count(char)
#     if count_char > count_max:
#         count_max = count_char
#         char_max = char
#     elif count_char == count_max and char != char_max:
#         char_max = '?'
# print(char_max)

# 풀이 3 : 이왕 collections 쓴거 왕찬 이용하자 했는데 계속 런타임 에러가 뜬다.. 
# 라고 원망하다가 문자 종류가 하나만 있는 경우를 소화 못함을 발견
# from collections import Counter
# char_list = list(input().upper())
# char_count = Counter(char_list)
# # 중복 여부 확인 check overlap
# c_o = char_count.most_common(2)
# if c_o[0][1] == c_o[1][1]:
#     print('?')
# elif c_o[0][1] > c_o[1][1]:
#     print(c_o[0][0])
# else:
#     print(c_o[1][0])

# 풀이 4 : 왐마... 드디어 ㅠㅠㅠㅠ
from collections import Counter
char_l = list(input().upper())
res = char_l[0] # 한가지 종류의 문자만 들어올 경우(else 없애기 위함)
if len(char_l) > 1:
    # frequency check
    fre_c = Counter(char_l).most_common(2)
    fre_c0 = fre_c[0]
    fre_c1 = fre_c[1]
    if fre_c0[1] == fre_c1[1]:
        res = '?'
    elif fre_c0[1] > fre_c1[1]:
        res = fre_c0[0]
    else:
        res = fre_c1[0]
print(res)

# 풀이 4 : 태웅님 답변 참고. 맞았습니다!..ㅠㅠ 왜 내껀 안되냐고오 ㅠㅠ
# from collections import Counter
# char_count = Counter(list(input().upper()))
# res_ = []
# for name_,num_ in char_count.items():
#     if num_ == max(char_count.values()):
#         res_.append(name_)
#         if len(res_) > 1:
#             break
# if len(res_) > 1:
#     print('?')
# else:
#     print(res_[0])
# count_max = -1
# char_max = ''
# for char in char_count: # key 값만 불러오는구나.
    

# 타인의 시각 (문태웅)
from collections import Counter
word = list(input().upper())
frequency = Counter(word)
result_ = []
for name_,number_ in frequency.items():
    if number_ == max(frequency.values()):
        result_.append(name_)
        if len(result_) > 1:
            break
if len(result_) == 1:
    print(result_[0])
else:
    print('?')