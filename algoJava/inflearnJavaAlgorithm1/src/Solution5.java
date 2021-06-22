//5. 특정 문자 뒤집기
//설명
//영어 알파벳과 특수문자로 구성된 문자열이 주어지면 영어 알파벳만 뒤집고,
//특수문자는 자기 자리에 그대로 있는 문자열을 만들어 출력하는 프로그램을 작성하세요.
//
//입력
//첫 줄에 길이가 100을 넘지 않는 문자열이 주어집니다.
//
//출력
//첫 줄에 알파벳만 뒤집힌 문자열을 출력합니다.

import java.util.Scanner;

public class Solution5 {
    public String solution(String str) {
        char[] charArr = str.toCharArray();

        int lt = 0, rt = str.length() - 1;
        while (lt < rt) {
            if(!Character.isAlphabetic(charArr[lt])){
                lt++;
            }else if(!Character.isAlphabetic(charArr[rt])) {
                rt--;
            } else{
                char tmp = charArr[lt];
                charArr[lt] = charArr[rt];
                charArr[rt] = tmp;
                lt++;
                rt--;
            }
        }
        return String.valueOf(charArr);
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String str = scanner.next();

        Solution5 solution5 = new Solution5();
        System.out.println(solution5.solution(str));
    }
}
