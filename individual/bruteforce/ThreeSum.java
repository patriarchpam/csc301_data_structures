public class ThreeSum {
    public static void main(String[] args) {
        int a[] = {2, 6, 7, 3, 10};

        for (int b = 0; b < a.length; b++) {
            for (int c = b + 1; c < a.length; c++) {
                for (int d = c + 1; d < a.length; d++) {
                    if (a[b] + a[c] + a[d] == 15) {
                        System.out.println(a[b] + ", " + a[c] + ", " + a[d]);
                        return;
                    }
                }
            }
        }
    }
}

