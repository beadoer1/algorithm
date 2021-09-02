//10. 미로탐색(DFS)
//설명
//7*7 격자판 미로를 탈출하는 경로의 가지수를 출력하는 프로그램을 작성하세요.
//출발점은 격자의 (1, 1) 좌표이고, 탈출 도착점은 (7, 7)좌표이다. 격자판의 1은 벽이고, 0은 통로이다.
//격자판의 움직임은 상하좌우로만 움직인다. 미로가 다음과 같다면
//위의 지도에서 출발점에서 도착점까지 갈 수 있는 방법의 수는 8가지이다.
//
//입력
//7*7 격자판의 정보가 주어집니다.
//
//출력
//첫 번째 줄에 경로의 가지수를 출력한다.
//
//예시 입력 1
//0 0 0 0 0 0 0
//0 1 1 1 1 1 0
//0 0 0 1 0 0 0
//1 1 0 1 0 1 1
//1 1 0 0 0 0 1
//1 1 0 1 1 0 0
//1 0 0 0 0 0 0
//
//예시 출력 1
//8

import java.util.Scanner;

public class Solution10 {

    public static final int[] dx = {1, 0, -1, 0};
    public static final int[] dy = {0, -1, 0, 1};
    public static final int[][] miro = new int[7][7];
    public static int count = 0;

    public int solution() {
        int i = 0;
        int j = 0;
        DFS(i, j);
        return count;
    }

    private void DFS(int i, int j) {
        if (i == 6 && j == 6) {
            count++;
            return;
        }

        for (int k = 0; k < 4; k++) {
            int nx = j + dx[k];
            int ny = i + dy[k];
            if (nx >= 0 && ny >= 0 && nx < 7 && ny < 7 && miro[ny][nx] == 0) {
                miro[i][j] = 1;
                DFS(ny,nx);
                miro[i][j] = 0;
            }
        }
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        for (int i = 0; i < 7; i++) {
            for (int j = 0; j < 7; j++) {
                miro[i][j] = scanner.nextInt();
            }
        }

        Solution10 solution10 = new Solution10();
        System.out.println(solution10.solution());
    }
}
