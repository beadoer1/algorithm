# 순차적으로 더하거나 곱해서 최대값을 뽑아내는 실습
# 'num 혹은 multiply_sum이 1 혹은 0일 때는 더해주는 것이 유리하다.' Point!

input = [0, 3, 5, 6, 1, 2, 4]

def find_max_plus_or_multiply(array):
    # 수업 답안
    multiply_sum = 0
    for num in input:
        if num <= 1 or multiply_sum <= 1:
            multiply_sum += num
        else:
            multiply_sum *= num
    return multiply_sum

result = find_max_plus_or_multiply(input)
print(result)