public class Quick {

    private static boolean less(Comparable v, Comparable w) {
        return v.compareTo(w) < 0;
    }
    private static void printA(Comparable[] a) {
        for (int i = 0; i < a.length; i++)
            System.out.print(a[i] + " ");
        System.out.println('\n');
    }
    private static void exch(Comparable[] a, int i, int j) {
        Comparable temp = a[i];
        a[i] = a[j];
        a[j] = temp;
    }


    public static void sort(Comparable[] a) {
        sort(a, 0, a.length - 1); // 递归调用自身
        printA(a);
    }

    private static void sort(Comparable[] a, int lo, int hi) {
        if (hi <= lo) return;
        // 快速排序，算法复杂度 2nlgn
        int j = partition(a, lo, hi); // 以j 左侧的元素都小于 a[j]，j 右侧的元素都大于 a[j]
        // 从顶往下切分数组，完成排序
        sort(a, lo, j - 1);
        sort(a, j + 1, hi);
    }

    private static int partition(Comparable[] a, int lo, int hi) {
        // 实现 j 位置出，左边都小于a[j]，右边都大于a[j]
        int i = lo, j = hi + 1;
        Comparable v = a[lo]; //初始化一个被比较值v，默认为第一个元素
        while (true) {
            //一个字串不动，到达边界了，完成交叉，结束循环，交换位置
            while (less(a[++i], v)) if (i == hi) break;
            while (less(v, a[--j])) if (j == lo) break;
            if (i >= j) break;   // 若i,j交叉，则结束循环
            // 交换a[i],a[j] 的位置
            exch(a, i, j);
        }
        exch(a, lo, j);
        return j;
    }

    //quick 3-way partitioning
    private static void quick3sort(Comparable[] a, int lo, int hi){
        if (hi <= lo) return;
        int lt = lo, i = lo+1, gt = hi;
        Comparable v = a[lo];
        while (i <= gt)
        {
            int cmp = a[i].compareTo(v);
            if (cmp < 0) exch(a, lt++, i++);
            else if (cmp > 0) exch(a, i, gt--);
            else i++;
        } // Now a[lo..lt-1] < v = a[lt..gt] < a[gt+1..hi].
        sort(a, lo, lt - 1);
        sort(a, gt + 1, hi);
    }

    public static void main(String[] args) {
        Comparable[] a = {2, 4, 5, 3, 1, 11, 7};
        Comparable[] s = {'a', 'm', 'z', 'c', 'b'};
        printA(a);printA(s);
        sort(a);
        quick3sort(s,0,s.length-1);
        printA(s);
    }
}
