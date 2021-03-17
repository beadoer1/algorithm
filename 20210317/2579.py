# 문제
# 계단 오르기 게임은 계단 아래 시작점부터 계단 꼭대기에 위치한 도착점까지 가는 게임이다. 
# <그림 1>과 같이 각각의 계단에는 일정한 점수가 쓰여 있는데 계단을 밟으면 그 계단에 쓰여 있는 점수를 얻게 된다.
# 예를 들어 <그림 2>와 같이 시작점에서부터 첫 번째, 두 번째, 네 번째, 여섯 번째 계단을 밟아 도착점에 도달하면 총 점수는 10 + 20 + 25 + 20 = 75점이 된다.
# 계단 오르는 데는 다음과 같은 규칙이 있다.
#   1. 계단은 한 번에 한 계단씩 또는 두 계단씩 오를 수 있다. 즉, 한 계단을 밟으면서 이어서 다음 계단이나, 다음 다음 계단으로 오를 수 있다.
#   2. 연속된 세 개의 계단을 모두 밟아서는 안 된다. 단, 시작점은 계단에 포함되지 않는다.
#   3. 마지막 도착 계단은 반드시 밟아야 한다.
# 따라서 첫 번째 계단을 밟고 이어 두 번째 계단이나, 세 번째 계단으로 오를 수 있다. 
# 하지만, 첫 번째 계단을 밟고 이어 네 번째 계단으로 올라가거나, 첫 번째, 두 번째, 세 번째 계단을 연속해서 모두 밟을 수는 없다.
# 각 계단에 쓰여 있는 점수가 주어질 때 이 게임에서 얻을 수 있는 총 점수의 최댓값을 구하는 프로그램을 작성하시오.
# 입력
# 입력의 첫째 줄에 계단의 개수가 주어진다.
# 둘째 줄부터 한 줄에 하나씩 제일 아래에 놓인 계단부터 순서대로 각 계단에 쓰여 있는 점수가 주어진다. 
# 계단의 개수는 300이하의 자연수이고, 계단에 쓰여 있는 점수는 10,000이하의 자연수이다.
# 출력
# 첫째 줄에 계단 오르기 게임에서 얻을 수 있는 총 점수의 최댓값을 출력한다.

# 풀이 1: 첫 계단을 무조건 밟아야된다고 착각했다. 아래는 첫 출발을 0 or 1로 할 수 있는 경우.(정답)
import sys

memo = {}
#     0 > 2     return step[0]  
#     1 > 2     return step[1] 
#     0 > 1 > 3 return step[0] + step[1]
def find_max_step(in_n,step_li,check_n):
    if in_n == 0:
        result = step_li[0]
        return result
    elif in_n == 1:
        if check_n == 2:
            result = step_li[in_n] + step_li[0]
            memo[(in_n,check_n)] = result
        else:
            result = step_li[1]
        return result
    elif (in_n,check_n) in memo:
        return memo[(in_n,check_n)]
    else:
        if check_n == 2:
            result = step_li[in_n] + max(find_max_step(in_n-1,step_li,1),find_max_step(in_n-2,step_li,2))
            memo[(in_n,check_n)] = result
        else:
            result = step_li[in_n] + find_max_step(in_n-2,step_li,2)
            memo[(in_n,check_n)] = result
        return result

steps = int(sys.stdin.readline())
step_score = []
for i in range(steps):
    score = int(sys.stdin.readline())
    step_score.append(score)
max_index = len(step_score)-1
print(find_max_step(max_index,step_score,2))

# 풀이 2: 다른 사람 풀이
n = int(input())
s = [0 for i in range(301)]     #계단을 300칸까지 미리 짜놓고                                 
dp = [0 for i in range(301)]    #층별 최고값(dp)을 넣기위한 틀도 300칸까지 미리 만들어둠                                  
for i in range(n):
    s[i] = int(input())         # 입력되는 계단 점수를 층별 인덱스 s 에 차곡차곡 담음                                   
dp[0] = s[0]                    # 1번째칸에서 최댓값(dp[0]) 은 그냥 1번째 칸(s[0]) 이니까 진행                                 
dp[1] = s[0] + s[1]             # 2번째칸에서 최댓값은 1번째와 2번째 두개 다밟으면 최대니까 진행  

# 여기서부터 비교 들어간다. 3번째칸부터는 2번째+3번째 값 vs 1번째+3번째 둘중 큰거(기준은 2번째칸 밟았는지아닌지임!)
dp[2] = max(s[1] + s[2], s[0] + s[2])          

#마찬가지로 찾고자하는 계단의 전 n-1계단을 밟은경우와 아닌경우를 넣고 비교해서 큰값을 입력
for i in range(3, n):
    dp[i] = max(dp[i - 3] + s[i - 1] + s[i], dp[i - 2] + s[i])    
print(dp[n - 1])
