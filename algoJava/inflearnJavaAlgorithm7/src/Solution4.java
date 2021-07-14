// 피보나치 수열
// 1) 피보나치 수열을 출력한다.
//    피보나치 수열이란 앞의 2개의 수를 합하여 다음 숫자가 되는 수열이다.
// 2) 입력은 피보나치 수열의 총 항의 수 이다.
//    만약 7이 입력되면 1 1 2 3 5 8 13 을 출력하면 된다.
//
// 입력 설명
// 첫 줄에 총 항수 N(3<=N<=45)이 입력된다.

import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

public class Solution4 {
    Map<Integer, Integer> piboMap = new HashMap<>();

    public int solution(int n) {

        if(piboMap.containsKey(n)){
            return piboMap.get(n);
        }

        if (n == 1 || n == 2) {
            piboMap.put(n, 1);
            return 1;
        }

        int piboN = solution(n - 1) + solution(n - 2);
        piboMap.put(n, piboN);
        return piboN;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();

        Solution4 solution4 = new Solution4();
        solution4.solution(n);

        for (int i = 1; i < solution4.piboMap.size()+1; i++) {
            System.out.print(solution4.piboMap.get(i)+ " ");
        }
    }
}
