//2. 아나그램(해쉬)
//설명
//Anagram이란 두 문자열이 알파벳의 나열 순서를 다르지만 그 구성이 일치하면 두 단어는 아나그램이라고 합니다.
//예를 들면 AbaAeCe 와 baeeACA 는 알파벳을 나열 순서는 다르지만 그 구성을 살펴보면 A(2), a(1), b(1), C(1), e(2)로
//알파벳과 그 개수가 모두 일치합니다. 즉 어느 한 단어를 재 배열하면 상대편 단어가 될 수 있는 것을 아나그램이라 합니다.
//길이가 같은 두 개의 단어가 주어지면 두 단어가 아나그램인지 판별하는 프로그램을 작성하세요. 아나그램 판별시 대소문자가 구분됩니다.
//
//입력
//첫 줄에 첫 번째 단어가 입력되고, 두 번째 줄에 두 번째 단어가 입력됩니다.
//단어의 길이는 100을 넘지 않습니다.
//
//출력
//두 단어가 아나그램이면 “YES"를 출력하고, 아니면 ”NO"를 출력합니다.
//
//예시 입력 1
//AbaAeCe
//baeeACA
//
//예시 출력 1
//YES
//
//예시 입력 2
//abaCC
//Caaab
//
//예시 출력 2
//NO

import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

public class Solution2 {
    // my answer(128ms)
//    public String solution(String str1, String str2) {
//        Map<Character, Integer> strMap1 = new HashMap<>();
//        Map<Character, Integer> strMap2 = new HashMap<>();
//
//        for (char c : str1.toCharArray()) {
//            if (!strMap1.containsKey(c)) {
//                strMap1.put(c, 1);
//            }else{
//                strMap1.replace(c, strMap1.get(c) + 1);
//            }
//        }
//
//        for (char c : str2.toCharArray()) {
//            if (!strMap2.containsKey(c)) {
//                strMap2.put(c, 1);
//            }else{
//                strMap2.replace(c, strMap2.get(c) + 1);
//            }
//        }
//
//        if(strMap1.equals(strMap2)){
//            return "YES";
//        }
//        return "NO";
//    }

    // my answer after complete lecture(118ms)
//    public String solution(String str1, String str2) {
//        Map<Character, Integer> map1 = new HashMap<>();
//        Map<Character, Integer> map2 = new HashMap<>();
//
//        for (char key1 : str1.toCharArray()) {
//            map1.put(key1, map1.getOrDefault(key1, 0) + 1);
//        }
//        for (char key2 : str2.toCharArray()) {
//            map2.put(key2, map2.getOrDefault(key2, 0) + 1);
//        }
//        if (map1.equals(map2)) {
//            return "YES";
//        }
//        return "NO";
//    }

    // lecture answer(116ms)
    public String solution(String str1, String str2) {
        Map<Character, Integer> map1 = new HashMap<>();
        for (char key : str1.toCharArray()) {
            map1.put(key, map1.getOrDefault(key, 0) + 1);
        }
        for (char key : str2.toCharArray()) {
            if (!map1.containsKey(key) || map1.get(key) == 0) {
                return "NO";
            }
            map1.put(key, map1.get(key) - 1);
        }
        return "YES";
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String str1 = scanner.next();
        String str2 = scanner.next();

        Solution2 solution2 = new Solution2();
        System.out.println(solution2.solution(str1, str2));
    }
}
