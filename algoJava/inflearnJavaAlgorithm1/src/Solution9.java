//9. 숫자만 추출
//설명
//문자와 숫자가 섞여있는 문자열이 주어지면 그 중 숫자만 추출하여 그 순서대로 자연수를 만듭니다.
//만약 “tge0a1h205er”에서 숫자만 추출하면 0, 1, 2, 0, 5이고 이것을 자연수를 만들면 1205이 됩니다.
//추출하여 만들어지는 자연수는 100,000,000을 넘지 않습니다.
//
//입력
//첫 줄에 숫자가 썩인 문자열이 주어집니다. 문자열의 길이는 100을 넘지 않습니다.
//
//출력
//첫 줄에 자연수를 출력합니다.


import java.util.Scanner;

public class Solution9 {
    public int solution(String str) {
        // my answer
        String strReplaceLowerCase = str.replaceAll("[a-z]", "");
        String strReplaceUpperCase = strReplaceLowerCase.replaceAll("[A-Z]", "");

        int result = Integer.parseInt(strReplaceUpperCase);

        return result;

        // lectur answer1
//        int result = 0;
//        for (char c : str.toCharArray()) {
//            if(48 <= c && c <= 57){
//                result = result * 10 + (c - 48);
//            }
//        }

        // lectur answer2
//        String resultStr = "";
//        for (char c : str.toCharArray()) {
//            if (Character.isDigit(c)) {
//                resultStr+=c;
//            }
//        }
//        int result = Integer.parseInt(resultStr);
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String str = scanner.next();

        Solution9 solution9 = new Solution9();
        System.out.println(solution9.solution(str));
    }
}
