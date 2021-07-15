// 경로 탐색 (인접 행렬)
// 방향 그래프가 주어지면 1번 정점에서 N번 정점으로 가는 모든 경로의 가지 수를 출력하는 프로그램을 작성하세요.
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

import java.util.Scanner;
import java.util.Stack;

public class Solution12 {

    static int n,m,count = 0;
    static int[][] graph;
    static Stack<Integer> printStack = new Stack<>(); // 경로 출력 안한다고 하면 배열 사용하는게 더 빠를 듯. 실제 수업에서는 int[] ch 사용.


    public void solution(int cur) {

        if (cur == n) {
            for (int i : printStack) {
                System.out.print(i + " ");
            }
            System.out.println();
            count++;
            return;
        }

        if (cur == 1 && !printStack.contains(1)) {
            printStack.push(1);
        }

        for (int i = 1; i < n + 1; i++) {
            if(printStack.contains(i)){
                continue;
            }else if(graph[cur][i] != 0){
                printStack.push(i);
                solution(i);
                printStack.pop();

            }
        }
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        n = scanner.nextInt();
        m = scanner.nextInt();

        graph = new int[n + 1][n + 1];
        for (int i = 0; i < m; i++) {
            int a = scanner.nextInt();
            int b = scanner.nextInt();

            graph[a][b] = 1;
        }

        Solution12 solution12 = new Solution12();
        solution12.solution(1);
        System.out.println("총 가지수 : " + count);
    }
}
