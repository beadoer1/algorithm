array_a = [1, 2, 3, 5]
array_b = [4, 6, 7, 8]

def merge1(array1, array2):
    # 풀이
    n,m = len(array1),len(array2)
    array_result = []
    for i in range(n):
        for j in range(m):
            if array1[i] < array2[j]:
                array_result.append(array1[i])
                if i == n-1:
                    for k in range(j,n):
                        array_result.append(array2[k]) 
                break
            elif array1[i] > array2[j]:
                array_result.append(array2[j])
            else:
                array_result.append(array1[i])
                array_result.append(array2[j])
    return array_result

print(merge1(array_a, array_b))  # [1, 2, 3, 4, 5, 6, 7, 8] 가 되어야 합니다!

def merge2(array1, array2):
    array1_in = 0
    array2_in = 0
    array_result = []
    while array1_in < len(array1) and array2_in < len(array2):
        if array1[array1_in] < array2[array2_in]:
            array_result.append(array1[array1_in])
            array1_in += 1
        else:
            array_result.append(array2[array2_in])
            array2_in += 1
    if array1_in == len(array1):
        while array2_in < len(array2):
            array_result.append(array2[array2_in])
            array2_in += 1
    elif array2_in == len(array2):
        while array1_in < len(array1):
            array_result.append(array1[array1_in])
            array1_in += 1
    return array_result

print(merge2(array_a, array_b)) 