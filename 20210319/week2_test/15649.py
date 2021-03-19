# 문제
# 자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.
# 1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열
# 입력
# 첫째 줄에 자연수 N과 M이 주어진다. (1 ≤ M ≤ N ≤ 8)
# 출력
# 한 줄에 하나씩 문제의 조건을 만족하는 수열을 출력한다. 
# 중복되는 수열을 여러 번 출력하면 안되며, 각 수열은 공백으로 구분해서 출력해야 한다.
# 수열은 사전 순으로 증가하는 순서로 출력해야 한다.

# 설명 : 1~N의 숫자로 이루어진(중복 X) M의 길이를 가진 수열들을 오름차순 출력 
# n,m 을 입력 받았을 때 
for i in range(1,n+1): 
    print(i, end = ' ')
    for j in range(1,n+1):
        if j == i:
            continue
        print(j, end = ' ')
        for k in range(1,n+1):
            if k == i or k == j:
                continue
            print(k, end = ' ')
            for l in range(1,n+1):
                if l == i or l == j or l == k:
                    continue
                print(l, end = ' ')
                ...
                ...
                # m번 만큼 (재귀의 탈출 조건)

# 풀이
import sys

def print_all_seq(visited_arr,n,m):
    # 탈출 조건
    if len(visited_arr) == m: # m개의 자릿수를 모두 채웠을 때 탈출한다.
        print(' '.join(map(str,visited_arr)))
        return
    # mutable

    for i in range(1,n+1):
        if i in visited_arr:
            continue
        visited_arr.append(i) # 이미 사용한 값을 넣은 list를 주고 받는 과정이 가장 어려웠다.
        print_all_seq(visited_arr,n,m)
        visited_arr.pop() # list 는 mutual 특성을 갖는 자료형으로 

N,M = map(int,sys.stdin.readline().split())
print_all_seq([],N,M)


# immutable(str) 15650 문제 풀이
import sys
# 1,3 -> 2,4 -> 3,5 -> 4,6 -> 5,7 -> 6,8(출력)    # start_num, max_num
def back_track(_str,start_num,max_num,n):        # str은 결과 출력,n은 재귀 종료 조건을 만들기 위함
    if  max_num == n:                            # 재귀 종료 조건 : max_num이 가장 끝 숫자와 같아지는 경우
        for i in range(start_num,max_num+1):
            print(_str+str(i))                   # 여태까지 더해 온 결과값을 출력
        return    
    # immutable
    tmp = _str   -> tmp = '1' , _str = '1,2'
    for i in range(start_num,(max_num)+1):       # 수열의 첫 번째 수를 결정
        _str = _str + str(i) + ' '
        back_track(_str,i+1,max_num+1,n)         # 수열의 다음 번째 수를 결정하기 위한 재귀
        _str = tmp
    return

N,M = map(int,sys.stdin.readline().split())
max_possible_num = N-M+1
back_track('',1,max_possible_num,N)