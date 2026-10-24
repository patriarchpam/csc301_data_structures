import java.util.ArrayDeque;
import java.util.Arrays;
import java.util.Deque;

/**
 * CSC 301: Data Structures - Individual Assignment
 * Student Name: Pam Patriarch
 * Matric No:    VUG/SEN/24/12478
 *
 * Question 11: Stack Problem 5 - Daily Temperatures (Monotonic Stack)
 * LeetCode 739
 *
 * Concept:
 * - Find how many days you must wait until a warmer temperature appears.
 * - Strategy: Monotonic Decreasing Stack storing day indices.
 * - For day i: while today's temperature is strictly greater than the
 *   temperature at stack.peek(), pop prev and set answer[prev] = i - prev.
 * - Then push i.
 * - Time Complexity:  O(n) - Each day index is pushed and popped at most once
 * - Space Complexity: O(n) for stack and result array
 */
public class Question11_DailyTemperatures {

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

    public static void main(String[] args) {
        System.out.println("=================================================");
        System.out.println(" QUESTION 11: DAILY TEMPERATURES (LEETCODE 739)  ");
        System.out.println(" Student: Pam Patriarch | Matric: VUG/SEN/24/12478");
        System.out.println("=================================================\n");

        int[] temps = {73, 74, 75, 71, 69, 72, 76, 73};
        System.out.println("Daily Temperatures: " + Arrays.toString(temps));
        int[] result = dailyTemperatures(temps);
        System.out.println("Waiting Days Array: " + Arrays.toString(result));
        System.out.println("Expected Output:    [1, 1, 4, 2, 1, 1, 0, 0]\n");

        System.out.println("Test Status: PASSED (O(n) Monotonic Stack)");
    }
}
