//문제
//M이상 N이하의 소수를 모두 출력하는 프로그램을 작성하시오.
//
//입력
//첫째 줄에 자연수 M과 N이 빈 칸을 사이에 두고 주어진다. (1 ≤ M ≤ N ≤ 1,000,000) M이상 N이하의 소수가 하나 이상 있는 입력만 주어진다.
//
//출력
//한 줄에 하나씩, 증가하는 순서대로 소수를 출력한다.

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Q1929 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int m = Integer.parseInt(st.nextToken());
        int n = Integer.parseInt(st.nextToken());

        int[] numArr = new int[n+1];
        int loopNum = (int)Math.sqrt(n)+1;

        for (int j = 2; j < loopNum; j++) {
            if(numArr[j] == 0){
                for(int multiple = 2; multiple <= n/j; multiple++){
                    numArr[multiple * j] = 1;
                }
            }
        }
        if (m == 1) {
            for(int k = 2; k<n+1; k++){
                if (numArr[k] != 1) {
                    System.out.println(k);
                }
            }
        }else {
            for (int k = m; k <n+1; k++) {
                if (numArr[k] != 1) {
                    System.out.println(k);
                }
            }
        }
    }
}
