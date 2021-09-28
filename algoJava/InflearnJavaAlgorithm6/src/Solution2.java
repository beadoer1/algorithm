//2. 버블 정렬
//설명
//N개이 숫자가 입력되면 오름차순으로 정렬하여 출력하는 프로그램을 작성하세요.
//정렬하는 방법은 버블정렬입니다.
//
//입력
//첫 번째 줄에 자연수 N(1<=N<=100)이 주어집니다.
//두 번째 줄에 N개의 자연수가 공백을 사이에 두고 입력됩니다. 각 자연수는 정수형 범위 안에 있습니다.
//
//출력
//오름차순으로 정렬된 수열을 출력합니다.
//
//예시 입력 1
//6
//13 5 11 7 23 15
//
//예시 출력 1
//5 7 11 13 15 23

import java.util.Scanner;

public class Solution2 {

    public int[] solution(int n, int[] arr) {
        for (int i = 0; i < n; i++) {
            for (int j = 1; j < n - i; j++) {
                if (arr[j] < arr[j - 1]) {
                    int tmp = arr[j - 1];
                    arr[j - 1] = arr[j];
                    arr[j] = tmp;
                }
            }
        }
        return arr;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = scanner.nextInt();
        }
        Solution2 solution2 = new Solution2();
        int[] answer = solution2.solution(n, arr);
        for(int i : answer) {
            System.out.print(i + " ");
        }
    }
}
