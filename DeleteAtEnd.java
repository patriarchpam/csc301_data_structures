// Simple program to delete the last node (end) of a Singly Linked List

public class DeleteAtEnd {

    // Simple Node definition
    static class Node {
        int data;
        Node next;

        Node(int data) {
            this.data = data;
            this.next = null;
        }
    }

    // Function to delete the last node
    public static Node deleteLast(Node head) {
        // Case 1: Empty list
        if (head == null) {
            System.out.println("List is empty.");
            return null;
        }

        // Case 2: Only one node in the list
        if (head.next == null) {
            return null;
        }

        // Case 3: More than one node
        // Stop at the second-to-last node
        Node current = head;
        while (current.next.next != null) {
            current = current.next;
        }

        // Disconnect the last node
        current.next = null;
        return head;
    }

    // Helper to print the list
    public static void printList(Node head) {
        if (head == null) {
            System.out.println("Empty List");
            return;
        }

        Node temp = head;
        while (temp != null) {
            System.out.print(temp.data + (temp.next != null ? " -> " : " -> null\n"));
            temp = temp.next;
        }
    }

    public static void main(String[] args) {
        // 1. Create a simple list: 10 -> 20 -> 30 -> null
        Node head = new Node(10);
        head.next = new Node(20);
        head.next.next = new Node(30);

        System.out.print("Before deleting at end: ");
        printList(head);

        // 2. Delete at end (removes 30)
        head = deleteLast(head);

        System.out.print("After deleting at end : ");
        printList(head);
    }
}
