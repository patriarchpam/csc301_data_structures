import java.util.Arrays;

/**
 * CSC 301: Data Structures - Individual Assignment
 * Student Name: Pam Patriarch
 * Matric No:    VUG/SEN/24/12478
 *
 * File: QueueQuestions.java
 * Topics:
 *   1. Circular Queue (Ring Buffer using Array and Modulo Arithmetic)
 *   2. Priority Queue (Binary Min-Heap Implementation)
 */
public class QueueQuestions {

    // ==========================================
    // 1. Circular Queue Implementation (Ring Buffer)
    // Avoids array element shifting; uses modulo arithmetic.
    // Enqueue, Dequeue, Front, Rear all execute in O(1) time.
    // ==========================================
    public static class CircularQueue {
        private final int[] data;
        private int head; // points to the front element
        private int tail; // points to the last inserted element
        private int size; // number of elements currently stored
        private final int capacity;

        public CircularQueue(int k) {
            this.capacity = k;
            this.data = new int[k];
            this.head = 0;
            this.tail = -1;
            this.size = 0;
        }

        // Enqueue: inserts an element at the rear. Returns true if successful.
        // Formula: tail = (tail + 1) % capacity
        public boolean enQueue(int value) {
            if (isFull()) return false;
            tail = (tail + 1) % capacity;
            data[tail] = value;
            size++;
            return true;
        }

        // Dequeue: deletes an element from the front. Returns true if successful.
        // Formula: head = (head + 1) % capacity
        public boolean deQueue() {
            if (isEmpty()) return false;
            head = (head + 1) % capacity;
            size--;
            return true;
        }

        // Get front item
        public int front() {
            if (isEmpty()) return -1;
            return data[head];
        }

        // Get rear item
        public int rear() {
            if (isEmpty()) return -1;
            return data[tail];
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

    // ==========================================
    // 2. Priority Queue Implementation (Binary Min-Heap)
    // Elements are served in order of priority (minimum value first).
    // Insert: O(log n)
    // ExtractMin: O(log n)
    // PeekMin: O(1)
    // Array indexing:
    //   Parent = (i - 1) / 2
    //   Left Child = 2 * i + 1
    //   Right Child = 2 * i + 2
    // ==========================================
    public static class MinPriorityQueue {
        private int[] heap;
        private int size;
        private int capacity;

        public MinPriorityQueue(int capacity) {
            this.capacity = capacity;
            this.heap = new int[capacity];
            this.size = 0;
        }

        // Insert new element into priority queue
        public void insert(int val) {
            if (size == capacity) {
                // Resize array
                capacity *= 2;
                heap = Arrays.copyOf(heap, capacity);
            }
            heap[size] = val;
            percolateUp(size);
            size++;
        }

        // Peek highest priority element (minimum) in O(1)
        public int peek() {
            if (isEmpty()) throw new IllegalStateException("Priority Queue is empty");
            return heap[0];
        }

        // Extract and remove highest priority element in O(log n)
        public int extractMin() {
            if (isEmpty()) throw new IllegalStateException("Priority Queue is empty");
            int minVal = heap[0];
            heap[0] = heap[size - 1]; // Move last element to root
            size--;
            if (size > 0) {
                percolateDown(0);
            }
            return minVal;
        }

        public boolean isEmpty() {
            return size == 0;
        }

        public int size() {
            return size;
        }

        // Helper: Percolate (bubble) up to restore min-heap invariant
        private void percolateUp(int index) {
            while (index > 0) {
                int parent = (index - 1) / 2;
                if (heap[index] < heap[parent]) {
                    swap(index, parent);
                    index = parent;
                } else {
                    break;
                }
            }
        }

        // Helper: Percolate (sift) down to restore min-heap invariant
        private void percolateDown(int index) {
            while (2 * index + 1 < size) {
                int left = 2 * index + 1;
                int right = 2 * index + 2;
                int smallest = left;

                if (right < size && heap[right] < heap[left]) {
                    smallest = right;
                }

                if (heap[smallest] < heap[index]) {
                    swap(index, smallest);
                    index = smallest;
                } else {
                    break;
                }
            }
        }

        private void swap(int i, int j) {
            int temp = heap[i];
            heap[i] = heap[j];
            heap[j] = temp;
        }
    }

    // ==========================================
    // Interactive Test Runner
    // ==========================================
    public static void main(String[] args) {
        System.out.println("===============================================================");
        System.out.println("       CSC 301 DATA STRUCTURES: QUEUE QUESTIONS SUITE         ");
        System.out.println("       Student: Pam Patriarch | Matric: VUG/SEN/24/12478       ");
        System.out.println("===============================================================\n");

        // 1. Circular Queue Test
        System.out.println("--- 1. Circular Queue Demonstration (Capacity = 3) ---");
        CircularQueue cq = new CircularQueue(3);
        System.out.println("enQueue(10): " + cq.enQueue(10));
        System.out.println("enQueue(20): " + cq.enQueue(20));
        System.out.println("enQueue(30): " + cq.enQueue(30));
        System.out.println("enQueue(40) on full queue: " + cq.enQueue(40) + " (Expected: false)");
        System.out.println("front(): " + cq.front() + " (Expected: 10)");
        System.out.println("rear():  " + cq.rear() + " (Expected: 30)");
        System.out.println("deQueue(): " + cq.deQueue() + " (Front moves clockwise)");
        System.out.println("enQueue(40) into freed slot: " + cq.enQueue(40) + " (Expected: true)");
        System.out.println("front(): " + cq.front() + " (Expected: 20)");
        System.out.println("rear():  " + cq.rear() + " (Expected: 40)\n");

        // 2. Priority Queue Test
        System.out.println("--- 2. Priority Queue Demonstration (Min-Heap) ---");
        MinPriorityQueue pq = new MinPriorityQueue(5);
        int[] insertValues = {25, 12, 5, 18, 9, 20, 14};
        System.out.print("Inserting values: ");
        for (int v : insertValues) {
            System.out.print(v + " ");
            pq.insert(v);
        }
        System.out.println("\nPeek highest priority (min): " + pq.peek() + " (Expected: 5)");

        System.out.print("Extracting elements in priority order: ");
        while (!pq.isEmpty()) {
            System.out.print(pq.extractMin() + " ");
        }
        System.out.println("\n(Elements extracted in ascending priority: 5, 9, 12, 14, 18, 20, 25)\n");

        System.out.println("===============================================================");
        System.out.println("         ALL QUEUE DEMONSTRATIONS EXECUTED CLEANLY!            ");
        System.out.println("===============================================================");
    }
}
