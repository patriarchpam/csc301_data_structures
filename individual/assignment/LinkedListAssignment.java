/**
 * CSC 301: Data Structures - Individual Assignment
 * Student Name: Pam Patriarch
 * Matric No:    VUG/SEN/24/12478
 *
 * File: LinkedListAssignment.java
 * Topics:
 *   1. Slow and Fast Pointer Technique (Tortoise and Hare)
 *   2. Insertion in the Middle of a Linked List in O(1) Complexity
 *      - Direct link after middle pointer: O(1)
 *      - Node-value shift technique (insert before given node without prev pointer): O(1)
 *      - Full find-and-insert from head: O(n) search + O(1) linking
 *   3. Sum Two Linked Lists (LeetCode 2 - Add Two Numbers)
 *   4. Merge Two Linked Lists:
 *      - Merge Two Sorted Lists (LeetCode 21)
 *      - Interleaving Merge (LeetCode 143)
 *   5. Detect Circle/Cycle in Linked List (LeetCode 141 & 142)
 *   6. Additional Slow & Fast Pointer Problems:
 *      - Middle of Linked List (LeetCode 876)
 *      - Nth Node from End (LeetCode 19)
 *      - Cycle Start Origin (LeetCode 142)
 *      - Palindrome Linked List (LeetCode 234)
 */
public class LinkedListAssignment {

    // ==========================================
    // Core Node Definition
    // ==========================================
    public static class Node {
        public int val;
        public Node next;

        public Node(int val) {
            this.val = val;
        }

        public Node(int val, Node next) {
            this.val = val;
            this.next = next;
        }
    }

    // ==========================================
    // 1 & 6a. Find Middle Node (LC 876)
    // Uses Slow (1 step) and Fast (2 steps) pointers.
    // For even length, returns the second middle node.
    // Time: O(n), Space: O(1)
    // ==========================================
    public static Node middle(Node head) {
        Node slow = head;
        Node fast = head;
        while (fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;
        }
        return slow;
    }

    // ==========================================
    // 2. Insertion in the Middle in O(1) Complexity
    // Case A: When pointer to the middle node is already given.
    // Inserting immediately after `midNode` is pure O(1) pointer rewriting.
    // Time: O(1), Space: O(1)
    // ==========================================
    public static void insertAfterNodeO1(Node midNode, int val) {
        if (midNode == null) return;
        midNode.next = new Node(val, midNode.next);
    }

    // Case B: Inserting BEFORE a given middle node in O(1) (Value-Swap Trick)
    // Avoids needing a predecessor pointer.
    // Time: O(1), Space: O(1)
    // ==========================================
    public static void insertBeforeNodeO1(Node midNode, int val) {
        if (midNode == null) return;
        // 1. Create a clone node of midNode
        Node clone = new Node(midNode.val, midNode.next);
        // 2. Overwrite midNode's value with the new value
        midNode.val = val;
        // 3. Link midNode to the clone
        midNode.next = clone;
    }

    // Case C: Standard traversal from head to middle node
    // Time: O(n) search + O(1) link = O(n) total, Space: O(1)
    // ==========================================
    public static Node insertMiddleFromHead(Node head, int val) {
        if (head == null) return new Node(val);
        Node slow = head;
        Node fast = head;
        while (fast.next != null && fast.next.next != null) {
            slow = slow.next;
            fast = fast.next.next;
        }
        slow.next = new Node(val, slow.next);
        return head;
    }

