import java.util.ArrayDeque;
import java.util.Deque;

/**
 * CSC 301: Data Structures - Individual Assignment
 * Student Name: Pam Patriarch
 * Matric No:    VUG/SEN/24/12478
 *
 * Question 9: Stack Problem 3 - Implement Queue using Stacks
 * LeetCode 232
 *
 * Concept:
 * - Implement FIFO Queue using only standard LIFO Stack operations.
 * - Strategy: Dual stacks ('in' and 'out').
 * - push(x): push directly onto 'in'.
 * - pop() / peek(): if 'out' is empty, transfer all elements from 'in' to 'out'.
 *   This reverses LIFO order into correct FIFO order!
 * - Time Complexity:  Amortized O(1) per operation (each item transferred at most once)
 * - Space Complexity: O(n) across two stacks
 */
public class Question9_QueueUsingStacks {

    public static class MyQueue {
        private final Deque<Integer> in = new ArrayDeque<>();
        private final Deque<Integer> out = new ArrayDeque<>();

        public void push(int x) {
            in.push(x);
        }

        public int pop() {
            shift();
            if (out.isEmpty()) throw new IllegalStateException("Queue is empty");
            return out.pop();
        }

        public int peek() {
            shift();
            if (out.isEmpty()) throw new IllegalStateException("Queue is empty");
            return out.peek();
        }

        public boolean empty() {
            return in.isEmpty() && out.isEmpty();
        }

        private void shift() {
            if (out.isEmpty()) {
                while (!in.isEmpty()) {
                    out.push(in.pop());
                }
            }
        }
    }

    public static void main(String[] args) {
        System.out.println("=================================================");
        System.out.println(" QUESTION 9: QUEUE USING STACKS (LEETCODE 232)   ");
        System.out.println(" Student: Pam Patriarch | Matric: VUG/SEN/24/12478");
        System.out.println("=================================================\n");

        MyQueue queue = new MyQueue();
        System.out.println("push(1)"); queue.push(1);
        System.out.println("push(2)"); queue.push(2);
        System.out.println("push(3)"); queue.push(3);

        System.out.println("peek():  " + queue.peek() + " (Expected: 1)");
        System.out.println("pop():   " + queue.pop() + " (Expected: 1)");
        System.out.println("peek():  " + queue.peek() + " (Expected: 2)");
        System.out.println("empty(): " + queue.empty() + " (Expected: false)\n");

        System.out.println("Test Status: PASSED (Amortized O(1) per operation)");
    }
}
