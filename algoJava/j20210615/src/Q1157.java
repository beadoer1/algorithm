//문제
//알파벳 대소문자로 된 단어가 주어지면, 이 단어에서 가장 많이 사용된 알파벳이 무엇인지 알아내는 프로그램을 작성하시오. 단, 대문자와 소문자를 구분하지 않는다.
//
//입력
//첫째 줄에 알파벳 대소문자로 이루어진 단어가 주어진다. 주어지는 단어의 길이는 1,000,000을 넘지 않는다.
//
//출력
//첫째 줄에 이 단어에서 가장 많이 사용된 알파벳을 대문자로 출력한다. 단, 가장 많이 사용된 알파벳이 여러 개 존재하는 경우에는 ?를 출력한다.

import java.util.Scanner;

public class Q1157 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String word = scanner.nextLine();
        System.out.println(highestFreWord(word));
    }

    public static char highestFreWord(String word){
        String upperWord = word.toUpperCase();
        int[] alphaArr = new int[26];

        for (int i = 0; i < 26; i++) {
            alphaArr[i] = 0;
        }
        for (int i = 0; i < upperWord.length(); i++) {
            alphaArr[upperWord.charAt(i)-65]++;
        }
        
        int maxNum = 0;
        char highestFreAlpha = '?';
        for (int i = 0; i < 26; i++) {
            if(alphaArr[i] > maxNum) {
                maxNum = alphaArr[i] ;
                highestFreAlpha = (char) (i + 65);
            } else if (alphaArr[i] == maxNum) {
                highestFreAlpha = '?';
            }
        }
        return highestFreAlpha;
    }
}
