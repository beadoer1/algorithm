input = "hello my name is sparta"

def find_max_occurred_alphabet(string):
    array_num = [0]*26
    for char in string:
        if char.isalpha():
            index = ord(char) - ord('a')
            array_num[index] += 1
    max_index = 0
    index = 0
    max_num = -1
    for num in array_num:
        if num > max_num:
            max_num = num
            max_index = index
        index += 1     
    return chr(max_index + 97)

result = find_max_occurred_alphabet(input)
print(result)

# 수업 답안 1
input = "hello my name is sparta"

def find_max_occurred_alphabet(string):
    alphabet_array = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n",
                    "o","p","q","r","s","t","u","v","w","x","y","z",]
    max_occurrence = 0
    max_alphabet = alphabet_array[0]

    for alphabet in alphabet_array:
        occurrence = 0
        for char in string:
            if char == alphabet:
                occurrence += 1
        if occurrence > max_occurrence:
            max_occurrence = occurrence
            max_alphabet = alphabet
    return max_alphabet
            
result = find_max_occurred_alphabet(input)
print(result)

# 수업 답안 2
input = "hello my name is sparta"

def find_alphabet_occurrence_array(string):
    alphabet_occurrence_array = [0] * 26
    # 풀이
    for char in string:
        if not char.isalpha(): # alphabet 인지 구분하는 내장함수
            continue
        arr_index = ord(char)-ord("a")
        alphabet_occurrence_array[arr_index] += 1
    max_occurrence = 0
    max_alphabet_index = 0
    for index in range(len(alphabet_occurrence_array)):
        if alphabet_occurrence_array[index] > max_occurrence:
            max_occurrence = alphabet_occurrence_array[index]
            max_alphabet_index = index
    return chr(alphabet_occurrence_array[index]+ord('a'))
    
print(find_alphabet_occurrence_array("hello my name is sparta"))

