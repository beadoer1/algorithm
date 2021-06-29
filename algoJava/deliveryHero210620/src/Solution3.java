import java.util.ArrayList;
import java.util.List;

class Solution3 {
        public static void main(String[] args) {
            solution(1765);
    }

    public static int solution(int N) {

        List<String> numConsCheck = new ArrayList<>();
        for (int i = 0; i < 10; i++) {
            numConsCheck.add(String.valueOf(i) + i);
        }

        int num = N + 1;

        String numString = String.valueOf(num);

        boolean isNumConsCheck = true;
        while (isNumConsCheck) {
            for (String numCons : numConsCheck) {
                if (numString.contains(numCons)) {
                    num = num + 1;
                    numString = String.valueOf(num);
                    break;
                }
                if (numCons.equals("99")) {
                    isNumConsCheck = false;
                }
            }
        }
        return num;
    }
}
