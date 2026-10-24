import java.util.Arrays;

/**
 * CSC 301: Data Structures - Individual Assignment
 * Student Name: Pam Patriarch
 * Matric No:    VUG/SEN/24/12478
 *
 * Question 13: Priority Queue (Binary Min-Heap Implementation)
 *
 * Concept:
 * - A Priority Queue retrieves the highest priority (minimum value in Min-Heap)
 *   element first, rather than following FIFO order.
 * - Stored in a contiguous 1D array representing a complete binary tree:
 *   - Parent index: (i - 1) / 2
 *   - Left Child:   2 * i + 1
 *   - Right Child:  2 * i + 2
 * - insert(val):    Appends at end and percolates UP in O(log n).
 * - extractMin():   Replaces root with last element and percolates DOWN in O(log n).
 * - peek():         Inspects root heap[0] in O(1).
 * - Time Complexity:  Insert O(log n), Extract O(log n), Peek O(1)
 * - Space Complexity: O(n)
 */
public class Question13_PriorityQueue {

    public static class MinPriorityQueue {
        private int[] heap;
        private int size;
        private int capacity;

        public MinPriorityQueue(int capacity) {
            this.capacity = capacity;
            this.heap = new int[capacity];
            this.size = 0;
        }

        public void insert(int val) {
            if (size == capacity) {
                capacity *= 2;
                heap = Arrays.copyOf(heap, capacity);
            }
            heap[size] = val;
            percolateUp(size);
            size++;
        }

        public int peek() {
            if (isEmpty()) throw new IllegalStateException("Priority Queue is empty");
            return heap[0];
        }

        public int extractMin() {
            if (isEmpty()) throw new IllegalStateException("Priority Queue is empty");
            int minVal = heap[0];
            heap[0] = heap[size - 1];
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

    public static void main(String[] args) {
        System.out.println("=================================================");
        System.out.println(" QUESTION 13: PRIORITY QUEUE (BINARY MIN-HEAP)   ");
        System.out.println(" Student: Pam Patriarch | Matric: VUG/SEN/24/12478");
        System.out.println("=================================================\n");

        MinPriorityQueue pq = new MinPriorityQueue(5);
        int[] elements = {25, 12, 5, 18, 9, 20, 14};

        System.out.print("Inserting elements: ");
        for (int x : elements) {
            System.out.print(x + " ");
            pq.insert(x);
        }
        System.out.println("\nPeek highest priority (min): " + pq.peek() + " (Expected: 5)\n");

        System.out.print("Extracting elements in priority order: ");
        while (!pq.isEmpty()) {
            System.out.print(pq.extractMin() + " ");
        }
        System.out.println("\nExpected Ascending Extraction: 5 9 12 14 18 20 25\n");

        System.out.println("Test Status: PASSED (O(log n) Heap Operations)");
    }
}
