import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;

/**
 * CSC 301: Data Structures - Group Assignment
 * Question 3: Explain Level Order Traversal
 *
 * Demonstrates:
 * 1. Standard Iterative Level Order Traversal using a FIFO Queue (O(n) time, O(n) space)
 * 2. Level-by-Level Grouped Level Order Traversal using Queue size per level
 * 3. Recursive Level Order Traversal (using tree height) for comparison
 */
public class Question3_LevelOrderTraversal {

    static class Node {
        int data;
        Node left;
        Node right;

        public Node(int data) {
            this.data = data;
            this.left = null;
            this.right = null;
        }
    }

    // =========================================================================
    // 1. Standard Iterative Level Order Traversal (BFS using Queue)
    // =========================================================================
    public static void levelOrder(Node root) {
        if (root == null) {
            return;
        }

        Queue<Node> q = new LinkedList<>();
        q.add(root); // Step 1: Enqueue root node at Level 0

        while (!q.isEmpty()) {
            // Step 2: Dequeue the front node and visit it
            Node current = q.poll();
            System.out.print(current.data + " ");

            // Step 3: Enqueue left child first (if present)
            if (current.left != null) {
                q.add(current.left);
            }

            // Step 4: Enqueue right child next (if present)
            if (current.right != null) {
                q.add(current.right);
            }
        }
    }

    // =========================================================================
    // 2. Level-by-Level Grouped Traversal (tracks each level separately)
    // =========================================================================
    public static List<List<Integer>> levelOrderGrouped(Node root) {
        List<List<Integer>> result = new ArrayList<>();
        if (root == null) {
            return result;
        }

        Queue<Node> q = new LinkedList<>();
        q.add(root);

        while (!q.isEmpty()) {
            int levelSize = q.size(); // Number of nodes currently at this level
            List<Integer> currentLevel = new ArrayList<>();

            for (int i = 0; i < levelSize; i++) {
                Node current = q.poll();
                currentLevel.add(current.data);

                if (current.left != null) {
                    q.add(current.left);
                }
                if (current.right != null) {
                    q.add(current.right);
                }
            }
            result.add(currentLevel);
        }
        return result;
    }

    // =========================================================================
    // 3. Recursive Level Order Traversal (Height-based approach)
    // =========================================================================
    public static void levelOrderRecursive(Node root) {
        int h = height(root);
        for (int i = 1; i <= h; i++) {
            printGivenLevel(root, i);
        }
    }

    private static int height(Node root) {
        if (root == null) {
            return 0;
        }
        int leftHeight = height(root.left);
        int rightHeight = height(root.right);
        return Math.max(leftHeight, rightHeight) + 1;
    }

    private static void printGivenLevel(Node root, int level) {
        if (root == null) {
            return;
        }
        if (level == 1) {
            System.out.print(root.data + " ");
        } else if (level > 1) {
            printGivenLevel(root.left, level - 1);
            printGivenLevel(root.right, level - 1);
        }
    }

    // =========================================================================
    // Main Method - Testing Examples 1 and 2
    // =========================================================================
    public static void main(String[] args) {
        // Example 1: Class Example Tree (4 nodes)
        //        10
        //       /  \
        //     15    40
        //    /
        //  20
        Node ex1Root = new Node(10);
        ex1Root.left = new Node(15);
        ex1Root.right = new Node(40);
        ex1Root.left.left = new Node(20);

        System.out.println("=== Example 1: Class Binary Tree ===");
        System.out.print("Flat Level Order (BFS):      ");
        levelOrder(ex1Root);
        System.out.println();
        System.out.println("Grouped by Level:            " + levelOrderGrouped(ex1Root));
        System.out.println();

        // Example 2: Complete 3-Level Binary Tree (7 nodes)
        //            10
        //          /    \
        //        15      40
        //       /  \    /  \
        //     20   25  35   50
        Node ex2Root = new Node(10);
        ex2Root.left = new Node(15);
        ex2Root.right = new Node(40);
        ex2Root.left.left = new Node(20);
        ex2Root.left.right = new Node(25);
        ex2Root.right.left = new Node(35);
        ex2Root.right.right = new Node(50);

        System.out.println("=== Example 2: 3-Level Binary Tree ===");
        System.out.print("Flat Level Order (BFS):      ");
        levelOrder(ex2Root);
        System.out.println();
        System.out.println("Grouped by Level:            " + levelOrderGrouped(ex2Root));
        System.out.print("Recursive Level Order:       ");
        levelOrderRecursive(ex2Root);
        System.out.println();
    }
}

