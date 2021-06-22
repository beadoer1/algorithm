//3. 문장 속 단어
//설명
//한 개의 문장이 주어지면 그 문장 속에서 가장 긴 단어를 출력하는 프로그램을 작성하세요.
//문장속의 각 단어는 공백으로 구분됩니다.
//
//입력
//첫 줄에 길이가 100을 넘지 않는 한 개의 문장이 주어집니다. 문장은 영어 알파벳으로만 구성되어 있습니다.
//
//출력
//첫 줄에 가장 긴 단어를 출력한다. 가장 길이가 긴 단어가 여러개일 경우 문장속에서 가장 앞쪽에 위치한
//단어를 답으로 합니다.

import java.util.Scanner;

public class Solution3 {

    public String solution(String str) {
        String result = "";
        int maxStringLength = 0;

        // my answer(and Lecture answer 1)
        String[] strArr = str.split(" ");
        for (String strCheck : strArr) {
            if (strCheck.length() > maxStringLength) {
                maxStringLength = strCheck.length();
                result = strCheck;
            }
        }

        // Lecture answer 2 (indexOf(), subString() 사용) -> 왜 이렇게 하는거지..?
//        while (str.contains(" ")) {
//            int pos = str.indexOf(" ");
//            String tmp = str.substring(0, pos);
//
//            if (tmp.length() > maxStringLength) {
//                maxStringLength = tmp.length();
//                result = tmp;
//            }
//
//            str = str.substring(pos + 1);
//        }
//        if (str.length() > maxStringLength) {
//            result = str;
//        }

        return result;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        String str = scanner.nextLine();

        Solution3 solution3 = new Solution3();
        System.out.println(solution3.solution(str));

    }
}
