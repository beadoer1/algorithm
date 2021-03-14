# 문제
# 세준이는 양수와 +, -, 그리고 괄호를 가지고 식을 만들었다. 그리고 나서 세준이는 괄호를 모두 지웠다.
# 그리고 나서 세준이는 괄호를 적절히 쳐서 이 식의 값을 최소로 만들려고 한다.
# 괄호를 적절히 쳐서 이 식의 값을 최소로 만드는 프로그램을 작성하시오.
# 입력
# 첫째 줄에 식이 주어진다. 식은 ‘0’~‘9’, ‘+’, 그리고 ‘-’만으로 이루어져 있고, 가장 처음과 마지막 문자는 숫자이다. 
# 그리고 연속해서 두 개 이상의 연산자가 나타나지 않고, 5자리보다 많이 연속되는 숫자는 없다. 수는 0으로 시작할 수 있다. 
# 입력으로 주어지는 식의 길이는 50보다 작거나 같다.
# 출력
# 첫째 줄에 정답을 출력한다.

# 풀이 1: 앞에 0이 달린 숫자는 사용 불가하다.
# leading zeros in decimal integer literals are not permitted; use an 0o prefix for octal integers

# expression_list = list(input())
# expression_list.insert(0,'(')
# for i in expression_list:
#     first_minus = 0
#     word = expression_list.pop(0)
#     if word == '-':
#         expression_list.append(')-(')
#     else:
#         expression_list.append(word)
# expression_list.append(')')
# expression = ''.join(expression_list)
# print(eval(expression))

# 풀이 2
expression_0 = input()
# 1. + 기호로 나누어 맨 앞에 0을 지워준 후 +기호로 다시 합쳐준다.(0 안 지우면 '런타임 에러' 발생)
split_ex_plus = expression_0.split('+')
for i in range(len(split_ex_plus)):
    if len(split_ex_plus[i]) == 1:
        continue
    elif split_ex_plus[i][0] == '0' and split_ex_plus[i][1] != '-':
        split_ex_plus[i]= split_ex_plus[i].lstrip('0')
expression_1 = '+'.join(split_ex_plus)

# 2. -기호로 나누어 맨 앞에 0을 지워주고 -기호 좌우에 괄호를 붙여 다시 합쳐준다.
split_ex_minus = expression_1.split('-')
for i in range(len(split_ex_minus)):
    if len(split_ex_minus[i]) == 1:
        continue
    elif split_ex_minus[i][0] == '0' and split_ex_minus[i][1] != '+':
        split_ex_minus[i]= split_ex_minus[i].lstrip('0')
expression_2 = ')-('.join(split_ex_minus)

# 3. 양 끝에 있는 괄호를 커버하기 위해 좌우에 ()기호를 넣어준다.
expression_fi = '('+expression_2+')'

# 4. str 식을 실제 식으로 바꾸어 그 결과를 출력한다.
print(eval(expression_fi))



    
    

