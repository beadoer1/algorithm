//2. 대소문자 변환
//설명
//대문자와 소문자가 같이 존재하는 문자열을 입력받아 대문자는 소문자로 소문자는 대문자로 변환하여 출력하는 프로그램을 작성하세요.
//
//입력
//첫 줄에 문자열이 입력된다. 문자열의 길이는 100을 넘지 않습니다.
//문자열은 영어 알파벳으로만 구성되어 있습니다.
//
//출력
//첫 줄에 대문자는 소문자로, 소문자는 대문자로 변환된 문자열을 출력합니다.

import java.util.Scanner;

public class Solution2 {

    public String solution(String str) {
        String result = "";

        // My Answer
//        for (int i = 0; i < str.length(); i++) {
//            char x = str.charAt(i);
//            if('a' <= x && x <= 'z'){
//                result = result + Character.toUpperCase(x);
//            } else if ('A' <= x && x <= 'Z') {
//                result = result + Character.toLowerCase(x);
//            }
//        }

        // Lecture Answer
        for (char x : str.toCharArray()) {
            if(Character.isLowerCase(x)){
                result += Character.toUpperCase(x);
            }else{
                result += Character.toLowerCase(x);
            }
        }
        return result;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        String str = scanner.next();

        Solution2 solution2 = new Solution2();
        System.out.println(solution2.solution(str));
    }
}
