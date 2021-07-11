import java.util.Scanner;
import java.util.Stack;

public class Solution3 {

    // my answer(lecture answer)
    public int solution(int n, int[][] board, int m, int[] moves) {
        int answer = 0;
        Stack<Integer> stack = new Stack<>();

        for (int num : moves) {
            for (int i = 0; i < n; i++) {
                if (board[i][num-1] != 0) {
                    int peekNum = board[i][num-1];
                    board[i][num-1] = 0;
                    if (stack.isEmpty() || stack.peek() != peekNum) {
                        stack.push(peekNum);
                    }else {
                        stack.pop();
                        answer += 2;
                    }
                    break;
                }
            }
        }
        return answer;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();

        int[][] board = new int[n][n];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                board[i][j] = scanner.nextInt();
            }
        }

        int m = scanner.nextInt();

        int[] moves = new int[m];
        for (int i = 0; i < m; i++) {
            moves[i] = scanner.nextInt();
        }

        Solution3 solution3 = new Solution3();
        System.out.println(solution3.solution(n,board,m,moves));

    }
}
