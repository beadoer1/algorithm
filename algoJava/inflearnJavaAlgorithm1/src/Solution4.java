//4. 단어 뒤집기
//설명
//N개의 단어가 주어지면 각 단어를 뒤집어 출력하는 프로그램을 작성하세요.
//
//입력
//첫 줄에 자연수 N(3<=N<=20)이 주어집니다.
//두 번째 줄부터 N개의 단어가 각 줄에 하나씩 주어집니다. 단어는 영어 알파벳으로만 구성되어 있습니다.
//
//출력
//N개의 단어를 입력된 순서대로 한 줄에 하나씩 뒤집어서 출력합니다.

import java.util.ArrayList;
import java.util.Scanner;

public class Solution4 {

    public ArrayList<String> solution(String[] strArr) {
        ArrayList<String> results = new ArrayList<>();
        // Lecture answer 1 -> StringBuilder 사용. String 변동 많을 때 사용하면 좋다.
        for (String str : strArr) {
            String tmp = new StringBuilder(str).reverse().toString();
            results.add(tmp);
        }

        // Lecture answer 2
//        for (String str : strArr) {
//            char[] charArr = str.toCharArray();
//            int lt = 0, rt = charArr.length - 1;
//            while (lt < rt) {
//                char tmp = charArr[lt];
//                charArr[lt] = charArr[rt];
//                charArr[rt] = tmp;
//                lt++;
//                rt--;
//            }
//            String result = String.valueOf(charArr);
//            results.add(result);
//        }


        return results;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int wordNum = scanner.nextInt();
        String[] words = new String[wordNum];
        for (int i = 0; i < wordNum; i++) {
            words[i] = (scanner.next());
        }

        Solution4 solution4 = new Solution4();
        ArrayList<String> results = solution4.solution(words);

        for (String result : results) {
            System.out.println(result);
        }
    }
}