    // ==========================================
    // 3. Sum Two Linked Lists (LC 2 - Add Two Numbers)
    // Digits stored in reverse order.
    // Example: (2 -> 4 -> 3) + (5 -> 6 -> 4) = (7 -> 0 -> 8) [342 + 465 = 807]
    // Time: O(max(m, n)), Space: O(max(m, n))
    // ==========================================
    public static Node addTwo(Node l1, Node l2) {
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

    // ==========================================
    // 4a. Merge Two Sorted Linked Lists (LC 21)
    // Splices nodes from both sorted lists in non-decreasing order.
    // Time: O(m + n), Space: O(1)
    // ==========================================
    public static Node mergeTwoLists(Node l1, Node l2) {
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

    // ==========================================
    // 4b. Interleaving Merge (LC 143)
    // Alternates nodes: l1[0] -> l2[0] -> l1[1] -> l2[1]...
    // Time: O(m + n), Space: O(1)
    // ==========================================
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

    // ==========================================
    // 5. Detect Cycle/Circle in Linked List (LC 141)
    // Floyd's Cycle Detection Algorithm.
    // Time: O(n), Space: O(1)
    // ==========================================
    public static boolean hasCycle(Node head) {
        Node slow = head;
        Node fast = head;
        while (fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;
            if (slow == fast) {
                return true;
            }
        }
        return false;
    }

    // ==========================================
    // 6c. Find Where Cycle Begins (LC 142)
    // Phase 1: Detect meeting point inside the cycle.
    // Phase 2: Reset slow to head, advance both 1 step until collision.
    // Time: O(n), Space: O(1)
    // ==========================================
    public static Node cycleStart(Node head) {
        Node slow = head;
        Node fast = head;
        while (fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;
            if (slow == fast) {
                slow = head;
                while (slow != fast) {
                    slow = slow.next;
                    fast = fast.next;
                }
                return slow;
            }
        }
        return null;
    }

    // ==========================================
    // 6b. Find Nth Node From End (LC 19)
    // Advances fast pointer by n nodes first, then advances both together.
    // Time: O(n), Space: O(1)
    // ==========================================
    public static Node nthFromEnd(Node head, int n) {
        Node fast = head;
        Node slow = head;
        for (int i = 0; i < n; i++) {
            if (fast == null) {
                throw new IllegalArgumentException("n (" + n + ") is larger than list length");
            }
            fast = fast.next;
        }
        while (fast != null) {
            slow = slow.next;
            fast = fast.next;
        }
        return slow;
    }

    // ==========================================
    // 6d. Check If Linked List Is Palindrome (LC 234)
    // 1. Find middle with slow & fast pointers
    // 2. Reverse second half
    // 3. Compare values from head and reversed second half
    // Time: O(n), Space: O(1)
    // ==========================================
    public static boolean isPalindrome(Node head) {
        if (head == null || head.next == null) return true;
        // 1. Find middle
        Node slow = head;
        Node fast = head;
        while (fast.next != null && fast.next.next != null) {
            slow = slow.next;
            fast = fast.next.next;
        }
        // 2. Reverse second half
        Node secondHalf = reverse(slow.next);
        // 3. Compare
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

    // ==========================================
    // Helpers & Test Harness
    // ==========================================
    public static Node buildList(int[] values) {
        if (values == null || values.length == 0) return null;
        Node dummy = new Node(0);
        Node cur = dummy;
        for (int v : values) {
            cur.next = new Node(v);
            cur = cur.next;
        }
        return dummy.next;
    }

    public static String listToString(Node head) {
        if (head == null) return "EMPTY";
        StringBuilder sb = new StringBuilder();
        Node cur = head;
        int count = 0;
        while (cur != null && count < 25) {
            sb.append(cur.val);
            if (cur.next != null) sb.append(" -> ");
            cur = cur.next;
            count++;
        }
        if (cur != null) sb.append(" -> ... (truncated)");
        return sb.toString();
    }

    public static void main(String[] args) {
        System.out.println("===============================================================");
        System.out.println("    CSC 301 DATA STRUCTURES: COMPLETE LINKED LIST SUITE       ");
        System.out.println("    Student: Pam Patriarch | Matric: VUG/SEN/24/12478         ");
        System.out.println("===============================================================\n");

        // 1. Slow & Fast Pointer (Middle)
        System.out.println("--- 1. Slow and Fast Pointer (Middle of List) ---");
        Node l1 = buildList(new int[]{1, 2, 3, 4, 5});
        System.out.println("List: " + listToString(l1));
        System.out.println("Middle Node: " + middle(l1).val + " (Expected: 3)\n");

        // 2. Insertion in Middle in O(1)
        System.out.println("--- 2. Insertion at Middle with O(1) Complexity ---");
        Node midRef = middle(l1); // pointer to node 3
        System.out.println("Given pointer to mid node (value = " + midRef.val + ")");
        insertAfterNodeO1(midRef, 99);
        System.out.println("After insertAfterNodeO1(midRef, 99):  " + listToString(l1));
        insertBeforeNodeO1(midRef, 88);
        System.out.println("After insertBeforeNodeO1(midRef, 88): " + listToString(l1) + "\n");

        // 3. Sum Two Linked Lists
        System.out.println("--- 3. Sum Two Linked Lists (LC 2) ---");
        Node numA = buildList(new int[]{2, 4, 3});
        Node numB = buildList(new int[]{5, 6, 4});
        System.out.println("Num A (342): " + listToString(numA));
        System.out.println("Num B (465): " + listToString(numB));
        System.out.println("Sum Result:  " + listToString(addTwo(numA, numB)) + " (Expected: 7 -> 0 -> 8)\n");

        // 4. Merge Two Linked Lists
        System.out.println("--- 4. Merge Two Linked Lists ---");
        Node s1 = buildList(new int[]{1, 3, 5, 7});
        Node s2 = buildList(new int[]{2, 4, 6, 8});
        System.out.println("Sorted List 1: " + listToString(s1));
        System.out.println("Sorted List 2: " + listToString(s2));
        System.out.println("Merged Sorted: " + listToString(mergeTwoLists(s1, s2)) + "\n");

        // 5. Detect Circle / Cycle (LC 141 & 142)
        System.out.println("--- 5. Detect Circle / Cycle (Floyd's Algorithm) ---");
        Node c1 = new Node(1), c2 = new Node(2), c3 = new Node(3), c4 = new Node(4), c5 = new Node(5);
        c1.next = c2; c2.next = c3; c3.next = c4; c4.next = c5;
        System.out.println("Before cycle: hasCycle = " + hasCycle(c1));
        c5.next = c3; // 5 -> 3
        System.out.println("Created loop (5 points back to 3):");
        System.out.println("hasCycle(c1)  = " + hasCycle(c1));
        System.out.println("cycleStart(c1) = " + cycleStart(c1).val + " (Expected: 3)\n");

        // 6. Additional Slow & Fast Pointer Problems
        System.out.println("--- 6. Additional Slow & Fast Pointer Problems ---");
        Node nList = buildList(new int[]{10, 20, 30, 40, 50});
        System.out.println("List: " + listToString(nList));
        System.out.println("2nd from end: " + nthFromEnd(nList, 2).val + " (Expected: 40)");

        Node palin = buildList(new int[]{1, 2, 3, 2, 1});
        Node notPalin = buildList(new int[]{1, 2, 3, 4, 5});
        System.out.println("isPalindrome([1,2,3,2,1]): " + isPalindrome(palin) + " (Expected: true)");
        System.out.println("isPalindrome([1,2,3,4,5]): " + isPalindrome(notPalin) + " (Expected: false)\n");

        System.out.println("===============================================================");
        System.out.println("        ALL LINKED LIST PROBLEMS EXECUTED SUCCESSFULLY!       ");
        System.out.println("===============================================================");
    }
}
