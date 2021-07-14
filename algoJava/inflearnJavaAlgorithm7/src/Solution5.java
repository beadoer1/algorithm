// 이진트리 순회(깊이 우선 탐색)
// 아래 그림과 같은 이진트리를 전위순회와 후위순회를 연습해보세요.
//        1
//      /   \
//     2     3
//    / \   / \
//   4   5 6   7
//
// 전위순회 출력 : 1 2 4 5 3 6 7
// 중위순회 출력 : 4 2 5 1 6 3 7
// 후위순회 출력 : 4 5 2 6 7 3 1


class Node{
    int data;
    Node lt,rt;

    public Node(int data) {
        this.data = data;
        lt = null;
        rt = null;
    }
}

public class Solution5 {
    Node root;
    // 전위 순회(preorder)
    public void preorderDFS(Node root) {
        if (root == null) {
            return;
        }
        System.out.print(root.data + " ");
        preorderDFS(root.lt);
        preorderDFS(root.rt);
    }
    // 중위 순회(inorder)
    public void inorderDFS(Node root) {
        if (root == null) {
            return;
        }
        inorderDFS(root.lt);
        System.out.print(root.data + " ");
        inorderDFS(root.rt);
    }

    // 후위 순회(postorder)
    public void postorderDFS(Node root) {
        if (root == null) {
            return;
        }
        postorderDFS(root.lt);
        postorderDFS(root.rt);
        System.out.print(root.data + " ");
    }

    public static void main(String[] args) {
        Solution5 tree = new Solution5();
        tree.root = new Node(1);
        tree.root.lt = new Node(2);
        tree.root.rt = new Node(3);
        tree.root.lt.lt = new Node(4);
        tree.root.lt.rt = new Node(5);
        tree.root.rt.lt = new Node(6);
        tree.root.rt.rt = new Node(7);

        tree.preorderDFS(tree.root);
        System.out.println();
        tree.inorderDFS(tree.root);
        System.out.println();
        tree.postorderDFS(tree.root);
    }
}
