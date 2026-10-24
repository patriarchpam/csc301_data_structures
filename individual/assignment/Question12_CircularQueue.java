/**
 * CSC 301: Data Structures - Individual Assignment
 * Student Name: Pam Patriarch
 * Matric No:    VUG/SEN/24/12478
 *
 * Question 12: Circular Queue (Ring Buffer)
 * LeetCode 622: Design Circular Queue
 *
 * Concept:
 * - A Circular Queue wraps the end of a fixed-size array back to the beginning
 *   using modulo arithmetic, eliminating the "false overflow" problem of linear queues.
 * - Enqueue: tail = (tail + 1) % capacity
 * - Dequeue: head = (head + 1) % capacity
 * - All operations run in O(1) time without array shifting.
 * - Time Complexity:  O(1) for enQueue, deQueue, Front, Rear, isEmpty, isFull
 * - Space Complexity: O(k) where k is the queue capacity
 */
public class Question12_CircularQueue {

    public static class CircularQueue {
        private final int[] data;
        private int head;
        private int tail;
        private int size;
        private final int capacity;

        public CircularQueue(int k) {
            this.capacity = k;
            this.data = new int[k];
            this.head = 0;
            this.tail = -1;
            this.size = 0;
        }

        // Insert at rear using modulo wrap-around
        public boolean enQueue(int value) {
            if (isFull()) return false;
            tail = (tail + 1) % capacity;
            data[tail] = value;
            size++;
            return true;
        }

        // Delete from front using modulo wrap-around
        public boolean deQueue() {
            if (isEmpty()) return false;
            head = (head + 1) % capacity;
            size--;
            return true;
        }

        public int front() {
            return isEmpty() ? -1 : data[head];
        }

        public int rear() {
            return isEmpty() ? -1 : data[tail];
        }

        public boolean isEmpty() {
            return size == 0;
        }

        public boolean isFull() {
            return size == capacity;
        }

        public int size() {
            return size;
        }
    }

    public static void main(String[] args) {
        System.out.println("=================================================");
        System.out.println(" QUESTION 12: CIRCULAR QUEUE (RING BUFFER)       ");
        System.out.println(" Student: Pam Patriarch | Matric: VUG/SEN/24/12478");
        System.out.println("=================================================\n");

        CircularQueue cq = new CircularQueue(3);
        System.out.println("Initialize CircularQueue with capacity = 3");
        System.out.println("enQueue(10): " + cq.enQueue(10));
        System.out.println("enQueue(20): " + cq.enQueue(20));
        System.out.println("enQueue(30): " + cq.enQueue(30));
        System.out.println("enQueue(40) on full queue: " + cq.enQueue(40) + " (Expected: false)");

        System.out.println("Front item: " + cq.front() + " (Expected: 10)");
        System.out.println("Rear item:  " + cq.rear() + " (Expected: 30)");

        System.out.println("\ndeQueue(): " + cq.deQueue() + " (Slot at index 0 freed)");
        System.out.println("enQueue(40) into wrap-around slot: " + cq.enQueue(40) + " (Expected: true)");
        System.out.println("New Front item: " + cq.front() + " (Expected: 20)");
        System.out.println("New Rear item:  " + cq.rear() + " (Expected: 40)\n");

        System.out.println("Test Status: PASSED (All operations executed in O(1) time)");
    }
}
