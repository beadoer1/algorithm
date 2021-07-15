// Tree 말단 노드까지의 가장 짧은 경로
// 아래 그림과 같은 이진트리에서 루트 노드 1에서 말단 노드까지의 길이 중 가장 짧은 길이를 구하는 프로그램을 작성하시오.
// 각 경로의 길이는 루트노드에서 말단노드까지 가는데 이동하는 횟수를 즉 간선(에지)의 개수를 길이로 하겠습니다.
//        1
//      /   \
//     2     3
//    / \
//   4   5
//
// 가장 짧은 길이는 3번 노드까지의 길이인 1이다.

class Node3{
    int data;
    Node3 lt,rt;

    public Node3(int data) {
        this.data = data;
        lt = rt = null;
    }
}
public class Solution9  {

    Node3 root;
    public int DFS(Node3 root, int dis) {
        if (root == null) {
            return dis - 1;
        }
        return Math.min(DFS(root.lt,dis+1),DFS(root.rt,dis+1));
    }

    public static void main(String[] args) {
        Solution9 tree = new Solution9();
        tree.root = new Node3(1);
        tree.root.lt = new Node3(2);
        tree.root.rt = new Node3(3);
        tree.root.lt.lt = new Node3(4);
        tree.root.lt.rt = new Node3(5);
        System.out.println(tree.DFS(tree.root, 0));
    }
}
