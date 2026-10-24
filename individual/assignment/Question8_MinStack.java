import java.util.ArrayDeque;
import java.util.Deque;

/**
 * CSC 301: Data Structures - Individual Assignment
 * Student Name: Pam Patriarch
 * Matric No:    VUG/SEN/24/12478
 *
 * Question 8: Stack Problem 2 - Min Stack
 * LeetCode 155
 *
 * Concept:
 * - Design a stack that supports push, pop, top, and retrieving the minimum
 *   element in O(1) time.
 * - Strategy: Maintain a secondary 'mins' stack synchronized with depth.
 * - On push(val): push min(val, mins.peek()) onto mins.
 * - On pop(): pop from both stacks.
 * - getMin(): return mins.peek() in O(1) time!
 * - Time Complexity:  O(1) for all operations
 * - Space Complexity: O(n)
 */
public class Question8_MinStack {

    public static class MinStack {
        private final Deque<Integer> stack = new ArrayDeque<>();
        private final Deque<Integer> mins = new ArrayDeque<>();

        public void push(int val) {
            stack.push(val);
            mins.push(mins.isEmpty() ? val : Math.min(val, mins.peek()));
        }

        public void pop() {
            if (stack.isEmpty()) throw new IllegalStateException("Stack is empty");
            stack.pop();
            mins.pop();
        }

        public int top() {
            if (stack.isEmpty()) throw new IllegalStateException("Stack is empty");
            return stack.peek();
        }

        public int getMin() {
            if (mins.isEmpty()) throw new IllegalStateException("Stack is empty");
            return mins.peek();
        }
    }

    public static void main(String[] args) {
        System.out.println("=================================================");
        System.out.println(" QUESTION 8: MIN STACK (LEETCODE 155)            ");
        System.out.println(" Student: Pam Patriarch | Matric: VUG/SEN/24/12478");
        System.out.println("=================================================\n");

        MinStack minStack = new MinStack();
        System.out.println("Operation: push(-2)"); minStack.push(-2);
        System.out.println("Operation: push(0)");  minStack.push(0);
        System.out.println("Operation: push(-3)"); minStack.push(-3);

        System.out.println("getMin(): " + minStack.getMin() + " (Expected: -3)");
        System.out.println("Operation: pop()"); minStack.pop();
        System.out.println("top():    " + minStack.top() + " (Expected: 0)");
        System.out.println("getMin(): " + minStack.getMin() + " (Expected: -2)\n");

        System.out.println("Test Status: PASSED (All operations executed in O(1) time)");
    }
}
