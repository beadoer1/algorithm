# 문제
# 재귀 호출만 생각하면 신이 난다! 아닌가요?
# 다음과 같은 재귀함수 w(a, b, c)가 있다.
# if a <= 0 or b <= 0 or c <= 0, then w(a, b, c) returns:
#     1
# if a > 20 or b > 20 or c > 20, then w(a, b, c) returns:
#     w(20, 20, 20)
# if a < b and b < c, then w(a, b, c) returns:
#     w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
# otherwise it returns:
#     w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
# 위의 함수를 구현하는 것은 매우 쉽다. 하지만, 그대로 구현하면 값을 구하는데 매우 오랜 시간이 걸린다. 
# (예를 들면, a=15, b=15, c=15)\
# a, b, c가 주어졌을 때, w(a, b, c)를 출력하는 프로그램을 작성하시오.
# 입력
# 입력은 세 정수 a, b, c로 이루어져 있으며, 한 줄에 하나씩 주어진다. 
# 입력의 마지막은 -1 -1 -1로 나타내며, 세 정수가 모두 -1인 경우는 입력의 마지막을 제외하면 없다.
# 출력
# 입력으로 주어진 각각의 a, b, c에 대해서, w(a, b, c)를 출력한다.
# 제한
# -50 ≤ a, b, c ≤ 50

# 풀이 1 : 아...return 은 하나의 함수 전체를 빠져나간다 그러므로 함수 한 번에 단 한 번만 작동한다...
# 하여 return으로 나오는 함수의 반환값은 하나이므로 이름을 처음 들어가는 abc로 해도 상관없다...
# 메모리 : 29724 KB, 시간 : 160ms
import sys
memo = {

}
def w(a,b,c):
    if a <= 0 or b <= 0 or c <= 0:
        memo[str(0)+'_'+str(0)+'_'+str(0)] = 1
        return memo[str(0)+'_'+str(0)+'_'+str(0)]
    if a > 20 or b > 20 or c > 20:
        memo[str(20)+'_'+str(20)+'_'+str(20)] = w(20, 20, 20)
        return memo[str(20)+'_'+str(20)+'_'+str(20)]
    if a < b and b < c:
        # w(a, b, c-1)
        if str(a)+'_'+str(b)+'_'+str(c-1) not in memo:
            w_1 = w(a, b, c-1)
            memo[str(a)+'_'+str(b)+'_'+str(c-1)] = w_1
        else:
            w_1 = memo[str(a)+'_'+str(b)+'_'+str(c-1)]
        
        # w(a, b-1, c-1)
        if str(a)+'_'+str(b-1)+'_'+str(c-1) not in memo:
            w_2 = w(a, b-1, c-1)
            memo[str(a)+'_'+str(b-1)+'_'+str(c-1)] = w_2
        else:
            w_2 = memo[str(a)+'_'+str(b-1)+'_'+str(c-1)]
        
        # w(a, b-1, c)    
        if str(a)+'_'+str(b-1)+'_'+str(c) not in memo:
            w_3 = w(a, b-1, c)
            memo[str(a)+'_'+str(b-1)+'_'+str(c)] = w_3
        else:
            w_3 = memo[str(a)+'_'+str(b-1)+'_'+str(c)]
        
        result_w = w_1 + w_2 - w_3
        return result_w
    else:
        #  w(a-1, b, c) 
        if str(a-1)+'_'+str(b)+'_'+str(c) not in memo:
            w_1 = w(a-1, b, c)
            memo[str(a-1)+'_'+str(b)+'_'+str(c)] = w_1
        else:
            w_1 = memo[str(a-1)+'_'+str(b)+'_'+str(c)]
        # w(a-1, b-1, c)
        if str(a-1)+'_'+str(b-1)+'_'+str(c) not in memo:
            w_2 = w(a-1, b-1, c)
            memo[str(a-1)+'_'+str(b-1)+'_'+str(c)] = w_2
        else:
            w_2 = memo[str(a-1)+'_'+str(b-1)+'_'+str(c)]

        # w(a-1, b, c-1)   
        if str(a-1)+'_'+str(b)+'_'+str(c-1) not in memo:
            w_3 = w(a-1, b, c-1)
            memo[str(a-1)+'_'+str(b)+'_'+str(c-1)] = w_3
        else:
            w_3 = memo[str(a-1)+'_'+str(b)+'_'+str(c-1)]
        
        # w(a-1, b-1, c-1) 
        if str(a-1)+'_'+str(b-1)+'_'+str(c-1) not in memo:
            w_4 = w(a-1, b-1, c-1)
            memo[str(a-1)+'_'+str(b-1)+'_'+str(c-1)] = w_4
        else:
            w_4 = memo[str(a-1)+'_'+str(b-1)+'_'+str(c-1)]

        return_w = w_1 + w_2 + w_3 - w_4
        return return_w

while True:
    a,b,c = map(int,sys.stdin.readline().split())
    if a == -1 and b == -1 and c == -1:
        break
    print("w("+str(a)+", "+str(b)+", "+str(c)+") = "+str(w(a,b,c)))

# 풀이 2: 풀이 1에 대한 고찰과 보다 빠른 코드 관찰 후 재작성.. 미쳤네 미쳤어...ㅠ
# 꼭 기억하자. 함수의 반환값은 하나다.
# 메모리 : 29724 KB, 시간 : 128 ms
import sys
memo = {}
def w(a,b,c):
    result_str = str(a)+'_'+str(b)+'_'+str(c)
    if result_str in memo:
        return memo[result_str]
    if a <= 0 or b <= 0 or c <= 0: 
        return 1
    if a > 20 or b > 20 or c > 20:
        result = w(20, 20, 20)
        return result
    if a < b and b < c:
        result = w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
        memo[result_str] = result
        return result
    else:
        result = w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
        memo[result_str] = result
        return result

while True:
    a,b,c = map(int,sys.stdin.readline().split())
    if a == -1 and b == -1 and c == -1:
        break
    print("w("+str(a)+", "+str(b)+", "+str(c)+") = "+str(w(a,b,c)))