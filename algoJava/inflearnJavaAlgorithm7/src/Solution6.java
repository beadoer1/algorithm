// 부분집합 구하기(DFS)
// 자연수 N이 주어지면 1부터 N까지의 원소를 갖는 집합의 부분집합을 모두 출력하는 프로그램을 작성하세요.
//
// 입력 설명
// 첫 번째 줄에 자연수 N(1<=N<=10)이 주어집니다.
//
// 출력 설명
// 첫 번째 줄부터 각 줄에 하나씩 부분집합을 아래와 출력 예제와 같은 순서로 출력한다.
// 단, 공집합은 출력하지 않습니다.
//
// 입력 예제
// 3
// 출력 예제
// 1 2 3
// 1 2
// 1 3
// 1
// 2 3
// 2
// 3

import java.util.Arrays;
import java.util.Scanner;

public class Solution6 {
    int[] ch;

    public void solution(int nS, int nE) {
        if (nS == nE + 1) {
            String tmp = "";
            for (int i = 1; i < nE + 1; i++) {
                if(ch[i]==1){
                    tmp += (i + " ");
                }
            }
            if (tmp.length() > 0) {
                System.out.println(tmp);
            }
            return;
        }
        ch[nS] = 1;
        solution(nS + 1, nE);
        ch[nS] = 0;
        solution(nS + 1, nE);
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();

        Solution6 solution6 = new Solution6();
        solution6.ch = new int[n+1];
        solution6.solution(1,n);
        System.out.println(Arrays.toString(solution6.ch));

    }
}
