//1. 씨름 선수
//설명
//현수는 씨름 감독입니다. 현수는 씨름 선수를 선발공고를 냈고, N명의 지원자가 지원을 했습니다.
//현수는 각 지원자의 키와 몸무게 정보를 알고 있습니다.
//현수는 씨름 선수 선발 원칙을 다음과 같이 정했습니다.
//“A라는 지원자를 다른 모든 지원자와 일대일 비교해서 키와 몸무게 모두 A지원자 보다 높은(크고, 무겁다) 지원자가
//존재하면 A지원자는 탈락하고, 그렇지 않으면 선발된다.”
//N명의 지원자가 주어지면 위의 선발원칙으로 최대 몇 명의 선수를 선발할 수 있는지 알아내는 프로그램을 작성하세요.
//
//입력
//첫째 줄에 지원자의 수 N(5<=N<=30,000)이 주어집니다.
//두 번째 줄부터 N명의 흰돌 능력치와 검은돌 능력치 정보가 차례로 주어집니다.
//각 선수의 흰돌능력치가 모두 다르고, 검은돌 능력치도 모두 다릅니다. 능력치 값은 1,000,000이하의 자연수입니다.
//
//출력
//첫째 줄에 바둑 선수로 뽑히는 최대 인원을 출력하세요.
//
//예시 입력 1
//5
//172 67
//183 65
//180 70
//170 72
//181 60
//
//예시 출력 1
//3
//
//힌트
//출력설명
//(183, 65), (180, 70), (170, 72) 가 선발됩니다. (181, 60)은 (183, 65)보다 키와 몸무게 모두 낮기 때문에 탈락이고, (172, 67)은 (180, 70) 때문에 탈락입니다.

import java.util.ArrayList;
import java.util.Collections;
import java.util.Scanner;

// 지네릭에 객체 지정해줘야 Override 때 해당 객체를 매개변수로 비교할 수 있다.
class Body implements Comparable<Body> {
    public int height;
    public int weight;

    public Body(int height, int weight) {
        this.height = height;
        this.weight = weight;
    }

    @Override
    public int compareTo(Body body) {
        return body.height - this.height;
    }


}

public class Solution1 {

    private int solution(ArrayList<Body> bodyArr) {
        Collections.sort(bodyArr);
        int maxWeight = Integer.MIN_VALUE;

        int count = 0;

        for (Body body : bodyArr) {
            if (body.weight > maxWeight) {
                count++;
                maxWeight = body.weight;
            }
        }

        return count;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int n = scanner.nextInt();

        ArrayList<Body> bodyArr = new ArrayList<>();

        for (int i = 0; i < n; i++) {
            int height = scanner.nextInt();
            int weight = scanner.nextInt();

            bodyArr.add(new Body(height, weight));
        }

        Solution1 solution1 = new Solution1();
        System.out.println(solution1.solution(bodyArr));
    }

// 1차 풀이 ( 계속 절차 지향으로만 생각하고 있는건 아닌가 꺠닫자.)
//    private int solution(int[][] total) {
//        Arrays.sort(total, Comparator.comparingInt(o -> o[0]));
//
//        Stack<Integer> peak = new Stack<>();
//        peak.push(0);
//
//        for (int i = 1; i < total.length-1; i++) {
//            if(total[i-1][1] < total[i][1] && total[i+1][1] < total[i][1]) {
//                // peak 가 비어있는데 꺼내려해서 Runtime error 가 발생했었다..ㅠ
//                while (!peak.empty() && total[peak.peek()][1] < total[i][1]) {
//                    peak.pop();
//                }
//                peak.push(i);
//            }
//        }
//        peak.push(total.length-1);
//
//        int count = 0;
//        for (int i = 0; i < peak.size() - 1; i++) {
//            int index = peak.get(i);
//            while (total[index][1] > total[peak.get(i + 1)][1]) {
//                count++;
//                index++;
//            }
//        }
//
//        return count + 1;
//    }
//
//    public static void main(String[] args) {
//        Scanner scanner = new Scanner(System.in);
//
//        int n = scanner.nextInt();
//
//        int[][] total = new int[n][2];
//
//        for (int i = 0; i < n; i++) {
//            int height = scanner.nextInt();
//            int weight = scanner.nextInt();
//
//            total[i] = new int[]{height, weight};
//        }
//
//        Solution1 solution1 = new Solution1();
//        System.out.println(solution1.solution(total));
//    }
}
