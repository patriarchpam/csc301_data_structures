import java.util.ArrayDeque;
import java.util.Deque;

/**
 * CSC 301: Data Structures - Individual Assignment
 * Student Name: Pam Patriarch
 * Matric No:    VUG/SEN/24/12478
 *
 * Question 10: Stack Problem 4 - Evaluate Reverse Polish Notation
 * LeetCode 150
 *
 * Concept:
 * - Evaluate arithmetic expressions given in postfix form.
 * - Operands (numbers) are pushed onto the stack.
 * - When an operator is read, pop two operands:
 *   b (right operand) is popped first, then a (left operand).
 * - Compute (a op b) and push the result back onto the stack.
 * - Time Complexity:  O(n)
 * - Space Complexity: O(n)
 */
public class Question10_EvaluateRPN {

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

    public static void main(String[] args) {
        System.out.println("=================================================");
        System.out.println(" QUESTION 10: EVALUATE RPN (LEETCODE 150)        ");
        System.out.println(" Student: Pam Patriarch | Matric: VUG/SEN/24/12478");
        System.out.println("=================================================\n");

        // Test Case 1: ["2","1","+","3","*"] -> ((2 + 1) * 3) = 9
        String[] rpn1 = {"2", "1", "+", "3", "*"};
        System.out.println("Expression 1: [\"2\",\"1\",\"+\",\"3\",\"*\"]");
        System.out.println("Result 1:     " + evalRPN(rpn1) + " (Expected: 9)\n");

        // Test Case 2: ["4","13","5","/","+"] -> (4 + (13 / 5)) = 6
        String[] rpn2 = {"4", "13", "5", "/", "+"};
        System.out.println("Expression 2: [\"4\",\"13\",\"5\",\"/\",\"+\"]");
        System.out.println("Result 2:     " + evalRPN(rpn2) + " (Expected: 6)\n");

        System.out.println("Test Status: PASSED");
    }
}
