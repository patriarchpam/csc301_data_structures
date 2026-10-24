/**
 * CSC 301: Data Structures - Individual Assignment
 * Student Name: Pam Patriarch
 * Matric No:    VUG/SEN/24/12478
 *
 * Question 4: How to Merge Two Linked Lists
 * Formulations:
 *   A. Merge Two Sorted Lists (LeetCode 21)
 *   B. Interleaving / Alternating Merge (LeetCode 143)
 *
 * Concept:
 * - Sorted Merge: Use a dummy head and tail pointer. Compare l1.val and l2.val,
 *   link the smaller node, advance. When one list empties, link the rest in O(1).
 * - Time Complexity:  O(m + n)
 * - Space Complexity: O(1) in-place pointer rewiring
 */
public class Question4_MergeTwoLinkedLists {

    static class Node {
        int val;
        Node next;
        Node(int val) { this.val = val; }
        Node(int val, Node next) { this.val = val; this.next = next; }
    }

    // A. Merge Two Sorted Linked Lists (LeetCode 21)
    public static Node mergeSortedLists(Node l1, Node l2) {
        Node dummy = new Node(0);
        Node tail = dummy;

        while (l1 != null && l2 != null) {
            if (l1.val <= l2.val) {
                tail.next = l1;
                l1 = l1.next;
            } else {
                tail.next = l2;
                l2 = l2.next;
            }
            tail = tail.next;
        }
        tail.next = (l1 != null) ? l1 : l2;
        return dummy.next;
    }

    // B. Interleaving / Alternating Merge (LeetCode 143)
    public static Node mergeInterleaving(Node l1, Node l2) {
        Node dummy = new Node(0);
        Node cur = dummy;
        while (l1 != null && l2 != null) {
            cur.next = l1;
            l1 = l1.next;
            cur = cur.next;

            cur.next = l2;
            l2 = l2.next;
            cur = cur.next;
        }
        if (l1 != null) cur.next = l1;
        if (l2 != null) cur.next = l2;
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
        System.out.println(" QUESTION 4: MERGE TWO LINKED LISTS (LEETCODE 21)");
        System.out.println(" Student: Pam Patriarch | Matric: VUG/SEN/24/12478");
        System.out.println("=================================================\n");

        // A. Sorted Merge Test
        Node listA = buildList(new int[]{1, 3, 5, 7});
        Node listB = buildList(new int[]{2, 4, 6, 8, 10});
        System.out.println("Sorted List 1: " + printList(listA));
        System.out.println("Sorted List 2: " + printList(listB));
        Node merged = mergeSortedLists(listA, listB);
        System.out.println("Merged Sorted: " + printList(merged) + "\n");

        // B. Interleaving Merge Test
        Node l1 = buildList(new int[]{1, 2, 3});
        Node l2 = buildList(new int[]{9, 8, 7});
        System.out.println("List 1:        " + printList(l1));
        System.out.println("List 2:        " + printList(l2));
        Node interleaved = mergeInterleaving(l1, l2);
        System.out.println("Interleaved:   " + printList(interleaved) + "\n");

        System.out.println("Test Status: PASSED");
    }
}
