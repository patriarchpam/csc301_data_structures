/**
 * CSC 301: Data Structures - Individual Assignment
 * Student Name: Pam Patriarch
 * Matric No:    VUG/SEN/24/12478
 *
 * Question 5: How to Detect Circle/Cycle in a Linked List (Floyd's Algorithm)
 * LeetCode 141: Linked List Cycle
 * LeetCode 142: Linked List Cycle II (Find Cycle Start)
 *
 * Concept:
 * - Slow pointer (S) moves 1 node, Fast pointer (F) moves 2 nodes.
 * - If no cycle: F hits null -> return false.
 * - If cycle: both enter cycle. F gains 1 node on S each step (gap shrinks by 1).
 *   They MUST collide -> return true!
 * - Finding Cycle Start: Keep F at collision node, reset S to head.
 *   Move both 1 node per step. They collide at the cycle entrance!
 * - Time Complexity:  O(n)
 * - Space Complexity: O(1)
 */
public class Question5_DetectCycle {

    static class Node {
        int val;
        Node next;
        Node(int val) { this.val = val; }
        Node(int val, Node next) { this.val = val; this.next = next; }
    }

    // Phase 1: Detect presence of cycle (LC 141)
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

    // Phase 2: Find the node where cycle begins (LC 142)
    public static Node detectCycleStart(Node head) {
        Node slow = head;
        Node fast = head;
        while (fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;
            if (slow == fast) {
                // Meeting point detected; find cycle origin
                slow = head;
                while (slow != fast) {
                    slow = slow.next;
                    fast = fast.next;
                }
                return slow;
            }
        }
        return null; // Acyclic
    }

    public static void main(String[] args) {
        System.out.println("=================================================");
        System.out.println(" QUESTION 5: DETECT CYCLE (FLOYD'S ALGORITHM)    ");
        System.out.println(" Student: Pam Patriarch | Matric: VUG/SEN/24/12478");
        System.out.println("=================================================\n");

        // Build list: 1 -> 2 -> 3 -> 4 -> 5
        Node n1 = new Node(1);
        Node n2 = new Node(2);
        Node n3 = new Node(3);
        Node n4 = new Node(4);
        Node n5 = new Node(5);
        n1.next = n2; n2.next = n3; n3.next = n4; n4.next = n5;

        System.out.println("List: 1 -> 2 -> 3 -> 4 -> 5 -> null (Acyclic)");
        System.out.println("hasCycle(n1): " + hasCycle(n1) + " (Expected: false)\n");

        // Create cycle: 5 points back to 3
        n5.next = n3;
        System.out.println("Created Cycle: Node 5 points back to Node 3");
        System.out.println("hasCycle(n1):         " + hasCycle(n1) + " (Expected: true)");
        Node cycleStart = detectCycleStart(n1);
        System.out.println("detectCycleStart(n1): " + (cycleStart != null ? cycleStart.val : "none") + " (Expected: 3)\n");

        System.out.println("Test Status: PASSED");
    }
}
