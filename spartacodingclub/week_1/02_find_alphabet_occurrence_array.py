def find_alphabet_occurrence_array(string):
    alphabet_occurrence_array = [0] * 26
    # 풀이
    for _char in string:
        if _char.isalpha(): # alphabet 인지 구분하는 내장함수
            for al in range(97,123):
                if al == ord(_char): # char -> int 해주는 내장함수
                    _index = al-97
                    alphabet_occurrence_array[_index] += 1
    return alphabet_occurrence_array
print(find_alphabet_occurrence_array("hello my name is sparta"))

# 수업 답안 1
def find_alphabet_occurrence_array(string):
    alphabet_occurrence_array = [0] * 26
    # 풀이
    for char in string:
        if not char.isalpha(): # alphabet 인지 구분하는 내장함수
            continue
        arr_index = ord(char)-ord("a")
        alphabet_occurrence_array[arr_index] += 1
    return alphabet_occurrence_array
print(find_alphabet_occurrence_array("hello my name is sparta"))