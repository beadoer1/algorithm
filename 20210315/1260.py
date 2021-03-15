# 문제
# 그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오. 
# 단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고, 더 이상 방문할 수 있는 점이 없는 경우 종료한다. 
# 정점 번호는 1번부터 N번까지이다.
# 입력
# 첫째 줄에 정점의 개수 N(1 ≤ N ≤ 1,000), 간선의 개수 M(1 ≤ M ≤ 10,000), 탐색을 시작할 정점의 번호 V가 주어진다. 
# 다음 M개의 줄에는 간선이 연결하는 두 정점의 번호가 주어진다. 어떤 두 정점 사이에 여러 개의 간선이 있을 수 있다. 입력으로 주어지는 간선은 양방향이다.
# 출력
# 첫째 줄에 DFS를 수행한 결과를, 그 다음 줄에는 BFS를 수행한 결과를 출력한다. V부터 방문된 점을 순서대로 출력하면 된다.

# 풀이 1: '시간 초과' 아무래도 반복문도 2중으로 되어있고, sort도 두 번씩 해서 그런거 같다. 줄여보자
#        + 해당 DFS 방식은 node를 쌓아놓지 않고 선을 따라가다 보니 다시 돌아올 곳이 없어서 '틀렸습니다.'가 나오는 듯 하다.
# import sys
# graph = {} # 전체 간선을 표시하기 위한 dict
# visited_dfs = []  # 방문한 정점을 넣기 위한 list
# visited_bfs = []
# def run_dfs(n,graph): # n: 탐색을 시작할 정점의 번호, 탐색할 간선 표시된 dict 
#     to_visit = [n]
#     while to_visit:
#         current_visit = to_visit.pop() 
#         visited_dfs.append(current_visit)
#         while len(visited_dfs) < len(graph):
#             next_node = graph[current_visit].pop(0) # 0번째 index를 꺼내줌(낮은 것 부터 접근하기 위함)
#             graph[current_visit].append(next_node) # 꺼내서 봤으니까 뒤에 다시 넣어줌(BFS 할 때도 봐야하니까.)
#             if next_node not in visited_dfs and next_node not in to_visit:
#                 to_visit.append(next_node)
#                 break
#     return visited_dfs

# def run_bfs(n,graph):
#     to_visit = [n]
#     while to_visit:
#         current_visit = to_visit.pop(0) # 추가된 순으로 돌아보기 위해 0번 index를 pop
#         visited_bfs.append(current_visit)
#         for node in graph[current_visit]:
#             if node not in visited_bfs and node not in to_visit:
#                 # BFS 에서는 queue를 이용해 넣은 순서대로 방문하므로써 너비를 우선으로 할 수 있다.
#                 to_visit.append(node)
#     return visited_bfs

# N,M,V= map(int,sys.stdin.readline().split())
# for i in range(M):
#     n_1,n_2 = map(int,sys.stdin.readline().split())
#     if n_1 not in graph:
#         graph[n_1] = [n_2]
#     else:
#         graph[n_1].append(n_2)
#     if n_2 not in graph:
#         graph[n_2] = [n_1]
#     else:
#         graph[n_2].append(n_1)
# graph_keys = graph.keys()
# for j in graph_keys:
#     graph[j].sort() # 작은 수에 먼저 접근하기 위한 정렬
# print(run_dfs(V,graph))
# for j in graph_keys:
#     graph[j].sort() # BFS에서도 작은 수에 먼저 접근하기 위한 정렬(DFS할 때 graph를 건드림)
# print(run_bfs(V,graph))

# 풀이 2: DFS 누락 가능성을 없애 보았다. '런타임 에러'가 뜬다.
import sys

graph = {} # 전체 간선을 표시하기 위한 dict
visited_dfs = []  # 방문한 정점을 넣기 위한 list
visited_bfs = []

def run_dfs(n,graph_node): # n: 탐색을 시작할 정점의 번호, graph_node: 탐색할 간선 표시된 dict 
    to_visit = [n]
    if n not in graph_node: # ★★★★★ 노드에 간선이 없는 경우를 고려해야 한다. ★★★★★
        visited_dfs.append(n)
        return
    while to_visit:
        current_visit = to_visit.pop() 
        visited_dfs.append(current_visit)
        for i in range(len(graph_node[current_visit])-1,-1,-1): # 낮은 수부터 접근하기 위해 뒤부터 탐색하여 추가
            node = graph_node[current_visit][i]
            if node in to_visit: # 깊이 우선 탐색을 위해 단계 별로 연결되어있는 노드를 제일 뒤로 보냄
                to_visit.remove(node)
                to_visit.append(node)
            elif graph_node[current_visit][i] not in visited_dfs:
                to_visit.append(node)
    return

def run_bfs(n,graph_node):
    to_visit = [n]
    if n not in graph_node:
        visited_bfs.append(n)
        return
    while to_visit:
        current_visit = to_visit.pop(0) # 추가된 순으로 돌아보기 위해 0번 index를 pop
        visited_bfs.append(current_visit)
        for node in graph_node[current_visit]:
            if node not in visited_bfs and node not in to_visit: # 오름차순 정렬되어있어 순서대로 탐색하면 된다.
                # BFS 에서는 queue를 이용해 넣은 순서대로 방문하므로써 너비를 우선으로 할 수 있다.
                to_visit.append(node)
    return

N,M,V= map(int,sys.stdin.readline().split())
for i in range(M):
    n_1,n_2 = map(int,sys.stdin.readline().split())
    if n_1 not in graph:
        graph[n_1] = [n_2]
    else:
        graph[n_1].append(n_2)

    if n_2 not in graph:
        graph[n_2] = [n_1]
    else:
        graph[n_2].append(n_1)

graph_keys = graph.keys()

for j in graph_keys:
    graph[j].sort() # 작은 수에 먼저 접근하기 위한 정렬

run_dfs(V,graph)
run_bfs(V,graph)

result_1 = map(str,visited_dfs)
result_2 = map(str,visited_bfs)

print(' '.join(result_1))
print(' '.join(result_2))

