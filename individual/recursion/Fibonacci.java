public class Fibonacci {

    public static int fib(int n) {
        // Base cases: first two values of Fibonacci are 0 and 1
        if (n == 0) {
            return 0;
        }
        if (n == 1) {
            return 1;
        }

        // Recursive call: sum of the previous two values
        return fib(n - 1) + fib(n - 2);
    }

    public static void main(String[] args) {
        System.out.println("First value fib(0): " + fib(10));
        System.out.println("Second value fib(1): " + fib(11));
        System.out.println("6th value fib(5): " + fib(15));
    }
}
