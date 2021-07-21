// 순열 구하기
// 10 이하 N개의 자연수가 주어지면 이 중 M개를 뽑아 일렬로 나열하는 방법을 모두 출력합니다.
//
// 입력 설명
// 첫 번째 줄에 자연수 N(3<=N<=10)과 M(2<=M<=N)이 주어집니다.
// 두 번째 줄에 N개의 자연수가 오름차순으로 주어집니다.
//
// 출력 설명
// 첫 번째 줄에 결과를 출력합니다.
// 출력 순서는 사전 순으로 오름차순으로 출력합니다.
//
// 입력 예제
// 3 2
// 3 6 9
//
// 출력 예제
// 3 6
// 3 9
// 6 3
// 6 9
// 9 3
// 9 6

import java.util.Scanner;

public class Solution6 {

    static int n,m;
    static int[] arr, answerArr;

    public void solution(int L) {

        if (L == m) {
            for (int x : answerArr) {
                System.out.print(x + " ");
            }
            System.out.println();
            return;
        }

        for (int i = 0; i < n; i++) {
            if (arr[i] != 0) {
                answerArr[L] = arr[i];
                int tmp = arr[i]; // check Arr 별도로 만드는게 더 효율적일지도(Lecture answer)
                arr[i] = 0;
                solution(L + 1);
                arr[i] = tmp;
            }
        }
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        n = scanner.nextInt();
        m = scanner.nextInt();

        arr = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = scanner.nextInt();
        }

        answerArr = new int[m];
        Solution6 solution6 = new Solution6();
        solution6.solution(0);
    }
}
