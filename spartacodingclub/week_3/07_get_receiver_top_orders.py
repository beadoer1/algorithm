top_heights = [6, 9, 5, 7, 4]

def get_receiver_top_orders(heights):
    result = [0]*len(heights) # 뒤에부터 채우는 경우라 0번 index 고정값인 0으로 같은 길이의 list를 만든다.
    while heights:
        height = top_heights.pop()
        for i in range(len(top_heights)-1,0,-1): # 0은 고정값이라 체크 필요 x
            if height < heights[i]:
                result[len(heights)] = i + 1 
                break
    return result


print(get_receiver_top_orders(top_heights))  # [0, 0, 2, 2, 4] 가 반환되어야 한다!