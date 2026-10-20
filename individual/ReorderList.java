/**
 * CSC 301 - Data Structures & Algorithms
 * Individual Assignment: LeetCode 143 - Reorder List
 * 
 * Student Name: Pam Patriarch
 * Matric Number: VUG/SEN/24/12478
 * 
 * Design Pattern: Modular Function Decomposition
 * -------------------------------------------------------------
 * Instead of one monolithic method, the problem is divided into
 * three discrete, testable sub-problems:
 *   1. findMiddle(head)   - Fast & Slow Pointer Strategy
 *   2. reverse(head)      - Iterative 3-pointer list reversal
 *   3. merge(l1, l2)      - Alternating pointer interleave
 */

public class ReorderList {

    /**
     * Primary entry point to reorder the linked list in-place:
     * L0 -> L1 -> ... -> Ln becomes L0 -> Ln -> L1 -> Ln-1 -> ...
     */
    public void reorderList(ListNode head) {
        if (head == null || head.next == null || head.next.next == null) {
            return;
        }

        // Step 1: Split the list at the middle
        ListNode mid = findMiddle(head);
        ListNode secondHalf = mid.next;
        mid.next = null; // Sever the connection between halves

        // Step 2: Reverse the second half
        secondHalf = reverse(secondHalf);

        // Step 3: Interleave both halves
        merge(head, secondHalf);
    }

    /**
     * Helper 1: Locates the end of the first half (midpoint).
     * Uses Floyd's Cycle-Finding / Tortoise-and-Hare approach.
     */
    private ListNode findMiddle(ListNode head) {
        ListNode slow = head;
        ListNode fast = head;

        while (fast.next != null && fast.next.next != null) {
            slow = slow.next;
            fast = fast.next.next;
        }
        return slow;
    }

    /**
     * Helper 2: Reverses a singly-linked list iteratively.
     * Time: O(m), Space: O(1)
     */
    private ListNode reverse(ListNode head) {
        ListNode prev = null;
        ListNode curr = head;

        while (curr != null) {
            ListNode nextTemp = curr.next;
            curr.next = prev;
            prev = curr;
            curr = nextTemp;
        }
        return prev;
    }

    /**
     * Helper 3: Merges two lists (l1 and l2) alternately.
     */
    private void merge(ListNode l1, ListNode l2) {
        while (l1 != null && l2 != null) {
            ListNode l1Next = l1.next;
            ListNode l2Next = l2.next;

            l1.next = l2;
            if (l1Next == null) break;

            l2.next = l1Next;
            l1 = l1Next;
            l2 = l2Next;
        }
    }

    // =========================================================================
    // Utility & Test Driver
    // =========================================================================

    public static ListNode fromArray(int[] values) {
        if (values == null || values.length == 0) return null;
        ListNode head = new ListNode(values[0]);
        ListNode current = head;
        for (int i = 1; i < values.length; i++) {
            current.next = new ListNode(values[i]);
            current = current.next;
        }
        return head;
    }

    public static void printList(ListNode head) {
        if (head == null) {
            System.out.println("null");
            return;
        }
        ListNode curr = head;
        while (curr != null) {
            System.out.print(curr.val + (curr.next != null ? " -> " : " -> null\n"));
            curr = curr.next;
        }
    }

    public static void main(String[] args) {
        ReorderList solver = new ReorderList();

        int[][] testSuites = {
            {1, 2, 3, 4, 5},       // Odd length
            {1, 2, 3, 4},          // Even length
            {10, 20, 30, 40, 50, 60}, // Longer even length
            {7, 9},                // Minimal 2-node list
            {42}                   // Single-node edge case
        };

        System.out.println("====================================================");
        System.out.println(" CSC 301: REORDER LIST - INDIVIDUAL SOLUTION");
        System.out.println(" Student: Pam Patriarch (VUG/SEN/24/12478)");
        System.out.println("====================================================\n");

        for (int i = 0; i < testSuites.length; i++) {
            ListNode list = fromArray(testSuites[i]);
            System.out.println("Test Case #" + (i + 1) + ":");
            System.out.print("  Original : ");
            printList(list);

            solver.reorderList(list);

            System.out.print("  Reordered: ");
            printList(list);
            System.out.println();
        }
    }
}

class ListNode {
    int val;
    ListNode next;

    ListNode() {}

    ListNode(int val) {
        this.val = val;
    }

    ListNode(int val, ListNode next) {
        this.val = val;
        this.next = next;
    }
}
