//5. 동전교환
//설명
//다음과 같이 여러 단위의 동전들이 주어져 있을때 거스름돈을 가장 적은 수의 동전으로 교환해주려면 어떻게 주면 되는가?
//각 단위의 동전은 무한정 쓸 수 있다.
//
//입력
//첫 번째 줄에는 동전의 종류개수 N(1<=N<=12)이 주어진다. 두 번째 줄에는 N개의 동전의 종류가 주어지고,
//그 다음줄에 거슬러 줄 금액 M(1<=M<=500)이 주어진다.각 동전의 종류는 100원을 넘지 않는다.
//
//출력
//첫 번째 줄에 거슬러 줄 동전의 최소개수를 출력한다.
//
//예시 입력 1
//3
//1 2 5
//15
//
//예시 출력 1
//3
//
// ※ 무조건 큰 동전으로 내보내는게 좋은 것이 아니다. 동전의 수가 여러개이니 만큼 최소 개수를 뽑는 경우가 많다.
// ex ) 3개(1, 5, 12) 의 동전으로 15를 뽑는 방법은 5*3이지 12*1+1*3이 아니다.

import java.util.Scanner;

public class Solution5 {

    static int n, m, minCoins = Integer.MAX_VALUE;
    static int[] coins;

    // My answer
    public void solution(int idx, int sum, int numCoins) {

        if (sum > m || numCoins > minCoins) {
            return;
        }

        if (idx == n) {
            if (sum == m) {
                minCoins = Math.min(minCoins, numCoins);
            }
            return;
        }

        int idxEnd = m / coins[idx];
        for (int i = 0; i <= idxEnd; i++) {
            solution(idx + 1, sum + (i * coins[idx]), numCoins + i);
        }

    }

    // Lecture answer (time limit error ^^;; main에서 sort(내림차순) 해서 큰 수부터 넣어주면 통과)
    public void DFS(int numCoins, int sum) {
        if (sum > m || numCoins >= minCoins) {
            return;
        }
        if (sum == m) {
            minCoins = Math.min(minCoins, numCoins);
            return;
        }
        for (int i = 0; i < n; i++) {
            DFS(numCoins + 1, sum + coins[i]);
        }
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        n = scanner.nextInt();

        coins = new int[n];
        for (int i = 0; i < n; i++) {
            coins[i] = scanner.nextInt();
        }

        m = scanner.nextInt();

        Solution5 solution5 = new Solution5();
        solution5.solution(0,0,0);
        System.out.println(minCoins);
        minCoins = Integer.MAX_VALUE;
        solution5.DFS(0, 0);
        System.out.println(minCoins);
    }
}
