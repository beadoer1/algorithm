//8. 등수구하기
//설명
//N명의 학생의 국어점수가 입력되면 각 학생의 등수를 입력된 순서대로 출력하는 프로그램을 작성하세요.
//같은 점수가 입력될 경우 높은 등수로 동일 처리한다.
//즉 가장 높은 점수가 92점인데 92점이 3명 존재하면 1등이 3명이고 그 다음 학생은 4등이 된다.
//
//입력
//첫 줄에 N(3<=N<=100)이 입력되고, 두 번째 줄에 국어점수를 의미하는 N개의 정수가 입력된다.
//
//출력
//입력된 순서대로 등수를 출력한다.
//
//예시 입력 1
//5
//87 89 92 100 76
//
//예시 출력 1
//4 3 2 1 5

import java.util.Scanner;

public class Solution8 {

    public int[] solution(int totNum, int[] scoreArr) {
//        // my answer : O(n) (126ms)
//        int[] answer = new int[totNum];
//        // 순위를 보기 위해 정렬된 배열을 마련
//        int[] sortScoreArr = new int[totNum];
//        for (int i = 0; i < totNum; i++) {
//            sortScoreArr[i] = scoreArr[i];
//        }
//        Arrays.sort(sortScoreArr);
//        // 점수 별 순위를 HashMap 형태로 정리
//        Map<Integer, Integer> scoreRankMap = new HashMap<>();
//        for (int j = totNum - 1; j >= 0; j--) {
//            if(!scoreRankMap.containsKey(sortScoreArr[j])){
//                scoreRankMap.put(sortScoreArr[j], totNum - j);
//            }
//        }
//        // 각 점수에 해당하는 순위를 answer에 입력
//        for (int k = 0; k < totNum; k++) {
//            answer[k] = scoreRankMap.get(scoreArr[k]);
//        }

        // lecture answer : O(n^2) (126ms) -> 들어가는 숫자가 엄청 커지면 더 느려지지 않을까..ㅠㅠ
        int[] answer = new int[totNum];
        for (int i = 0; i < totNum; i++) {
            int count = 0;
            for (int j = 0; j < totNum; j++) {
                if(scoreArr[j] > scoreArr[i]){
                    count++;
                }
                answer[i] = count + 1;
            }
        }

        return answer;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int totNum = scanner.nextInt();

        int[] scoreArr = new int[totNum];
        for (int i = 0; i < totNum; i++) {
            scoreArr[i] = scanner.nextInt();
        }

        Solution8 solution8 = new Solution8();
        for (int rank : solution8.solution(totNum, scoreArr)) {
            System.out.print(rank + " ");
        }
    }
}
