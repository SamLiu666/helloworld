public class Merge {
    // 判断v，u 的大小，返回 v<u 的判断结果，顺序:第一个<第二个为真
    private static boolean less(Comparable v, Comparable w) {
        return v.compareTo(w) < 0;
    }

    // 交换数组中位置为 i,j 的值，位置一i 与 位置二 j 交换
    private static void exch(Comparable[] a, int i, int j) {
        Comparable temp = a[i];
        a[i] = a[j];
        a[j] = temp;
    }

    // 检测数组是否已排序
    private static boolean isSorted(Comparable[] a) {
        for (int i = 1; i < a.length; i++) {
            if (less(a[i], a[i - 1])) return false;
        }
        return true;
    }

    // 输出数组
    private static void printA(Comparable[] a) {
        for (int i = 0; i < a.length; i++)
            System.out.print(a[i] + " ");
        System.out.println('\n');
    }

    private static Comparable[] aux; // auxiliary array for merges

    //排序归并数组
    public static void merge(Comparable[] a, int lo, int mid, int hi)
    { // Merge a[lo..mid] with a[mid+1..hi].
        int i = lo, j = mid+1;
        for (int k = lo; k <= hi; k++) // Copy a[lo..hi] to aux[lo..hi].
            aux[k] = a[k];
        for (int k = lo; k <= hi; k++) // Merge back to a[lo..hi].
            if (i > mid) a[k] = aux[j++];       // 右边还有剩余
            else if (j > hi ) a[k] = aux[i++];  // 左边还有剩余，去掉边界问题
            else if (less(aux[j], aux[i])) a[k] = aux[j++];
            else a[k] = aux[i++];
/*        printA(a);
        printA(aux);*/
    }

    //Top-down MergeSort
    public static void sort(Comparable[] a)
    {
        aux = new Comparable[a.length]; // Allocate space just once.
        sort(a, 0, a.length - 1);
        printA(a);
    }
    //分治方法实现归并排序，从上至下
    private static void sort(Comparable[] a, int lo, int hi)
    { // Sort a[lo..hi].
        if (hi <= lo) return;
        int mid = lo + (hi - lo)/2;
        sort(a, lo, mid); // Sort left half.
        sort(a, mid+1, hi); // Sort right half.
        merge(a, lo, mid, hi); // Merge results (code on page 271).

    }

    //Bottom-up merge sort
    public static void sort_down(Comparable[] a)
    { // Do lg N passes of pairwise merges.
        int N = a.length;
        aux = new Comparable[N];
        for (int sz = 1; sz < N; sz = sz+sz) // sz: subarray size
            for (int lo = 0; lo < N-sz; lo += sz+sz) // lo: subarray index
                merge(a, lo, lo+sz-1, Math.min(lo+sz+sz-1, N-1));
        printA(a);
    }

    public static void main(String[] args){
        Comparable[] a = {2,4,5,3,1,11,7};
        Comparable[] s = {'a', 'm', 'z', 'c', 'b'};
        printA(a); printA(s);
        Merge.sort_down(a);
        Merge.sort(s);

    }
}