input = [3, 5, 6, 1, 2, 4]


def find_max_num(array):
    # 풀이
    _max = 0
    for i in array:
        if i > _max:
            _max = i
    return _max

result = find_max_num(input)
print(result)

# 수업 답안 1
def find_max_num(array):
    for num in array:
        for compare_num in array:
            if num < compare_num:
                break
        else:
            return num

result = find_max_num(input)
print(result)

# 수업 답변 2
def find_max_num(array):
    max_num = array[0]
    for num in array:
        if num > max_num:
            max_num = num    
    return max_num

result = find_max_num(input)
print(result)