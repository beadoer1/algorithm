finding_target = 14
finding_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]


def is_existing_target_number_binary(target, array):
    # 풀이
    low = 0
    high = len(array)-1
    while low <= high:
        mid = (low+high)//2
        if mid == target:
            return True
        elif mid < target:
            low = mid + 1
        else:
            high = mid - 1
    return False
    # 수업 답안 : mid를 값으로 하는 것이 아닌 index로 활용
    low = 0
    high = len(array)-1
    while low <= high:
        mid = (low+high)//2
        if array[mid] == target:
            return True
        elif array[mid] < target:
            high = mid + 1
        else:
            low = mid - 1
    return False



result = is_existing_target_number_binary(finding_target, finding_numbers)
print(result)