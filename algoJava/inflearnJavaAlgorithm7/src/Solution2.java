// 재귀함수를 이용한 이진수 출력
// 10진수 N이 입력되면 2진수로 변환하여 출력하는 프로그램을 작성하세요.
// 단 재귀함수를 이용해서 출력해야 합니다.
//
// 입력설명
// 첫 번째 줄에 10진수 N(1<=N<=1000)이 주어집니다.
//
// 출력설명
// 첫 번째 줄에 이진수를 출력하세요.
//
// 입력예제 - 11 , 출력예제 - 1011

import java.util.Scanner;

public class Solution2 {

    // 결과값 반환
    public String solution(int n, String result) {
        if (n == 1) {
            return result + 1;
        }
        result = solution(n/2,result) + n % 2;
        return result;
    }

    // 바로 출력
//    public void solution(int n) {
//        if (n == 1) {
//            System.out.print(n);
//            return;
//        }
//        solution(n / 2);
//        System.out.print(n % 2);
//    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        String result = "";

        Solution2 solution2 = new Solution2();
        System.out.println(solution2.solution(n,result));
//        solution2.solution(n);
    }
}
