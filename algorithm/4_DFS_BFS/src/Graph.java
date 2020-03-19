import java.util.Iterator;

public class Graph {

    private final int V;    //vertices
    private int E;          // edges
    private Bag<Integer>[] adj; //adjacency lists

    public Graph(int V) {
        this.V = V; this.E = 0;
        adj = (Bag<Integer>[]) new Bag[V];  //create array of lists
        for (int v=0; v<V; v++){
            adj[v] = new Bag<Integer>();
        }
    }

    public class Bag<Item> implements Iterable<Item> {
        private Node first;

        private class Node{
            Item item;
            Node next;
        }

        public void add(Item item){
            Node oldfirst = first;
            first = new Node();
            first.item = item;
            first.next = oldfirst;
        }

        public Iterator<Item> iterator() {
            return new ListIterator();
        }

        private class ListIterator implements Iterator<Item>{
            private Node current = first;
            @Override
            public boolean hasNext() {
                return current != null;
            }

            public void remove(){}

            @Override
            public Item next() {
                Item item = current.item;
                current = current.next;
                return item;
            }
        }
    }

    public Graph(In in)
    {
        this(in.readInt()); // Read V and construct this graph.
        int E = in.readInt(); // Read E.
        for (int i = 0; i < E; i++)
        { // Add an edge.
            int v = in.readInt(); // Read a vertex,
            int w = in.readInt(); // read another vertex,
            addEdge(v, w); // and add edge connecting them.
        }
    }
    
    public int V()  {return V;}
    public int E()  {return E;}

    public void addEdge(int v, int w){
        adj[v].add(w);
        adj[w].add(v);
        E++;
    }

    public Iterator<Integer> adj(int v){
        return (Iterator<Integer>) adj[v];
    }

    public void show(){
        for (int i=0; i<V; i++){
            System.out.print(adj[i]);
        }
    }

    public static void main(String[] args){
        Graph graph_0 = new Graph(5);
        graph_0.addEdge(0,3);
        graph_0.addEdge(0,4);
        graph_0.addEdge(1,2);
//        System.out.println(graph_0);
        graph_0.show();
    }
}
