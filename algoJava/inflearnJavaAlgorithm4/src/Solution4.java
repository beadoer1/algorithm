//4. 모든 아나그램 찾기
//설명
//S문자열에서 T문자열과 아나그램이 되는 S의 부분문자열의 개수를 구하는 프로그램을 작성하세요.
//아나그램 판별 시 대소문자가 구분됩니다. 부분문자열은 연속된 문자열이어야 합니다.
//
//입력
//첫 줄에 첫 번째 S문자열이 입력되고, 두 번째 줄에 T문자열이 입력됩니다.
//S문자열의 길이는 10,000을 넘지 않으며, T문자열은 S문자열보다 길이가 작거나 같습니다.
//
//출력
//S단어에 T문자열과 아나그램이 되는 부분문자열의 개수를 출력합니다.
//
//예시 입력 1
//bacaAacba
//abc
//
//예시 출력 1
//3
//
//힌트
//출력설명: {bac}, {acb}, {cba} 3개의 부분문자열이 "abc"문자열과 아나그램입니다.

import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

public class Solution4 {

    // my answer(162ms)
//    public int solution(String str1, String str2) {
//        int answer = 0;
//        Map<Character, Integer> forMap = new HashMap<>();
//        Map<Character, Integer> checkMap = new HashMap<>();
//
//        for (char c : str2.toCharArray()) {
//            if (!checkMap.containsKey(c)) {
//                checkMap.put(c, 1);
//            }else{
//                checkMap.replace(c, checkMap.get(c) + 1);
//            }
//        }
//
//        for (int i = 0; i < str2.length(); i++) {
//            char c = str1.charAt(i);
//            if (!forMap.containsKey(c)) {
//                forMap.put(c, 1);
//            }else{
//                forMap.replace(c, forMap.get(c) + 1);
//            }
//        }
//        if (forMap.equals(checkMap)) {
//            answer++;
//        }
//
//        int k = str2.length();
//        for (int i = k; i < str1.length(); i++) {
//            char cL = str1.charAt(i - k);
//            char cR = str1.charAt(i);
//            if (forMap.get(cL) > 1) {
//                forMap.replace(cL, forMap.get(cL) - 1);
//            }else if(forMap.get(cL) == 1){
//                forMap.remove(cL);
//            }
//
//            if (!forMap.containsKey(cR)) {
//                forMap.put(cR, 1);
//            }else{
//                forMap.replace(cR, forMap.get(cR) + 1);
//            }
//
//            if (forMap.equals(checkMap)) {
//                answer++;
//            }
//        }
//        return answer;
//    }

    // lecture answer(154ms)
    public int solution(String str1, String str2) {
        int answer = 0;

        Map<Character, Integer> map1 = new HashMap<>();
        Map<Character, Integer> map2 = new HashMap<>();

        for (char key2 : str2.toCharArray()) {
            map2.put(key2, map2.getOrDefault(key2, 0) + 1);
        }
        int k = str2.length() - 1;
        for (int i = 0; i < k; i++) {
            map1.put(str1.charAt(i), map1.getOrDefault(str1.charAt(i), 0) + 1);
        }

        int lt = 0;
        for (int rt = k; rt < str1.length(); rt++) {
            map1.put(str1.charAt(rt), map1.getOrDefault(str1.charAt(rt), 0) + 1);
            if (map1.equals(map2)) {
                answer++;
            }
            map1.put(str1.charAt(lt), map1.get(str1.charAt(lt)) - 1);
            if (map1.get(str1.charAt(lt)) == 0) {
                map1.remove(str1.charAt(lt));
            }
            lt++;
        }
        return answer;
    }

    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);
        String str1 = scanner.next();
        String str2 = scanner.next();

        Solution4 solution4 = new Solution4();
        System.out.println(solution4.solution(str1, str2));
    }

}
