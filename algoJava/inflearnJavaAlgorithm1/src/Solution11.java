//11. 문자열 압축
//설명
//알파벳 대문자로 이루어진 문자열을 입력받아 같은 문자가 연속으로 반복되는 경우 반복되는
//문자 바로 오른쪽에 반복 횟수를 표기하는 방법으로 문자열을 압축하는 프로그램을 작성하시오.
//단 반복횟수가 1인 경우 생략합니다.
//
//입력
//첫 줄에 문자열이 주어진다. 문자열의 길이는 100을 넘지 않는다.
//
//출력
//첫 줄에 압축된 문자열을 출력한다.

import java.util.Scanner;

public class Solution11 {
    public String solution(String str) {
        // my answer
//        char currentC = 'a';
//        int count = 1;
//        String result = "";
//        for (char c : str.toCharArray()) {
//            if (c == currentC) {
//                count++;
//            }else{
//                result = result + currentC + count;
//                currentC = c;
//                count = 1;
//            }
//        }
//        result = result + currentC + count;
//        return result.replace("a","").replaceAll("1", "");

        // lectur answer
        str += " ";
        String result = "";
        int count = 1;
        for (int i = 0; i < str.length() - 1; i++) {
            if (str.charAt(i) == str.charAt(i + 1)) {
                count++;
            }else{
                result += str.charAt(i);
                if (count > 1) {
                    result += count;
                }
                count = 1;
            }
        }
        return result;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String str = scanner.next();

        Solution11 solution11 = new Solution11();
        System.out.println(solution11.solution(str));
    }
}
