// 중복 순열 구하기
// 1부터 N까지 번호가 적힌 구슬이 있습니다.
// 이 중 중복을 허락하여 M번을 뽑아 일렬로 나열하는 방법을 모두 출력합니다.
//
// 입력 설명
// 첫 번째 자연수 N(3<=N<=10)과 M(2<=M<=N)이 주어집니다.
//
// 출력 설명
// 첫 번째 줄에 결과를 출력합니다.
// 출력 순서는 사전 순으로 오름차순으로 출력합니다.

import java.util.Scanner;

public class Solution4 {

    public void solution(int L, int n, int m, int[] arr) {

        if (L == m) {
            for (int i = 0; i < m; i++) {
                System.out.print(arr[i] + " ");
            }
            System.out.println();
            return;
        }

        for (int i = 1; i <= n; i++) {
            arr[L] = i;
            solution(L + 1, n, m, arr);
        }
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        int m = scanner.nextInt();

        int[] arr = new int[m];
        Solution4 solution4 = new Solution4();
        solution4.solution(0, n, m, arr);
    }
}
