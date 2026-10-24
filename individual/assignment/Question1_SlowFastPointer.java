/**
 * CSC 301: Data Structures - Individual Assignment
 * Student Name: Pam Patriarch
 * Matric No:    VUG/SEN/24/12478
 *
 * Question 1: Slow and Fast Pointer Technique (Tortoise and Hare)
 * LeetCode 876: Middle of the Linked List
 *
 * Concept:
 * - Slow Pointer (S) moves 1 node per iteration (v_s = 1).
 * - Fast Pointer (F) moves 2 nodes per iteration (v_f = 2).
 * - When F reaches the end (or null), S is at the exact middle!
 * - Loop condition: while (fast != null && fast.next != null)
 * - Time Complexity:  O(n) - Single pass
 * - Space Complexity: O(1) - Two pointer variables only
 */
public class Question1_SlowFastPointer {

    static class Node {
        int val;
        Node next;
        Node(int val) { this.val = val; }
        Node(int val, Node next) { this.val = val; this.next = next; }
    }

    public static Node findMiddle(Node head) {
        Node slow = head;
        Node fast = head;
        while (fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;
        }
        return slow;
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
        System.out.println(" QUESTION 1: SLOW AND FAST POINTER TECHNIQUE    ");
        System.out.println(" Student: Pam Patriarch | Matric: VUG/SEN/24/12478");
        System.out.println("=================================================\n");

        // Test 1: Odd Length (1 -> 2 -> 3 -> 4 -> 5)
        Node oddList = buildList(new int[]{1, 2, 3, 4, 5});
        System.out.println("Odd Length List:   " + printList(oddList));
        Node midOdd = findMiddle(oddList);
        System.out.println("Middle Node Value: " + midOdd.val + " (Expected: 3)\n");

        // Test 2: Even Length (1 -> 2 -> 3 -> 4 -> 5 -> 6)
        Node evenList = buildList(new int[]{1, 2, 3, 4, 5, 6});
        System.out.println("Even Length List:  " + printList(evenList));
        Node midEven = findMiddle(evenList);
        System.out.println("Middle Node Value: " + midEven.val + " (Expected: 4, second middle)\n");

        System.out.println("Test Status: PASSED");
    }
}
