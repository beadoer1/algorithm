//13. 섬나라 아일랜드 (DFS)
//설명
//N*N의 섬나라 아일랜드의 지도가 격자판의 정보로 주어집니다.
//각 섬은 1로 표시되어 상하좌우와 대각선으로 연결되어 있으며, 0은 바다입니다.
//섬나라 아일랜드에 몇 개의 섬이 있는지 구하는 프로그램을 작성하세요.
//만약 위와 같다면 섬의 개수는 5개입니다.
//
//입력
//첫 번째 줄에 자연수 N(3<=N<=20)이 주어집니다.
//두 번째 줄부터 격자판 정보가 주어진다.
//
//출력
//첫 번째 줄에 섬의 개수를 출력한다.
//
//예시 입력 1
//7
//1 1 0 0 0 1 0
//0 1 1 0 1 1 0
//0 1 0 0 0 0 0
//0 0 0 1 0 1 1
//1 1 0 1 1 0 0
//1 0 0 0 1 0 0
//1 0 1 0 1 0 0
//
//예시 출력 1
//5

import java.util.Scanner;

public class Solution13 {
    static int n;
    static int[][] map;
    static int[] dx = {0, 1, 1, 1, 0, -1, -1, -1};
    static int[] dy = {1, 1, 0, -1, -1, -1, 0, 1};

    private int solution() {
        int numberOfIsland = 0;

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if(map[i][j] == 1) {
                    numberOfIsland++;
                    DFS(j, i);
                }
            }
        }

        return numberOfIsland;
    }

    private void DFS(int x, int y) {

        map[y][x] = 0;
        for (int k = 0; k < 8; k++) {
            int nx = x + dx[k];
            int ny = y + dy[k];
            if (0 <= nx && nx < n && 0 <= ny && ny < n && map[ny][nx] == 1) {
                DFS(nx, ny);
            }
        }
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        n = scanner.nextInt();

        map = new int[n][n];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                map[i][j] = scanner.nextInt();
            }
        }

        Solution13 solution14 = new Solution13();
        System.out.println(solution14.solution());
    }
}
