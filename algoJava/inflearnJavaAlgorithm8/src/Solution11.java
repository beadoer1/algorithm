//11. 미로의 최단거리 통로(BFS)
//설명
//7*7 격자판 미로를 탈출하는 최단경로의 길이를 출력하는 프로그램을 작성하세요.
//경로의 길이는 출발점에서 도착점까지 가는데 이동한 횟수를 의미한다.
//출발점은 격자의 (1, 1) 좌표이고, 탈출 도착점은 (7, 7)좌표이다. 격자판의 1은 벽이고, 0은 도로이다.
//격자판의 움직임은 상하좌우로만 움직인다. 미로가 다음과 같다면
//위와 같은 경로가 최단 경로의 길이는 12이다.
//
//입력
//첫 번째 줄부터 7*7 격자의 정보가 주어집니다.
//
//출력
//첫 번째 줄에 최단으로 움직인 칸의 수를 출력한다. 도착할 수 없으면 -1를 출력한다.
//
//예시 입력 1
//0 0 0 0 0 0 0
//0 1 1 1 1 1 0
//0 0 0 1 0 0 0
//1 1 0 1 0 1 1
//1 1 0 1 0 0 0
//1 0 0 0 1 0 0
//1 0 1 0 0 0 0
//
//예시 출력 1
//12

import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class Solution11 {
    public static final int[] dx = {1, 0, -1, 0};
    public static final int[] dy = {0, -1, 0, 1};
    public static final int[][] miro = new int[7][7];

    public int solution(){
        Queue<Point> queue = new LinkedList<>();
        queue.offer(new Point(0, 0));

        int level = 0;
        while (!queue.isEmpty()) {
            level++;
            int cur = queue.size();
            for (int i = 0; i < cur; i++) {
                Point checkValue = queue.poll();
                for (int j = 0; j < 4; j++) {
                    int nx = checkValue.x + dx[j];
                    int ny = checkValue.y + dy[j];
                    if(nx >= 0 && ny >= 0 && nx < 7 && ny < 7 && miro[ny][nx] == 0){
                        miro[ny][nx] = level;
                        queue.offer(new Point(nx, ny));
                    }
                }
            }
        }

        if(miro[6][6] == 0){
            return -1;
        }
        return miro[6][6];
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        for (int i = 0; i < 7; i++) {
            for (int j = 0; j < 7; j++) {
                miro[i][j] = scanner.nextInt();
            }
        }

        Solution11 solution11 = new Solution11();
        System.out.println(solution11.solution());
    }
}
