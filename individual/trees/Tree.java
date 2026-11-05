import java.util.LinkedList;
import java.util.Queue;

public class Tree {

    // 1. DFS (Depth-First Search) - Goes deep down one branch before the next
    public static void dfs(Node node) {
        if (node == null) {
            return;
        }
        System.out.print(node.data + " "); // Visit current node
        dfs(node.left);                    // Go all the way left
        dfs(node.right);                   // Go all the way right
    }

    // 2. BFS (Breadth-First Search) - Goes level by level using a Queue
    public static void bfs(Node root) {
        if (root == null) {
            return;
        }
        Queue<Node> q = new LinkedList<>();
        q.add(root);

        while (!q.isEmpty()) {
            Node current = q.poll();
            System.out.print(current.data + " ");

            if (current.left != null) {
                q.add(current.left);
            }
            if (current.right != null) {
                q.add(current.right);
            }
        }
    }

    public static void main(String[] args) {
        Node A = new Node(10);
        Node B = new Node(15);
        Node C = new Node(20);
        Node d = new Node(40);

        A.left = B;
        A.left.left = C;
        A.right = d;

        System.out.print("DFS: ");
        dfs(A); // Output: 10 15 20 40

        System.out.println();

        System.out.print("BFS: ");
        bfs(A); // Output: 10 15 40 20
    }
}

class Node {
    int data;
    Node left;
    Node right;

    public Node(int data) {
        this.data = data;
    }
}
