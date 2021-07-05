//6. 뒤집은 소수
//설명
//N개의 자연수가 입력되면 각 자연수를 뒤집은 후 그 뒤집은 수가 소수이면 그 소수를 출력하는 프로그램을 작성하세요.
//예를 들어 32를 뒤집으면 23이고, 23은 소수이다. 그러면 23을 출력한다. 단 910를 뒤집으면 19로 숫자화 해야 한다.
//첫 자리부터의 연속된 0은 무시한다.
//
//입력
//첫 줄에 자연수의 개수 N(3<=N<=100)이 주어지고, 그 다음 줄에 N개의 자연수가 주어진다.
//각 자연수의 크기는 100,000를 넘지 않는다.
//
//출력
//첫 줄에 뒤집은 소수를 출력합니다. 출력순서는 입력된 순서대로 출력합니다.
//
//예시 입력 1
//9
//32 55 62 20 250 370 200 30 100
//
//예시 출력 1
//23 2 73 2 3

import java.util.ArrayList;
import java.util.Scanner;

public class Solution6 {

    // my answer(139ms)
//    public ArrayList<Integer> solution(int totNum, String[] numArr) {
//        ArrayList<Integer> answer = new ArrayList<>();
//        ArrayList<Integer> revNumArr = new ArrayList<>();
//
//        // 숫자 거꾸로 뒤집기
//        for (int i = 0; i < totNum; i++) {
//            revNumArr.add(Integer.parseInt(new StringBuilder(numArr[i]).reverse().toString()));
//        }
//        // 최대값 선정
//        int maxNum = 0;
//        for (int num : revNumArr) {
//            if (num > maxNum) {
//                maxNum = num;
//            }
//        }
//        // ~최대값 까지 소수 판별
//        int[] primeNum = new int[maxNum + 1];
//        for (int i = 2; i < maxNum + 1; i++) {
//            if (primeNum[i] == 0) {
//                for (int j = 2*i ; j < maxNum + 1; j = j + i) {
//                    primeNum[j] = 1;
//                }
//            }
//        }
//        // 거꾸로 수 중 소수인 수 판별
//        for (int num : revNumArr) {
//            if (primeNum[num] == 0 && num > 1) {
//                answer.add(num);
//            }
//        }
//
//        return answer;
//    }
//
//    public static void main(String[] args) {
//        Scanner scanner = new Scanner(System.in);
//        int totNum = scanner.nextInt();
//
//        String[] numArr = new String[totNum];
//        for (int i = 0; i < totNum; i++) {
//            numArr[i] = scanner.next();
//        }
//
//        Solution6 solution6 = new Solution6();
//        for(int num : solution6.solution(totNum, numArr)){
//            System.out.print(num + " ");
//        }
//    }

    // lecture answer(132ms)
    public boolean isPrime(int num){
        if (num == 1) {
            return false;
        }
        for (int i = 2; i < num; i++) {
            if (num % i == 0) {
                return false;
            }
        }
        return true;
    }

    public ArrayList<Integer> solution(int totNum, int[] numArr) {
        ArrayList<Integer> answer = new ArrayList<>();

        for (int i = 0; i < totNum; i++) {
            int num = numArr[i];
            int res = 0;
            while (num > 0) {
                res = (res*10) + (num%10);
                num = num / 10;
            }
            if (isPrime(res)) {
                answer.add(res);
            }
        }
        return answer;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int totNum = scanner.nextInt();

        int[] numArr = new int[totNum];
        for (int i = 0; i < totNum; i++) {
            numArr[i] = scanner.nextInt();
        }

        Solution6 solution6 = new Solution6();
        for(int num :solution6.solution(totNum, numArr)) {
            System.out.print(num + " ");
        }
    }



}
