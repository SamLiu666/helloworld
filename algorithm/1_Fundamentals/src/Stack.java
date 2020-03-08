import java.util.Iterator;

public class Stack {
    // 固定长度的栈，用于字符串
    public static class FixedCapacityStackOfStrings
    {
        private String[] a; // stack entries
        private int N; // size
        public FixedCapacityStackOfStrings(int cap)
        { a = new String[cap]; }
        public boolean isEmpty() { return N == 0; }
        public int size() { return N; }
        public void push(String item)
        { a[N++] = item; }
        public String pop()
        { return a[--N]; }
    }

    // 固定长度的通用栈
    public static class FixedCapacityStack<Item>
    {
        private Item[] a; // stack entries
        private int N; // size
        public FixedCapacityStack(int cap)
        { a = (Item[]) new Object[cap]; }
        public boolean isEmpty() { return N == 0; }
        public int size() { return N; }
        public void push(Item item)
        { a[N++] = item; }
        public Item pop()
        { return a[--N]; }
    }


    public static void main(String[] args)
    {
        FixedCapacityStackOfStrings s = new FixedCapacityStackOfStrings(100);
        //推入 to  be not
        s.push("to");
        s.push(" be ");
        s.push("not!");
        System.out.println(s.pop() +" (" + s.size() + " left on stack) " + s.pop());

        FixedCapacityStack f = new FixedCapacityStack(5);
        boolean di = f.isEmpty();
        f.push("toto");
        f.push(5);
        System.out.println(di + " "+ f.pop() + " " + f.pop());
    }
}

//迭代+栈法实现队列问题
class ResizingArrayStack<Item> implements Iterable<Item>
{
    private Item[] a = (Item[]) new Object[1]; // stack items
    private int N = 0; // number of items
    public boolean isEmpty() { return N == 0; }
    public int size() { return N; }
    private void resize(int max)
    { // Move stack to a new array of size max.
        Item[] temp = (Item[]) new Object[max];
        for (int i = 0; i < N; i++)
            temp[i] = a[i];
        a = temp;
    }
    public void push(Item item)
    { // Add item to top of stack.
        if (N == a.length) resize(2*a.length);
        a[N++] = item;
    }
    public Item pop()
    { // Remove item from top of stack.
        Item item = a[--N];
        a[N] = null; // Avoid loitering (see text).
        if (N > 0 && N == a.length/4) resize(a.length/2);
        return item;
    }
    public Iterator<Item> iterator()
    { return new ReverseArrayIterator(); }
    private class ReverseArrayIterator implements Iterator<Item>
    { // Support LIFO iteration.
        private int i = N;
        public boolean hasNext() { return i > 0; }
        public Item next() { return a[--i]; }
        public void remove() { }
    }
}