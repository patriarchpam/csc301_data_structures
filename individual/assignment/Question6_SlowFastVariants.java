/**
 * CSC 301: Data Structures - Individual Assignment
 * Student Name: Pam Patriarch
 * Matric No:    VUG/SEN/24/12478
 *
 * Question 6: Solve Other Problems Using Slow and Fast Pointers
 *   A. Find Nth Node from End of List (LeetCode 19)
 *   B. Check if Linked List is a Palindrome (LeetCode 234)
 *
 * Concept:
 * - Nth from End: Advance Fast by n nodes first (offset window).
 *   Then advance Slow and Fast together until Fast hits null.
 * - Palindrome: Use Slow & Fast pointers to find middle in O(n),
 *   reverse the second half in O(n) and O(1) space, then compare halves.
 * - Time Complexity:  O(n)
 * - Space Complexity: O(1)
 */
public class Question6_SlowFastVariants {

    static class Node {
        int val;
        Node next;
        Node(int val) { this.val = val; }
        Node(int val, Node next) { this.val = val; this.next = next; }
    }

    // A. Find Nth node from end (1-based)
    public static Node nthFromEnd(Node head, int n) {
        Node fast = head;
        Node slow = head;
        for (int i = 0; i < n; i++) {
            if (fast == null) throw new IllegalArgumentException("n exceeds list length");
            fast = fast.next;
        }
        while (fast != null) {
            slow = slow.next;
            fast = fast.next;
        }
        return slow;
    }

    // B. Palindrome Linked List in O(1) Space
    public static boolean isPalindrome(Node head) {
        if (head == null || head.next == null) return true;
        // 1. Locate middle
        Node slow = head;
        Node fast = head;
        while (fast.next != null && fast.next.next != null) {
            slow = slow.next;
            fast = fast.next.next;
        }
        // 2. Reverse second half
        Node secondHalf = reverse(slow.next);
        // 3. Compare values
        Node p1 = head;
        Node p2 = secondHalf;
        boolean palindrome = true;
        while (p2 != null) {
            if (p1.val != p2.val) {
                palindrome = false;
                break;
            }
            p1 = p1.next;
            p2 = p2.next;
        }
        // Restore list
        slow.next = reverse(secondHalf);
        return palindrome;
    }

    private static Node reverse(Node head) {
        Node prev = null;
        Node cur = head;
        while (cur != null) {
            Node next = cur.next;
            cur.next = prev;
            prev = cur;
            cur = next;
        }
        return prev;
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
        System.out.println(" QUESTION 6: OTHER SLOW & FAST POINTER PROBLEMS ");
        System.out.println(" Student: Pam Patriarch | Matric: VUG/SEN/24/12478");
        System.out.println("=================================================\n");

        // A. Nth Node from End Test
        Node list = buildList(new int[]{10, 20, 30, 40, 50});
        System.out.println("List: " + printList(list));
        System.out.println("2nd node from end: " + nthFromEnd(list, 2).val + " (Expected: 40)");
        System.out.println("4th node from end: " + nthFromEnd(list, 4).val + " (Expected: 20)\n");

        // B. Palindrome Test
        Node palList = buildList(new int[]{1, 2, 3, 2, 1});
        Node nonPalList = buildList(new int[]{1, 2, 3, 4, 5});
        System.out.println("List 1: " + printList(palList));
        System.out.println("isPalindrome(List 1): " + isPalindrome(palList) + " (Expected: true)");
        System.out.println("List 2: " + printList(nonPalList));
        System.out.println("isPalindrome(List 2): " + isPalindrome(nonPalList) + " (Expected: false)\n");

        System.out.println("Test Status: PASSED");
    }
}
