// 8. 송아지 찾기 1(BFS : 상태 트리 탐색)
// 설명
// 현수는 송아지를 잃어버렸다. 다행히 송아지에는 위치추적기가 달려 있다.
// 현수의 위치와 송아지의 위치가 수직선상의 좌표 점으로 주어지면 현수는 현재 위치에서 송아지의 위치까지 다음과 같은 방법으로 이동한다.
// 송아지는 움직이지 않고 제자리에 있다.
// 현수는 스카이 콩콩을 타고 가는데 한 번의 점프로 앞으로 1, 뒤로 1, 앞으로 5를 이동할 수 있다.
// 최소 몇 번의 점프로 현수가 송아지의 위치까지 갈 수 있는지 구하는 프로그램을 작성하시오.
//
// 입력
// 첫 번째 줄에 현수의 위치 S와 송아지의 위치 E가 주어진다.
//
// 출력
// 점프의 최소횟수를 구한다. 답은 1 이상이며 반드시 존재한다.


import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class Solution8 {

//    public int solution(int S, int E) {
//        int distance = E - S;
//        if (distance == 0) {
//            return 2;
//        }
//        else if (distance > 0) {
//            if (distance % 5 == 0) {
//                return distance / 5;
//            } else if(distance % 5 <= 3) {
//                return (distance / 5) + (distance % 5);
//            } else{
//                return (distance / 5) + 2;
//            }
//        } else {
//            return (-1) * distance;
//        }
//    }
//

    public int BFS(int S, int E) {
        Queue<Integer> queue = new LinkedList<>();
        queue.offer(S);
        int[] disArr = {1, -1, 5};
        int[] ch = new int[10001];
        int L = 0;
        while (!queue.isEmpty()) {
            int len = queue.size();
            for (int i = 0; i < len; i++) {
                int cur = queue.poll();
                for (int dis : disArr) {
                    int nx = cur + dis;
                    if(nx == E){
                        return ++L;
                    }
                    if (nx >= 1 && nx <= 10000 && ch[nx] == 0) {
                        ch[nx] = 1;
                        queue.offer(nx);
                    }
                }
            }
            L++;
        }

        return 0;
    }



    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int s = scanner.nextInt();
        int e = scanner.nextInt();

        Solution8 solution8 = new Solution8();
//        System.out.println(solution8.solution(s, e));
        System.out.println(solution8.BFS(s,e));
    }
}
