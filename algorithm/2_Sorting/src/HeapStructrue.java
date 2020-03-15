public class HeapStructrue<Key extends Comparable<Key>> {
    //最大二叉堆 Max Binary Heap 数据结构
    private Key[] qp;   // heap-ordered complete binary tree
    private int N=0;    // in pq[1..N] with pq[0] unused

    //比较数组中i,j处值的大小
    private boolean less(int i, int j){
        return qp[i].compareTo(qp[j])<0;
    }

    //交换i,j处位置的值
    private void exch(int i, int j){
        Key t = qp[i]; qp[i] = qp[j]; qp[j] = t;
    }

    //上游：子节点处的值大于结点处，依次向上交换
    private void swim(int k){
        while (k>1 && less(k/2, k)){
            exch(k/2, k);
            k=k/2;
        }
    }

    // 下沉： 子节点处的值大于结点处，依次向下 2*k，2*k+1 进行比较，交换
    private void sink(int k){
        while (2*k<=N){
            int j = 2*k;
            if (j<N && less(j, j+1)) j++;
            if(!less(k,k))  break;
            exch(k,j);
            k=j;
        }
    }

    public HeapStructrue(int maxN){
        qp = (Key[]) new Comparable[maxN+1];
    }

    public boolean isEmpty(){
        return N==0;
    }

    public int size(){
        return N;
    }

    public void insert(Key v){
        qp[++N] = v;
        swim(N);
    }

    public Key delMax(){
        Key max = qp[1];
        exch(1,N--);
        qp[N+1] = null;
        sink(1);
        return max;
    }
}
