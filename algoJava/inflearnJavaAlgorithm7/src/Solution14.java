// 그래프 최단 거리(BFS)
// 주어지는 연결정보를 통해 1번 정점에서 각 정점으로 가는 최소 이동 간선수를 출력하세요.
//
// 입력 설명
// 첫 째 줄에는 정점의 수 N(1<=N<=20)과 간선의 수 M이 주어진다.
// 그 다음부터 M줄에 걸쳐 연결정보가 주어진다.
//
// 출력 설명
// 1번 정점에서 각 정점으로 가는 최소 간선수를 2번 정점부터 차례대로 출력하세요.
//
// 입력 예시
// 6 9
// 1 3
// 1 4
// 2 1
// 2 5
// 3 4
// 4 5
// 4 6
// 6 2
// 6 5

// 출력 예시
// 3 1 1 2 2

import java.util.*;

public class Solution14 {
    // my answer
    static Map<Integer, ArrayList<Integer>> graph;
    static int[] answer;

    public int[] BFS_mine(int n) {
        int level = 0;
        Queue<Integer> Q = new LinkedList<>();
        Q.offer(n);
        while (!Q.isEmpty()) {
            int len = Q.size();
            for (int i = 0; i < len; i++) {
                int cur = Q.poll();
                for(int node : graph.get(cur)){
                    if (answer[node] == 0) {
                        Q.offer(node);
                        answer[node] = level + 1;
                    }
                }
            }
            level++;
        }
        return answer;
    }

    // lecture answer
    static ArrayList<ArrayList<Integer>> graph_l;
    static int[] dis;
    static int[] ch;

    public void BFS_l(int v) {
        Queue<Integer> queue = new LinkedList<>();
        ch[v] = 1;
        dis[v] = 0;
        queue.offer(v);
        while (!queue.isEmpty()) {
            int cv = queue.poll();
            for (int nv : graph_l.get(cv)) {
                if (ch[nv] == 0) {
                    ch[nv] = 1;
                    queue.offer(nv);
                    dis[nv] = dis[cv] + 1;
                }
            }

        }

    }


    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        int m = scanner.nextInt();

        graph = new HashMap<>();
        graph_l = new ArrayList<>();
        for (int i = 0; i < n+1; i++) {
            graph.put(i, new ArrayList<>());
            graph_l.add(new ArrayList<>());
        }
        for (int i = 0; i < m; i++) {
            int a = scanner.nextInt();
            int b = scanner.nextInt();
            graph.get(a).add(b);
            graph_l.get(a).add(b);
        }
        // my answer
        answer = new int[n + 1];
        Solution14 solution14 = new Solution14();
        answer = solution14.BFS_mine(1);
        System.out.println("== My answer ==");
        for (int i = 2; i < n+1; i++) {
            System.out.println(i + " : " + answer[i]);
        }
        // lecture answer
        ch = new int[n + 1];
        dis = new int[n + 1];
        solution14.BFS_l(1);
        System.out.println("== Lecture answer ==");
        for (int i = 2; i < n + 1; i++) {
            System.out.println(i + " : " + dis[i]);
        }
    }
}
