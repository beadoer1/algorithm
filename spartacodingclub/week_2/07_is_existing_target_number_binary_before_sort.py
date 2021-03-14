# 정렬되지 않은 숫자에 대해서는 정렬을 한 후에 진행해줘야 한다!!

finding_target = 2
finding_numbers = [0, 3, 5, 6, 1, 2, 4]

def is_exist_target_number_binary(target, numbers):
    # 풀이
    numbers.sort()
    low = 0
    high = len(numbers)-1
    while low <= high:
        mid = (low+high)//2
        if numbers[mid] == target:
            return True
        elif numbers[mid] > target:
            high = mid - 1
        else:
            numbers[mid] < target
            low = mid + 1
    return False


result = is_exist_target_number_binary(finding_target, finding_numbers)
print(result)