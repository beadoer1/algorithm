# 문제
# 상근이는 요즘 설탕공장에서 설탕을 배달하고 있다. 
# 상근이는 지금 사탕가게에 설탕을 정확하게 N킬로그램을 배달해야 한다. 
# 설탕공장에서 만드는 설탕은 봉지에 담겨져 있다. 봉지는 3킬로그램 봉지와 5킬로그램 봉지가 있다.
# 상근이는 귀찮기 때문에, 최대한 적은 봉지를 들고 가려고 한다. 
# 예를 들어, 18킬로그램 설탕을 배달해야 할 때, 3킬로그램 봉지 6개를 가져가도 되지만, 
# 5킬로그램 3개와 3킬로그램 1개를 배달하면, 더 적은 개수의 봉지를 배달할 수 있다.
# 상근이가 설탕을 정확하게 N킬로그램 배달해야 할 때, 봉지 몇 개를 가져가면 되는지 그 수를 구하는 프로그램을 작성하시오.
# 입력
# 첫째 줄에 N이 주어진다. (3 ≤ N ≤ 5000)
# 출력
# 상근이가 배달하는 봉지의 최소 개수를 출력한다. 만약, 정확하게 N킬로그램을 만들 수 없다면 -1을 출력한다.

# 풀이 1: /5, %5, /3, %3 를 이용해 풀어보자.
import sys
def cal_min_plastic_bag(num): 
    division_5 = num // 5
    if num % 5 == 0:
        return division_5
    else:  
        while division_5 >= 0:      
            if division_5 == 0:
                if num % 3 == 0:
                    return num//3
                else:
                    return -1
            else:
                num_check_3 = num - (5*division_5)
                division_3 = num_check_3 // 3
                remainder_3 = num_check_3 % 3
                if remainder_3 == 0:
                    return division_5+division_3
                division_5 = division_5 - 1
    return -1
    
num_salt = int(input())
print(cal_min_plastic_bag(num_salt))

k = int(input())
if k % 5 == 0:
    print(int(k/5))
else:
    count = 0
    while k >= 0:
        k = k - 3
        count += 1 # 3키로 봉지를 추가
        if k % 5 == 0:
            print(int(k/5) + count)
            break
    if k % 5 != 0:
        print(-1)


N = int(input())
box = 0
while True:
    if N % 5 == 0:
        box = box + N//5
        print(box)
        break
    N -= 3
    box += 1
    if N < 0:
        print(-1)
        break