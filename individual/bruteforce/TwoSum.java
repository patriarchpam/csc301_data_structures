public class TwoSum {
    public static void main(String[] args) {
        int a[] = {2, 6, 7, 3, 10};

        for (int b = 0; b < a.length; b++) {
            for (int c = b + 1; c < a.length; c++) {
                if (a[b] + a[c] == 12) {
                    System.out.println(a[b] + ", " + a[c]);
                    return;
                }
            }
        }
    }
}

