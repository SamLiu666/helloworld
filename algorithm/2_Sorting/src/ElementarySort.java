
public class ElementarySort {

    // 判断v，u 的大小，返回 v<u 的判断结果，顺序:第一个<第二个为真
    private static boolean less(Comparable v, Comparable w){
        return v.compareTo(w)<0;
    }

    // 交换数组中位置为 i,j 的值，位置一i 与 位置二 j 交换
    private static void exch(Comparable[] a, int i, int j){
        Comparable temp = a[i]; a[i] = a[j]; a[j] = temp;
    }

    private static boolean isSorted(Comparable[] a){
        // 检测数组是否已排序
        for (int i=1; i<a.length; i++){
            if (less(a[i], a[i-1])) return false;
        }
        return true;
    }

    // 输出数组
    private static void printA(Comparable[] a){
        for (int i=0; i<a.length; i++)
            System.out.print(a[i] + " ");
        System.out.println('\n');
    }

    //1.选择排序，升序，与输入无关，算法复杂度O(N^2)
    public static void SelectionSort(Comparable[] a){
        int N = a.length;
        for (int i=0; i<N;i++){
            int cur_min = i;   //当前排序指针位置
            for (int j = i+1; j<N; j++){
                if (less(a[j], a[cur_min]))  cur_min = j;
            }
            exch(a, i, cur_min);
        }
        printA(a);
    }

    //2.插入排序，比选择排序时间少一半，线性交换次数=逆序对个数，
    public static int InsertionSort(Comparable[] a){
        int count = 0; //记录逆序对个数，交换次数
        for (int i=0; i<a.length; i++){
            for (int j=i; j>0 ;j--)
                if (less(a[j], a[j-1]))
                {exch(a, j, j-1); count += 1;}
        }
        printA(a);
        return count;
    }

    //3.希尔排序ShellSort，插入排序变形为 3*n个 距离移动
    public static void ShellSort(Comparable[] a){
        int N = a.length; int h = 1;
        while (h < N/3)   h = 3*h+1;  //实验得3个距离较好
        while ( h>=1 ){
            for (int i=h; i<N; i++){
                for (int j=i; j>=h && less(a[j], a[j-h]); j-=h)
                    exch(a, j, j-h);
            }
            h = h/3;
        }
        printA(a);
    }

    // 主程序运行
    public static void main(String[] args){
        Comparable[] a = {2,4,5,3,1,11,7};
        Comparable[] s = {'a', 'm', 'z', 'c', 'b'};
        printA(a);
        //SelectionSort(s);     //选择排序
        int count = InsertionSort(a);   //插入排序，并记录交换次数
        System.out.println("交换次数： " + count);
        ShellSort(s);
    }
}
