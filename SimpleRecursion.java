public class SimpleRecursion {
    // Recursively sum the first n natural numbers (1..n)
    static int sum(int n) {
        return n == 0 ? 0 : n + sum(n - 1);
    }
    public static void main(String[] args) {
        // Sum of first 10 numbers
        System.out.println(sum(10));
    }
}
