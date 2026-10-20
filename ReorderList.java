// LeetCode 143 - Reorder List
// Turns L0 -> L1 -> ... -> Ln into L0 -> Ln -> L1 -> Ln-1 -> L2 -> ...

// "public" = visible everywhere; the file name must match this class name.
public class ReorderList {

    // "static" = belongs to the class (no object needed); "void" = returns nothing.
    // Reorders the list in place, starting from "head".
    static void reorderList(ListNode head) {
        // If the list is empty (null) or has one node, nothing to reorder.
        // "||" means OR; "return" exits the method early.
        if (head == null || head.next == null) return;

        // ---------- STEP 1: find the middle ----------
        // "slow" will move 1 step at a time, starting at the head.
        ListNode slow = head;
        // "fast" will move 2 steps at a time, starting at the head.
        ListNode fast = head;
        // "while" repeats as long as the condition is true.
        // "&&" is AND: we need two more nodes ahead of fast to jump safely.
        while (fast.next != null && fast.next.next != null) {
            // Move slow forward by one node.
            slow = slow.next;
            // Move fast forward by two nodes.
            fast = fast.next.next;
        }
        // Now "slow" is the last node of the first half (the middle).

        // ---------- STEP 2: reverse the second half ----------
        // "prev" = the already reversed part; starts empty (null).
        ListNode prev = null;
        // "curr" = node being processed; the start of the second half.
        ListNode curr = slow.next;
        // Cut the list in two so the first half ends at "slow".
        slow.next = null;
        // Loop until we have processed every node of the second half.
        while (curr != null) {
            // Save the next node before we overwrite curr.next (else we lose it).
            ListNode next = curr.next;
            // Flip the arrow: curr now points backwards to prev.
            curr.next = prev;
            // Move prev forward to curr (the reversed part grows).
            prev = curr;
            // Move curr forward to the saved next node.
            curr = next;
        }
        // "prev" is now the head of the reversed second half.

        // ---------- STEP 3: merge the two halves alternately ----------
        // "first" walks the first half, starting at the real head.
        ListNode first = head;
        // "second" walks the reversed second half.
        ListNode second = prev;
        // The second half is never longer than the first, so loop on it.
        while (second != null) {
            // Remember the next nodes of both halves before relinking.
            ListNode t1 = first.next;
            ListNode t2 = second.next;
            // first -> second (take a node from the back).
            first.next = second;
            // second -> old next of first (continue with the front).
            second.next = t1;
            // Advance both pointers to their saved nodes.
            first = t1;
            second = t2;
        }
    }

    // Helper: builds a linked list from an array of numbers.
    // "int[]" is an array of ints; "..." isn't used, we pass the array directly.
    static ListNode build(int[] nums) {
        // "dummy" is a fake start node so we don't special-case the first node.
        ListNode dummy = new ListNode(0);
        // "tail" always points to the last node added.
        ListNode tail = dummy;
        // "for (int n : nums)" = for-each loop: n takes each value in nums.
        for (int n : nums) {
            // Create a node and attach it after tail.
            tail.next = new ListNode(n);
            // Move tail to the new last node.
            tail = tail.next;
        }
        // Real list starts after the dummy.
        return dummy.next;
    }

    // Helper: converts a list into text like "1 -> 2 -> 3".
    // "String" is the text type.
    static String show(ListNode head) {
        // StringBuilder efficiently builds text piece by piece.
        StringBuilder sb = new StringBuilder();
        // Walk through the list until we fall off the end (null).
        for (ListNode p = head; p != null; p = p.next) {
            // Add this node's value.
            sb.append(p.val);
            // Add an arrow only if another node follows.
            if (p.next != null) sb.append(" -> ");
        }
        // Convert the builder to a String and return it.
        return sb.toString();
    }

    // "main" is where Java starts running the program.
    public static void main(String[] args) {
        // Test cases: odd length and even length lists.
        int[][] tests = { {1, 2, 3, 4, 5}, {1, 2, 3, 4}, {1} };
        // Loop through each test array.
        for (int[] t : tests) {
            // Build the list from the array.
            ListNode head = build(t);
            // Print the list before reordering.
            System.out.println("Before: " + show(head));
            // Reorder it in place.
            reorderList(head);
            // Print the list after reordering.
            System.out.println("After : " + show(head));
            // Blank line for readability.
            System.out.println();
        }
    }
}

// (Kept below ReorderList so "java ReorderList.java" finds main in the first class.)
// "class" declares a blueprint (type) for objects; one node of the linked list.
class ListNode {
    // "int" is a whole-number type; "val" stores the number held by this node.
    int val;
    // "ListNode next" is a reference to the following node (null if none).
    ListNode next;

    // Constructor: runs when we write "new ListNode(x)"; same name as the class.
    ListNode(int val) {
        // "this.val" is the field; "val" on the right is the parameter. Copy it in.
        this.val = val;
    }
}
