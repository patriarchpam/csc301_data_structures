import java.util.Arrays;

public class ThreeSumN2 {
    public static void main(String[] args) {
        int a[] = {2, 6, 7, 3, 10};
        Arrays.sort(a);

        for (int b = 0; b < a.length - 2; b++) {
            int c = b + 1;
            int d = a.length - 1;

            while (c < d) {
                if (a[b] + a[c] + a[d] == 12) {
                    System.out.println(a[b] + ", " + a[c] + ", " + a[d]);
                    return;
                } else if (a[b] + a[c] + a[d] < 12) {
                    c++;
                } else {
                    d--;
                }
            }
        }
    }
}

