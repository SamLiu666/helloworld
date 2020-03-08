/*It can be used for any type of data.
The space required is always proportional to the size of the collection.
The time per operation is always independent of the size of the collection.
 */
public class StackLinkedList<Item>{
    //栈用链表方式实现，FILO
    private Node first;   //栈顶
    private int N;        //数量

    private class Node{
        Item item;
        Node next;
    }

    public boolean isEmpty(){
        return first == null;
    }

    public int size(){
        return N;
    }

    public void push(Item item){
        Node oldfirst = first;
        first = new Node();
        first.item = item;
        first.next = oldfirst;
        N++;
    }

    public Item pop(){
        Item item = first.item;
        first.next = first;
        N--;
        return item;
    }



}