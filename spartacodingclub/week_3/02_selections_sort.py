input = [4, 6, 2, 9, 1]


def selection_sort(array):
    n = len(array)
    for i in range(n-1):
        min = array[i]
        for j in range(i,n): 
            if min > array[j]:
                min = j
        array[i], array[min] = array[min], array[i]
    return array


selection_sort(input)
print(input) # [1, 2, 4, 6, 9] 가 되어야 합니다!