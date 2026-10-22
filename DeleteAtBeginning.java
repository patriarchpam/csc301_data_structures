// Simple program to delete the first node (beginning) of a Singly Linked List

public class DeleteAtBeginning {

    // Simple Node definition
    static class Node {
        int data;
        Node next;

        Node(int data) {
            this.data = data;
            this.next = null;
        }
    }

    // Function to delete the first node
    // To delete at the beginning, we simply move head to head.next
    public static Node deleteFirst(Node head) {
        // If the list is empty, there is nothing to delete
        if (head == null) {
            System.out.println("List is already empty.");
            return null;
        }

        // Move head to the next node (old first node is removed)
        head = head.next;
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

        System.out.print("Before deleting: ");
        printList(head);

        // 2. Delete at beginning
        head = deleteFirst(head);

        System.out.print("After deleting : ");
        printList(head);
    }
}
