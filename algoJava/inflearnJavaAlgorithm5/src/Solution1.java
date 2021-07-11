//1. 올바른 괄호
//설명
//괄호가 입력되면 올바른 괄호이면 “YES", 올바르지 않으면 ”NO"를 출력합니다.
//(())() 이것은 괄호의 쌍이 올바르게 위치하는 거지만, (()()))은 올바른 괄호가 아니다.
//
//입력
//첫 번째 줄에 괄호 문자열이 입력됩니다. 문자열의 최대 길이는 30이다.
//
//출력
//첫 번째 줄에 YES, NO를 출력한다.
//
//예시 입력 1
//(()(()))(()
//
//예시 출력 1
//NO

import java.util.Scanner;
import java.util.Stack;

public class Solution1 {

    public String solution(String str) {

        // my answer(125ms)
//        int count = 0;
//        for (char c : str.toCharArray()) {
//            if(c == '(') {
//                count++;
//            }else {
//                count--;
//            }
//            if (count < 0) {
//                return "NO";
//            }
//        }
//        if (count > 0) {
//            return "NO";
//        }
//        return "YES";

        // lecture answer(118ms)
        Stack<Character> stack = new Stack<>();
        for (char c : str.toCharArray()) {
            if (c == '(') {
                stack.push(c);
            } else{
                if(stack.isEmpty()){
                    return "NO";
                }
                stack.pop();
            }
        }
        if (!stack.isEmpty()) {
            return "NO";
        }
        return "YES";
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String str = scanner.next();

        Solution1 solution1 = new Solution1();
        System.out.println(solution1.solution(str));
    }
}
