//5. K번째 큰 수
//설명
//현수는 1부터 100사이의 자연수가 적힌 N장의 카드를 가지고 있습니다. 같은 숫자의 카드가 여러장 있을 수 있습니다.
//현수는 이 중 3장을 뽑아 각 카드에 적힌 수를 합한 값을 기록하려고 합니다. 3장을 뽑을 수 있는 모든 경우를 기록합니다.
//기록한 값 중 K번째로 큰 수를 출력하는 프로그램을 작성하세요.
//만약 큰 수부터 만들어진 수가 25 25 23 23 22 20 19......이고 K값이 3이라면 K번째 큰 값은 22입니다.
//
//입력
//첫 줄에 자연수 N(3<=N<=100)과 K(1<=K<=50) 입력되고, 그 다음 줄에 N개의 카드값이 입력된다.
//
//출력
//첫 줄에 K번째 수를 출력합니다. K번째 수가 존재하지 않으면 -1를 출력합니다.
//
//예시 입력 1
//10 3
//13 15 34 23 45 65 33 11 26 42
//
//예시 출력 1
//143

import java.util.Collections;
import java.util.Scanner;
import java.util.TreeSet;

public class Solution5 {
    // 3중 for 문 돌리는거였구나...^^^^
    public int solution(int totNum, int selectNum, int[] arr) {
        TreeSet<Integer> treeSet = new TreeSet<>(Collections.reverseOrder());

        for (int i = 0; i < totNum; i++) {
            for (int j = i + 1; j < totNum; j++) {
                for (int k = j + 1; k < totNum; k++) {
                    treeSet.add(arr[i] + arr[j] + arr[k]);
                }
            }
        }

        // lecture answer(171ms)
//        int count = 0;
//        for (int x : treeSet) {
//            count++;
//            if (count == selectNum) {
//                return x;
//            }
//        }

        // 응용(166ms)
        if (treeSet.size() < selectNum) {
            return -1;
        }
        for (int i = 0; i < selectNum-1; i++) {
            treeSet.pollFirst();
        }
        return treeSet.pollFirst();
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int totNum = scanner.nextInt();
        int selectNum = scanner.nextInt();

        int[] arr = new int[totNum];
        for (int i = 0; i < totNum; i++) {
            arr[i] = scanner.nextInt();
        }

        Solution5 solution5 = new Solution5();
        System.out.println(solution5.solution(totNum, selectNum, arr));
    }
}
