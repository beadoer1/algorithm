//5. 소수(에라토스테네스 체)
//설명
//자연수 N이 입력되면 1부터 N까지의 소수의 개수를 출력하는 프로그램을 작성하세요.
//만약 20이 입력되면 1부터 20까지의 소수는 2, 3, 5, 7, 11, 13, 17, 19로 총 8개입니다.
//
//입력
//첫 줄에 자연수의 개수 N(2<=N<=200,000)이 주어집니다.
//
//출력
//첫 줄에 소수의 개수를 출력합니다.
//
//예시 입력 1
//20
//
//예시 출력 1
//8

import java.util.Scanner;

public class Solution5 {

    public int solution(int n){
        int answer=0;
        // my answer(128ms)
//        int[] primeNums = new int[n+1];
//        for (int i = 2; i < Math.sqrt(n)+1; i++) {
//            if (primeNums[i] == 0) {
//                for (int j = 2; i * j <= n; j++) {
//                    primeNums[i*j] = 1;
//                }
//            }
//        }
//
//        for (int k = 2; k < n; k++) {
//            if (primeNums[k] == 0) {
//                answer++;
//            }
//        }

        // lecture answer(120ms)
        int[] numArr = new int[n + 1];
        for (int i = 2; i < n + 1; i++) {
            if(numArr[i] == 0){
                answer++;
                for (int j = i; j < n + 1; j=j+i) {
                    numArr[j] = 1;
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
