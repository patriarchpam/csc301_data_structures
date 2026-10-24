import java.util.ArrayDeque;
import java.util.Arrays;
import java.util.Deque;

/**
 * CSC 301: Data Structures - Individual Assignment
 * Student Name: Pam Patriarch
 * Matric No:    VUG/SEN/24/12478
 *
 * File: StackQuestions.java
 * Topic: Five Classic LeetCode Stack Problems
 *   Q1. Valid Parentheses (LeetCode 20)
 *   Q2. Min Stack (LeetCode 155)
 *   Q3. Implement Queue using Stacks (LeetCode 232)
 *   Q4. Evaluate Reverse Polish Notation (LeetCode 150)
 *   Q5. Daily Temperatures / Monotonic Stack (LeetCode 739)
 */
public class StackQuestions {

    // ==========================================
    // Q1. Valid Parentheses (LeetCode 20)
    // Time: O(n), Space: O(n)
    // ==========================================
    public static boolean isValid(String s) {
        Deque<Character> stack = new ArrayDeque<>();
        for (char c : s.toCharArray()) {
            if (c == '(' || c == '[' || c == '{') {
                stack.push(c);
            } else {
                if (stack.isEmpty()) return false;
                char open = stack.pop();
                if ((c == ')' && open != '(')
                        || (c == ']' && open != '[')
                        || (c == '}' && open != '{')) {
                    return false;
                }
            }
        }
        return stack.isEmpty();
    }

    // ==========================================
    // Q2. Min Stack (LeetCode 155)
    // Push, pop, top, getMin in O(1) time
    // Space: O(n) using synchronized minimum tracking
    // ==========================================
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

    // ==========================================
    // Q3. Implement Queue using Stacks (LeetCode 232)
    // Time: Amortized O(1) for push, pop, peek.
    // Space: O(n) across two stacks (in and out).
    // ==========================================
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

    // ==========================================
    // Q4. Evaluate Reverse Polish Notation (LeetCode 150)
    // Time: O(n), Space: O(n)
    // Operands popped: b (right) first, then a (left).
    // Evaluates: a op b
    // ==========================================
    public static int evalRPN(String[] tokens) {
        Deque<Integer> stack = new ArrayDeque<>();
        for (String t : tokens) {
            switch (t) {
                case "+":
                    stack.push(stack.pop() + stack.pop());
                    break;
                case "*":
                    stack.push(stack.pop() * stack.pop());
                    break;
                case "-": {
                    int b = stack.pop();
                    int a = stack.pop();
                    stack.push(a - b);
                    break;
                }
                case "/": {
                    int b = stack.pop();
                    int a = stack.pop();
                    stack.push(a / b);
                    break;
                }
                default:
                    stack.push(Integer.parseInt(t));
            }
        }
        return stack.pop();
    }

    // ==========================================
    // Q5. Daily Temperatures (LeetCode 739)
    // Monotonic Decreasing Stack storing indices.
    // Time: O(n) - each day is pushed & popped at most once.
    // Space: O(n) for stack and result array.
    // ==========================================
    public static int[] dailyTemperatures(int[] temps) {
        int[] answer = new int[temps.length];
        Deque<Integer> stack = new ArrayDeque<>(); // stores indices of temperatures

        for (int i = 0; i < temps.length; i++) {
            while (!stack.isEmpty() && temps[i] > temps[stack.peek()]) {
                int prev = stack.pop();
                answer[prev] = i - prev;
            }
            stack.push(i);
        }
        return answer;
    }

    // ==========================================
    // Comprehensive Verification Suite
    // ==========================================
    public static void main(String[] args) {
        System.out.println("===============================================================");
        System.out.println("      CSC 301 DATA STRUCTURES: STACK QUESTIONS SUITE          ");
        System.out.println("      Student: Pam Patriarch | Matric: VUG/SEN/24/12478       ");
        System.out.println("===============================================================\n");

        // Q1. Valid Parentheses
        System.out.println("--- Q1. Valid Parentheses (LC 20) ---");
        String[] testStrings = {"()[]{}", "([{}])", "(]", "([)]", "{[]}"};
        for (String s : testStrings) {
            System.out.println("isValid(\"" + s + "\") = " + isValid(s));
        }
        System.out.println();

        // Q2. Min Stack
        System.out.println("--- Q2. Min Stack (LC 155) ---");
        MinStack minStack = new MinStack();
        System.out.println("Action: push(-2)"); minStack.push(-2);
        System.out.println("Action: push(0)");  minStack.push(0);
        System.out.println("Action: push(-3)"); minStack.push(-3);
        System.out.println("Current getMin(): " + minStack.getMin() + " (Expected: -3)");
        System.out.println("Action: pop()");     minStack.pop();
        System.out.println("Current top():    " + minStack.top() + " (Expected: 0)");
        System.out.println("Current getMin(): " + minStack.getMin() + " (Expected: -2)\n");

        // Q3. Implement Queue using Stacks
        System.out.println("--- Q3. Implement Queue using Stacks (LC 232) ---");
        MyQueue queue = new MyQueue();
        System.out.println("Action: push(1)"); queue.push(1);
        System.out.println("Action: push(2)"); queue.push(2);
        System.out.println("Action: push(3)"); queue.push(3);
        System.out.println("peek():  " + queue.peek() + " (Expected: 1)");
        System.out.println("pop():   " + queue.pop() + " (Expected: 1)");
        System.out.println("peek():  " + queue.peek() + " (Expected: 2)");
        System.out.println("empty(): " + queue.empty() + " (Expected: false)\n");

        // Q4. Evaluate Reverse Polish Notation
        System.out.println("--- Q4. Evaluate Reverse Polish Notation (LC 150) ---");
        String[] rpn1 = {"2", "1", "+", "3", "*"}; // (2 + 1) * 3 = 9
        String[] rpn2 = {"4", "13", "5", "/", "+"}; // 4 + (13 / 5) = 6
        String[] rpn3 = {"10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"}; // 22
        System.out.println("RPN [\"2\",\"1\",\"+\",\"3\",\"*\"] = " + evalRPN(rpn1) + " (Expected: 9)");
        System.out.println("RPN [\"4\",\"13\",\"5\",\"/\",\"+\"] = " + evalRPN(rpn2) + " (Expected: 6)");
        System.out.println("RPN Complex expression = " + evalRPN(rpn3) + " (Expected: 22)\n");

        // Q5. Daily Temperatures
        System.out.println("--- Q5. Daily Temperatures (LC 739) ---");
        int[] temps1 = {73, 74, 75, 71, 69, 72, 76, 73};
        int[] res1 = dailyTemperatures(temps1);
        System.out.println("Temperatures: " + Arrays.toString(temps1));
        System.out.println("Wait Days:    " + Arrays.toString(res1));
        System.out.println("Expected:     [1, 1, 4, 2, 1, 1, 0, 0]\n");

        System.out.println("===============================================================");
        System.out.println("      ALL STACK TEST CASES EXECUTED SUCCESSFULLY!             ");
        System.out.println("===============================================================");
    }
}
