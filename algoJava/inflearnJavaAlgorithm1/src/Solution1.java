//1. 문자 찾기
//설명
//한 개의 문자열을 입력받고, 특정 문자를 입력받아 해당 특정문자가 입력받은 문자열에 몇 개 존재하는지 알아내는 프로그램을 작성하세요.
//대소문자를 구분하지 않습니다.문자열의 길이는 100을 넘지 않습니다.
//
//입력
//첫 줄에 문자열이 주어지고, 두 번째 줄에 문자가 주어진다.
//문자열은 영어 알파벳으로만 구성되어 있습니다.
//
//출력
//첫 줄에 해당 문자의 개수를 출력한다.


import java.util.Scanner;

public class Solution1 {

    public int solution(String str, char c) {
        str = str.toLowerCase();
        c = Character.toLowerCase(c); // 자료형 변수는 자료형 클래스 이용하여 조작한다.


        int count = 0;

        // 일반적인 for 문 사용
//        for (int i = 0; i < str.length(); i++) {
//            char x = str.charAt(i);
//            if (x == c) {
//                count++;
//            }
//        }

        // 향상된 for 문 사용
        for (char x: str.toCharArray()) { // 배열 혹은 Iterator 컬렉션이 와야한다. str.toCharArray() 는 문자열을 문자 배열로 만들어 준다.
            if (x == c) {
                count++;
            }
        }

        return count;
    }

    public static void main(String[] args) {
        Solution1 solution1 = new Solution1();

        Scanner scanner = new Scanner(System.in);
        String str = scanner.next(); // 문자열 하나 읽어들임
        char c = scanner.next().charAt(0); // 문자열 하나 읽어들여 맨 앞에 문자 뽑아냄

        System.out.println(solution1.solution(str, c));
    }
}
