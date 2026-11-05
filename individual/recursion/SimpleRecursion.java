public class SimpleRecursion {

    public static void findValue(int n) {
        if (n == 5) {
            System.out.println(n);
            return;
        }
        findValue(n - 1);
    }

    public static void main(String[] args) {
        findValue(10);
    }
}
