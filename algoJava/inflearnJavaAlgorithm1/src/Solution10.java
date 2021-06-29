//10. 가장 짧은 문자거리
//설명
//한 개의 문자열 s와 문자 t가 주어지면 문자열 s의 각 문자가 문자 t와 떨어진 최소거리를 출력하는 프로그램을 작성하세요.
//
//입력
//첫 번째 줄에 문자열 s와 문자 t가 주어진다. 문자열과 문자는 소문자로만 주어집니다.
//문자열의 길이는 100을 넘지 않는다.
//
//출력
//첫 번째 줄에 각 문자열 s의 각 문자가 문자 t와 떨어진 거리를 순서대로 출력한다.

import java.util.Scanner;

public class Solution10 {
    public int[] solution(String str, char c){
        // my answer
//        char[] charArr = str.toCharArray();
//        int[] leftResult = new int[charArr.length];
//        int[] rightResult = new int[charArr.length];
//        int checkNum = 1000;
//        for (int i = 0; i < charArr.length; i++) {
//            if(charArr[i] == c){
//                checkNum = 0;
//            } else{
//                checkNum += 1;
//            }
//            leftResult[i] = checkNum;
//        }
//        checkNum = 1000;
//        for (int i = charArr.length-1; i >= 0; i--) {
//            if(charArr[i] == c){
//                checkNum = 0;
//            }else{
//                checkNum += 1;
//            }
//            rightResult[i] = checkNum;
//        }
//        int[] result = new int[charArr.length];
//        for (int i = 0; i < result.length; i++) {
//            if (leftResult[i] >= rightResult[i]) {
//                result[i] = rightResult[i];
//            }else{
//                result[i] = leftResult[i];
//            }
//        }

        // lecture answer
        int[] result = new int[str.length()];
        int p = 1000;
        for (int i = 0; i < str.length(); i++) {
            if (str.charAt(i) == c) {
                p = 0;
            } else {
                p++;
            }
            result[i] = p;
        }
        p = 1000;
        for (int i = str.length() - 1; i >= 0; i--) {
            if (str.charAt(i) == c) {
                p = 0;
            } else {
                p++;
            }
            result[i] = Math.min(result[i], p);
        }
        return result;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String str = scanner.next();
        char c = scanner.next().charAt(0);

        Solution10 solution10 = new Solution10();
        int[] result = solution10.solution(str, c);
        for (int j : result) {
            System.out.print(j+" ");
        }
    }
}
