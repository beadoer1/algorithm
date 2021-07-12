//4. 후위식 연산(postfix)
//설명
//후위연산식이 주어지면 연산한 결과를 출력하는 프로그램을 작성하세요.
//만약 3*(5+2)-9 을 후위연산식으로 표현하면 352+*9- 로 표현되며 그 결과는 12입니다.
//
//입력
//첫 줄에 후위연산식이 주어집니다. 연산식의 길이는 50을 넘지 않습니다.
//식은 1~9의 숫자와 +, -, *, / 연산자로만 이루어진다.
//
//출력
//연산한 결과를 출력합니다.
//
//예시 입력 1
//352+*9-
//
//예시 출력 1
//12

import java.util.Scanner;
import java.util.Stack;

public class Solution4 {

    public int solution(String str) {
        Stack<Integer> stack = new Stack<>();
        for (char c : str.toCharArray()) {
            if (c == '+' || c == '-' || c == '*' || c == '/') {
                int rt = stack.pop();
                int lt = stack.pop();
                int res;
                if(c == '+'){
                    res = lt + rt;
                } else if (c == '-') {
                    res = lt - rt;
                } else if (c == '*') {
                    res = lt * rt;
                } else{
                    res = lt / rt;
                }
                stack.push(res);
            } else{
                stack.push(c - '0');
            }
        }
        return stack.get(0);
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String str = scanner.next();

        Solution4 solution4 = new Solution4();
        System.out.println(solution4.solution(str));

    }
}
