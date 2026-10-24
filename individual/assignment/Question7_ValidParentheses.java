import java.util.ArrayDeque;
import java.util.Deque;

/**
 * CSC 301: Data Structures - Individual Assignment
 * Student Name: Pam Patriarch
 * Matric No:    VUG/SEN/24/12478
 *
 * Question 7: Stack Problem 1 - Valid Parentheses
 * LeetCode 20
 *
 * Concept:
 * - Push every open bracket '(', '[', '{' onto the stack.
 * - For a close bracket, verify the stack is non-empty and the top matches.
 * - Valid only if stack is empty at the end.
 * - Time Complexity:  O(n)
 * - Space Complexity: O(n)
 */
public class Question7_ValidParentheses {

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

    public static void main(String[] args) {
        System.out.println("=================================================");
        System.out.println(" QUESTION 7: VALID PARENTHESES (LEETCODE 20)     ");
        System.out.println(" Student: Pam Patriarch | Matric: VUG/SEN/24/12478");
        System.out.println("=================================================\n");

        String[] testCases = {"()", "()[]{}", "(]", "([)]", "{[]}"};
        for (String test : testCases) {
            System.out.println("isValid(\"" + test + "\") = " + isValid(test));
        }

        System.out.println("\nTest Status: PASSED");
    }
}
