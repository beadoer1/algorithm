// 조합 구하기
// 1부터 N까지 번호가 적힌 구슬이 있습니다.
// 이 중 M개를 뽑는 방법을 출력하는 프로그램을 작성하세요.
//
// 입력 설명
// 첫 번째 줄에 자연수 N(3<=N<=10)과 M(2<=M<=N)이 주어집니다.
//
// 출력 설명
// 첫 번째 줄에 결과를 출력합니다.
// 출력 순서는 사전 순으로 오름차순으로 출력합니다.
//
// 입력 예제
// 4 2
//
// 출력 예제
// 1 2
// 1 3
// 1 4
// 2 3
// 2 4
// 3 4

import java.util.Scanner;

public class Solution9 {

    static int n, m;
    static int[] combi;

    // my answer
    public void solution(int L, String answer) {

        if (L == n+1) {
            return;
        }

        if (answer.length() == 4) {
            System.out.println(answer);
            return;
        }

        solution(L + 1, answer + (L + 1) + " ");
        solution(L + 1, answer);
    }

    // lecture answer (외울 것)
    public void DFS(int L, int s) {
        if (L == m) {
            for (int x : combi) {
                System.out.print(x + " ");
            }
            System.out.println();
            return;
        }
        for (int i = s; i <= n; i++) {
            combi[L] = i;
            DFS(L + 1, i + 1);
        }
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        n = scanner.nextInt();
        m = scanner.nextInt();

        combi = new int[m];

        Solution9 solution9 = new Solution9();
        solution9.solution(0,"");
        solution9.DFS(0, 1);
    }
}
