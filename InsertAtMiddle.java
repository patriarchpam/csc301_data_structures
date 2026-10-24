public class InsertAtMiddle {

    static class Node {
        int data;
        Node next;

        Node(int data) {
            this.data = data;
            this.next = null;
        }
    }

    public static Node insertMiddle(Node head, int data) {
        // If list is empty
        if (head == null) {
            return new Node(data);
        }

        // --- COUNTING SYSTEM ---
        // 1. Count total nodes in the list
        int totalNodes = 0;
        Node temp = head;
        while (temp != null) {
            totalNodes++;
            temp = temp.next;
        }

        // 2. Find the middle position
        int mid = totalNodes / 2;

        // 3. Count up to the middle node using while loop
        int count = 1;
        Node current = head;
        while (count < mid) {
            current = current.next;
            count++;
        }

        // 4. Insert the new node
        Node newNode = new Node(data);
        newNode.next = current.next;
        current.next = newNode;

        return head;
    }

    public static void main(String[] args) {
        // Initial list: 10 -> 20 -> 40 -> 50 -> null
        Node head = new Node(10);
        head.next = new Node(20);
        head.next.next = new Node(40);
        head.next.next.next = new Node(50);

        // Insert 30 in the middle (no printing)
        head = insertMiddle(head, 30);
    }
}
