import java.util.Iterator;
import java.util.NoSuchElementException;

public class StackLinkedList<Item>  {
    private Node<Item> first;
    private int n;

    private static class Node<Item>{
        private Item item;
        private Node<Item> next;
    }

}
