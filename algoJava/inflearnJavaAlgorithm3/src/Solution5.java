//5. 연속된 자연수의 합
//설명
//N입력으로 양의 정수 N이 입력되면 2개 이상의 연속된 자연수의 합으로 정수 N을 표현하는 방법의 가짓수를 출력하는 프로그램을 작성하세요.
//만약 N=15이면
//7+8=15
//4+5+6=15
//1+2+3+4+5=15
//와 같이 총 3가지의 경우가 존재한다.
//
//입력
//첫 번째 줄에 양의 정수 N(7<=N<1000)이 주어집니다.
//
//출력
//첫 줄에 총 경우수를 출력합니다.
//
//예시 입력 1
//15
//
//예시 출력 1
//3

import java.util.Scanner;

public class Solution5 {

    public int solution(int n) {
        // my answer : O(n^2)
//        int answer = 0;
//        for (int i = 1; i < n / 2 + 1; i++) {
//            int sum = 0;
//            for (int j = i; j < n / 2 + 2; j++) {
//                sum+=j;
//                if(sum == n){
//                    answer++;
//                    break;
//                } else if (sum > n) {
//                    break;
//                }
//            }
//        }

        // lecture answer : O(n)
        int answer = 0, lt = 0, sum = 0;
        int m = n / 2 + 1;
        int[] arr = new int[m];
        for (int i = 0; i < m; i++) {
            arr[i] = i + 1;
        }
        for (int rt = 0; rt < m; rt++) {
            sum += arr[rt];
            if (sum == n) {
                answer++;
            }
            while (sum >= n) {
                sum -= arr[lt];
                lt++;
                if (sum == n) {
                    answer++;
                }
            }
        }
        return answer;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();

        Solution5 solution5 = new Solution5();
        System.out.println(solution5.solution(n));
    }
}
