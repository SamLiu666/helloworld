import java.lang.reflect.Array;
import java.util.*;

public class Set_List_Hashmap {
    // 8.1、普通哈希集合，树集合，链表哈希集合
    public void Set_(){
        Set<Integer> t = new HashSet<Integer>();    // 集合没有重复元素，哈希结构
        // t = [-2, 100, 5, 56, 12, 30]
        t.add(100); t.add(12); t.add(-2);
        t.add(56); t.add(5); t.add(30); t.add(-9);   // t.add()添加操作，无序集合
        boolean co = t.contains(3);                 // 判断集合内是否有该元素
        t.remove(-9);
        System.out.println(t + "  普通集合  " + co + " 集合大小 " + t.size());

        // 以树的结构构造集合，有序;
        Set<Integer> tree_set = new TreeSet<>(t);
        System.out.println(tree_set + "     树集合是有序的");

        //链表哈希集合表
        Set<Integer> linkSet = new LinkedHashSet<>(t);
        System.out.println("链表集合：  " + linkSet);
    }

    // 8.2、普通整数列表， 链表列表
    public void List_(){
        // 8.2 列表，原集合 t= [-2, 100, 5, 56, 12, 30]
        Set<Integer> t = new HashSet<Integer>();    // 集合没有重复元素，哈希结构
        // t = [-2, 100, 5, 56, 12, 30]
        t.add(100); t.add(12); t.add(-2);
        t.add(56); t.add(5); t.add(30); t.add(-9);   // t.add()添加操作，无序集合
        boolean co = t.contains(3);                 // 判断集合内是否有该元素

        // 集合转化为列表
        ArrayList<Integer> list_t = new ArrayList<>(t);
        list_t.add(6);  list_t.get(6);  //获取元素索引
        list_t.set(2, 60);  // 改变指定位置处 元素
        // 获取 1~4 处字串, list.subList(i, j)
        System.out.println(list_t + " 数组列表 " + list_t.subList(1,4));

        // 链表结构
        LinkedList<Integer> linkList = new LinkedList<Integer>(list_t);
        System.out.println(" 链表列表  " + linkList);

    }

    // 9、 Map， key-value 键-值对的结构，类似python中的字典
    // 普通哈希表，树哈希表，链表哈希表
    public void Map_(){
        // 9.1 哈希表，无序，唯一键-值对
        Map m = new HashMap();
        // 输入键 m.put， 可以是不同类型
        m.put("Tom", 6); m.put(11, 1111);
        m.put("Peter", 23); m.put("Sasa", "zzc");
        System.out.println("哈希表元素："+m + "   键：" + m.get("Tom"));

        // 9.2 TreeMap，以键排序，必须是同一类型的键，键对应的ASCII
        Map tree_m = new TreeMap();
        tree_m.put("peter", 5); tree_m.put("Petter", 5);
        tree_m.put("Ali", 11); tree_m.put("aaa", -11);
        System.out.println("树表  " +tree_m);

        // 9.3 linkedMap 链表键值对，维持添加元素的顺序，可以是不一同类型键值对
        Map linked_m = new LinkedHashMap(m);    // 类对象的继承
        Map linked_n = new LinkedHashMap(tree_m);

        System.out.println("树变换后的： " + linked_n +
                "     键：" + linked_n.keySet());
        System.out.println("链表键值对：  " + linked_m +
                "    值：" + linked_m.values());


    }

/*    10、 Map 例子
    10.1 记录每个字符在字符串中出现的次数,10.2 排序*/
    public void Map_example(){
        Map m = new HashMap();
        String str = "Hello, world Maybe I do not know who are you ";
        // str.toCharArray() 将字符串转换为一个个字符
        for (char x:str.toCharArray()){
            if (m.containsKey(x)){
                int old = (int) m.get(x);
                m.put(x, old+1);
            }
            else {
                m.put(x, 1);
            }
        }
        m.remove(' ');      // 删除表中指定的键-值对
        System.out.println(m);

        //
        int[] x = {-123,1,43,562,123,10,11,35,687, -11, 54};
        // 对指定范围的数组进行排序
        Arrays.sort(x, 1,7);
        for (int i: x){
            System.out.print(i + " , ");
        }
    }

    public static void main(String[] args){

    }
}
