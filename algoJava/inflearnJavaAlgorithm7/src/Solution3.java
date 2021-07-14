// 팩토리얼
// 자연수 N이 입력되면 N!를 구하는 프로그램을 작성하세요.
// 예를 들어 5! = 5*4*3*2*1 = 120 입니다.
//
// 입력설명
// 첫 번째 줄에 자연수 N(1<=N<=100)이 주어집니다.
//
// 출력설명
// 첫 번째 줄에 N! 값을 출력합니다.

import java.util.Scanner;

public class Solution3 {

    public int solution(int n) {

        if (n == 1) {
            return 1;
        }
        return n * solution(n - 1);
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();

        Solution3 solution3 = new Solution3();
        System.out.println(solution3.solution(n));
    }
}
