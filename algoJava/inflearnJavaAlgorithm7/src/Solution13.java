// 경로 탐색(인접리스트)
// 방향그래프가 주어지면 1번 정점에서 N번 정점으로 가는 모든 경로의 가지 수를 출력하는 프로그램을 작성하세요.
//
// 입력 설명
// 첫 쨰 줄에는 정점의 수 N(1<=N<=20)와 간선의 수 M이 주어진다. 그 다음부터 M줄에 걸쳐 연결 정보가 주어진다.
//
// 출력 설명
// 총 가지수를 출력한다.
//
// 입력 예제
// 5 9
// 1 2
// 1 3
// 1 4
// 2 1
// 2 3
// 2 5
// 3 4
// 4 2
// 4 5
//
// 출력 예제
// 6


import java.util.ArrayList;
import java.util.Scanner;

public class Solution13 {
    static int n,m,count = 0;
    static ArrayList<ArrayList<Integer>> graph;
    static int[] ch;

    public void DFS(int v) {

        if (v == n) {
            count++;
            return;
        }

        for (int node : graph.get(v)) {
            if (ch[node] == 0) {
                ch[node] = 1;
                DFS(node);
                ch[node] = 0;
            }
        }
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        n = scanner.nextInt();
        m = scanner.nextInt();

        graph = new ArrayList<ArrayList<Integer>>();
        for (int i = 0; i < n; i++) {
            graph.add(new ArrayList<Integer>());
        }

        ch = new int[n + 1];
        for (int i = 0; i < m; i++) {
            int a = scanner.nextInt();
            int b = scanner.nextInt();
            graph.get(a).add(b);
        }

        Solution13 solution13 = new Solution13();
        ch[1] = 1;
        solution13.DFS(1);
        System.out.println("총 가지수 : " + count);
    }
}