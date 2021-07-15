// 이진트리 순회(넓이 우선 탐색 : 레벨 탐색)
// 아래 그림과 같은 이진트리를 레벨 탐색 연습하세요.
//
//        1
//      /   \
//     2     3
//    / \   / \
//   4   5 6   7
//
// 레벨 탐색 순회 출력 : 1 2 3 4 5 6 7


import java.util.LinkedList;
import java.util.Queue;

class Node2{
    int data;
    Node2 lt,rt;

    public Node2(int data){
        this.data = data;
        lt = rt = null;
    }
}
public class Solution7 {

    Node2 root;
    Queue<Node2> queue = new LinkedList<>();

    public void BFS_mine(Node2 root) {

        if (root == null) {
            return;
        }

        if (root.data == 1) {
            queue.offer(root);
        }

        if (root.lt != null) {
            queue.offer(root.lt);
        }
        if (root.rt != null) {
            queue.offer(root.rt);
        }

        BFS_mine(root.lt);
        BFS_mine(root.rt);
    }

    // lecture answer
    public void BFS(Node2 root) {
        Queue<Node2> Q = new LinkedList<>();
        Q.offer(root);
        while (!Q.isEmpty()) {
            int len = Q.size();
            for (int i = 0; i < len; i++) {
                Node2 cur = Q.poll();
                System.out.print(cur.data + " ");
                if (cur.lt != null) {
                    Q.offer(cur.lt);
                }
                if (cur.rt != null) {
                    Q.offer(cur.rt);
                }
            }
        }
    }

    public static void main(String[] args) {
        Solution7 tree = new Solution7();
        tree.root = new Node2(1);
        tree.root.lt = new Node2(2);
        tree.root.rt = new Node2(3);
        tree.root.lt.lt = new Node2(4);
        tree.root.lt.rt = new Node2(5);
        tree.root.rt.lt = new Node2(6);
        tree.root.rt.rt = new Node2(7);
        tree.BFS(tree.root);

        // my answer
//        tree.BFS_mine(tree.root);
//        while(!tree.queue.isEmpty()){
//            System.out.print(tree.queue.poll().data + " ");
//        }
    }
}
