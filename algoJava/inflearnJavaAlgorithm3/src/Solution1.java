//1. 두 배열 합치기
//설명
//오름차순으로 정렬이 된 두 배열이 주어지면 두 배열을 오름차순으로 합쳐 출력하는 프로그램을 작성하세요.
//
//입력
//첫 번째 줄에 첫 번째 배열의 크기 N(1<=N<=100)이 주어집니다.
//두 번째 줄에 N개의 배열 원소가 오름차순으로 주어집니다.
//세 번째 줄에 두 번째 배열의 크기 M(1<=M<=100)이 주어집니다.
//네 번째 줄에 M개의 배열 원소가 오름차순으로 주어집니다.
//각 리스트의 원소는 int형 변수의 크기를 넘지 않습니다.
//
//출력
//오름차순으로 정렬된 배열을 출력합니다.
//
//예시 입력 1
//3
//1 3 5
//5
//2 3 6 7 9
//
//예시 출력 1
//1 2 3 3 5 6 7 9

import java.util.ArrayList;
import java.util.Scanner;

public class Solution1 {
    // my answer (135ms)
//    public int[] solution(int n, int[] arrN, int m, int[] arrM) {
//        int[] answer = new int[n+m];
//        for (int i = 0; i < n; i++) {
//            answer[i] = arrN[i];
//        }
//        for (int i = 0; i < m; i++) {
//            answer[i + n] = arrM[i];
//        }
//
//        Arrays.sort(answer);
//
//        return answer;
//    }

    // lecture answer (137ms) -> 시간 차이는 크게 나지 않지만, 출제 의도가 단순 sort를 위함이 아니다. 참고!!
    public ArrayList<Integer> solution(int n, int[] arrN, int m, int[] arrM){
        ArrayList<Integer> answer = new ArrayList<>();
        int p1 = 0;
        int p2 = 0;
        while(p1 < n && p2 < m){
            if(arrN[p1] < arrM[p2]){
                answer.add(arrN[p1]);
                p1++;
            } else{
                answer.add(arrM[p2]);
                p2++;
            }
        }
        while(p1 < n){
            answer.add(arrN[p1]);
            p1++;
        }
        while (p2 < m) {
            answer.add(arrM[p2]);
            p2++;
        }
        return answer;
    }
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        int[] arrN = new int[n];
        for (int i = 0; i < n; i++) {
            arrN[i] = scanner.nextInt();
        }
        int m = scanner.nextInt();
        int[] arrM = new int[m];
        for (int i = 0; i < m; i++) {
            arrM[i] = scanner.nextInt();
        }

        Solution1 solution1 = new Solution1();
        for(int num : solution1.solution(n,arrN,m,arrM)){
            System.out.print(num + " ");
        }
    }
}
