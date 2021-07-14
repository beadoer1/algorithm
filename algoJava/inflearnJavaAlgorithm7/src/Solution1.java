// 재귀함수
// 자연수 N이 입력되면 재귀함수를 이용하여 1부터 N까지 출력하는 프로그램을 작성하세요.
//
// 입력 설명
// 첫 번째 줄은 정수 N(3<=N<=10)이 입력도니다.
//
// 출력 설명
// 첫 째 줄에 출력한다.
//
// 입력 예제 - 3 , 출력 예제 - 1 2 3

import java.util.ArrayList;
import java.util.Scanner;
import java.util.List;

public class Solution1 {

    List<Integer> answer = new ArrayList<>();

    // List 반환 시
    public List<Integer> solution(int n) {
        if (n == 1) {
            answer.add(n);
            return answer;
        }
        solution(n - 1);
        answer.add(n);
        return answer;
    }

    // 단순 출력
//    public void solution(int n) {
//        if (n == 1) {
//            System.out.print(n + " ");
//            return
//        }
//        solution(n - 1);
//        System.out.print(n + " ");
//    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();

        Solution1 solution1 = new Solution1();
        for(int i : solution1.solution(n)){
            System.out.print(i + " ");
        }
    }
}
