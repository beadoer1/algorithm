# 주어진 문자열에서 여러번 나오지 않고 가장 앞에 있는 글자를 출력하는 문제

input = "abacabade"

def find_not_repeating_character(string):
    # 풀이
    alphabet_occurrence_array = [0] * 26
    for char in string:
        if not char.isalpha(): # alphabet 인지 구분하는 내장함수
            continue
        arr_index = ord(char)-ord('a')
        alphabet_occurrence_array[arr_index] += 1
    for char in string:
        if alphabet_occurrence_array[ord(char)-ord('a')] == 1:
            return char

result = find_not_repeating_character(input)
print(result)