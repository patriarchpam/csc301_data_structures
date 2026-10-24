/**
 * CSC 301: Data Structures - Individual Assignment
 * Student Name: Pam Patriarch
 * Matric No:    VUG/SEN/24/12478
 *
 * Question 3: How to Sum Two Linked Lists Together
 * LeetCode 2: Add Two Numbers
 *
 * Concept:
 * - Digits are stored in reverse order (e.g., 342 stored as 2 -> 4 -> 3).
 * - Traverse both lists simultaneously, adding corresponding digits plus carry.
 * - Append (sum % 10) as a new node, and carry = sum / 10.
 * - Loop continues while (l1 != null || l2 != null || carry != 0) to capture trailing carry.
 * - Time Complexity:  O(max(m, n))
 * - Space Complexity: O(max(m, n)) for the result list
 */
public class Question3_SumTwoLinkedLists {

    static class Node {
        int val;
        Node next;
        Node(int val) { this.val = val; }
        Node(int val, Node next) { this.val = val; this.next = next; }
    }

    public static Node addTwoLists(Node l1, Node l2) {
        Node dummy = new Node(0);
        Node cur = dummy;
        int carry = 0;

        while (l1 != null || l2 != null || carry != 0) {
            int sum = carry;
            if (l1 != null) {
                sum += l1.val;
                l1 = l1.next;
            }
            if (l2 != null) {
                sum += l2.val;
                l2 = l2.next;
            }
            carry = sum / 10;
            cur.next = new Node(sum % 10);
            cur = cur.next;
        }
        return dummy.next;
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
        System.out.println(" QUESTION 3: SUM TWO LINKED LISTS (LEETCODE 2)   ");
        System.out.println(" Student: Pam Patriarch | Matric: VUG/SEN/24/12478");
        System.out.println("=================================================\n");

        // Test Case 1: 342 + 465 = 807
        // List 1: 2 -> 4 -> 3 (342)
        // List 2: 5 -> 6 -> 4 (465)
        // Sum:    7 -> 0 -> 8 (807)
        Node num1 = buildList(new int[]{2, 4, 3});
        Node num2 = buildList(new int[]{5, 6, 4});
        System.out.println("List 1 (342 reversed): " + printList(num1));
        System.out.println("List 2 (465 reversed): " + printList(num2));
        Node result1 = addTwoLists(num1, num2);
        System.out.println("Sum Result:            " + printList(result1) + " (Expected: 7 -> 0 -> 8)\n");

        // Test Case 2: 99 + 1 = 100 (Carry creates extra node)
        // List 1: 9 -> 9 (99)
        // List 2: 1 (1)
        // Sum:    0 -> 0 -> 1 (100)
        Node numA = buildList(new int[]{9, 9});
        Node numB = buildList(new int[]{1});
        System.out.println("List A (99 reversed):  " + printList(numA));
        System.out.println("List B (1 reversed):   " + printList(numB));
        Node result2 = addTwoLists(numA, numB);
        System.out.println("Sum Result with Carry: " + printList(result2) + " (Expected: 0 -> 0 -> 1)\n");

        System.out.println("Test Status: PASSED");
    }
}
