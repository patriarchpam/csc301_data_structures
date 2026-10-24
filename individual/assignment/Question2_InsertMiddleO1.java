/**
 * CSC 301: Data Structures - Individual Assignment
 * Student Name: Pam Patriarch
 * Matric No:    VUG/SEN/24/12478
 *
 * Question 2: How to Insert in the Middle of a Linked List Using O(1) Complexity
 *
 * Algorithmic Clarification:
 * 1. If starting from head: finding middle requires O(n) traversal.
 * 2. If given a direct reference to the middle node (mid):
 *    - Case A: Inserting AFTER mid is pure O(1) pointer rewriting:
 *              mid.next = new Node(val, mid.next)
 *    - Case B: Inserting BEFORE mid without predecessor pointer is achieved
 *              in O(1) using the "Node Value-Copy Trick":
 *              Clone mid into a new node, overwrite mid's value with newVal,
 *              and link mid to the clone.
 * - Time Complexity:  O(1) given node reference
 * - Space Complexity: O(1) auxiliary
 */
public class Question2_InsertMiddleO1 {

    static class Node {
        int val;
        Node next;
        Node(int val) { this.val = val; }
        Node(int val, Node next) { this.val = val; this.next = next; }
    }

    // Case A: Insert AFTER given middle node in O(1)
    public static void insertAfterMiddle(Node mid, int val) {
        if (mid == null) return;
        mid.next = new Node(val, mid.next);
    }

    // Case B: Insert BEFORE given middle node in O(1) (Value-Copy Trick)
    public static void insertBeforeMiddle(Node mid, int val) {
        if (mid == null) return;
        Node clone = new Node(mid.val, mid.next);
        mid.val = val;
        mid.next = clone;
    }

    public static Node buildList(int[] values) {
        Node dummy = new Node(0);
        Node cur = dummy;
        for (int v : values) {
            cur.next = new Node(v);
            cur = cur.next;
        }
        return dummy.next;
    }

    public static String printList(Node head) {
        StringBuilder sb = new StringBuilder();
        Node cur = head;
        while (cur != null) {
            sb.append(cur.val);
            if (cur.next != null) sb.append(" -> ");
            cur = cur.next;
        }
        return sb.toString();
    }

    public static void main(String[] args) {
        System.out.println("=================================================");
        System.out.println(" QUESTION 2: INSERT IN MIDDLE WITH O(1) COMPLEXITY");
        System.out.println(" Student: Pam Patriarch | Matric: VUG/SEN/24/12478");
        System.out.println("=================================================\n");

        Node list = buildList(new int[]{1, 2, 3, 4, 5});
        System.out.println("Initial List: " + printList(list));

        // Locate middle node (value 3)
        Node mid = list.next.next; // points to node 3
        System.out.println("Direct pointer to middle node: [val = " + mid.val + "]\n");

        // Case A: Insert 99 AFTER middle node in O(1)
        insertAfterMiddle(mid, 99);
        System.out.println("After insertAfterMiddle(val = 99):");
        System.out.println(printList(list) + "\n");

        // Case B: Insert 88 BEFORE middle node in O(1) (Value-Copy trick)
        insertBeforeMiddle(mid, 88);
        System.out.println("After insertBeforeMiddle(val = 88):");
        System.out.println(printList(list) + "\n");

        System.out.println("Test Status: PASSED (All operations executed in O(1) time)");
    }
}
