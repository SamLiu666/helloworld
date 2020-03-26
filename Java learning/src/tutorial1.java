import java.util.*;

public class tutorial1 {
    // 1、JAVA 数据类型
    public void dataType(){

        // 蓝色数据：基础类型
        int hello_world = 1;
        double num2 =5.0;
        boolean bo = true;
        char ch = 'a';  //单引号表示一个字符
        //非基础数据类型
        String str = "hello,  world";   //任意字符个数
        int num3 = (int) num2;
        System.out.print(num3 + num2);
        //运算符
        int a = 5; int b = 4; int c = 7;
        double sum = a + b - c;
        float other = a * b - c/4;
        int zhishu = (int) Math.pow(2,3); // 8
        int quyu = 56 % 5;     //取余
        System.out.print(zhishu + " " + sum + " "+ other);
    }

    // 2、扫描，输入输出，导入库 Scanner
    public void Scanner(){
        Scanner sca =  new Scanner(System.in);  //键盘输入
        String scanned = sca.next();    // 获取输入的一个字符串如 hello world 输出 hello
        int scanned1 = sca.nextInt();   // 输入整数，都是以回车结束
        int trans = Integer.parseInt(scanned); // 转换为整数
        System.out.println(scanned + " " +scanned1 + " " + trans);
    }

    // 3、逻辑运算和 boolean 类型
    public void logicOperate(){
        // boolean 逻辑 与 &&, 或 ||, 非 !
        int a = 6; int b = 7; int c = 10;
        boolean compare;    // > < >= <= == !=
        compare = a <= b;   // 整数对比
        //字符串比较,相等或不相等
        String x = "Hello"; String y = "hello";
        compare = x==y && a<b || a<c ;   //优先级
        System.out.print(compare);
    }

    // 4、if else if else 判断语句
    public void ifDecision(){
        Scanner sc = new Scanner(System.in);
        String s = sc.nextLine();  // 输入一整行
        // 字符串比较使用 s.equals()，使用等号不一致
        if (s.equals("Good")){
            System.out.println("You input GOOD not good!"); }
        // elif 顺序读程序优先执行
        else if(s.equals("hi")){
            System.out.println("hello"); }
        else{   System.out.println(s + " world! "); }   // else 最后结尾
    }

    // 5、嵌套语句
    public void NestedSentence(){
        System.out.println("输入您的年龄: ");
        Scanner sc = new Scanner(System.in);
        String s = sc.nextLine();
        int age = Integer.parseInt(s);
        if (age >= 18) {
            System.out.println("成年啦，你喜欢什么食物");
            String food = sc.nextLine();
            if (food.equals("面条")){
                System.out.println("我也喜欢面条");
            }
            else{  System.out.println("不是我的菜"); }
        }
        else if (age >= 14) System.out.println("青少年");
        else System.out.println("不知道");
    }

    // 6、数组
    public void CreateArray(){
        //数组初始化，要定义数组的大小，
        String[] strArray = new String[10];     //字符串数组，无法改变数组的大小
        int[] newArray = {1, 2, 3, 4, 5, 6, 7};     // 整数数组初始化
        strArray = new String[]{"Hello", "Good", "Byebye", "Nice", "pppp"};  // 赋值
        System.out.println(strArray[2]+ " " + newArray[0] );
    }

    // 7、 循环控制语句 for， while
    public void controlLoop(){
        int x = 0, y=0;
        for (int i=0; i<5; i++){
            y += 1;
            System.out.println(i + " "+ x + " " + y);
            x +=1;
            if (x>3) break;         //结束循环
        }
        System.out.println("数组");

        // 7.1数组循环赋值
        int[] arr = new int[6];
        for (int i=0; i<5; i++){
            arr[i] = i+1;
            System.out.println(arr[i]);
        }
        System.out.println(Arrays.stream(arr));
        // 7.2元素循环
        for (int element: arr){
            element += 1;
            System.out.println(element);
        }

        // 键盘输入，字符串数组赋值
        String[] newstr = new String[5];
        Scanner sc = new Scanner(System.in);

        for (int i=0; i< newstr.length; i++){
            System.out.print("请输入，退出请输入q：");
            newstr[i] = sc.nextLine();
            if(newstr[i].equals("q") )
                break;
        }
        for (String i:newstr)
            System.out.println(i);

        // while 循环
        int i=0;
        while (i<10){
            i += 1;
            if(i==5)
                System.out.print("i == 5");
            continue;
        }
    }

    public static void main(String[] args){
        // 8、列表和集合,list sett
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

        // 8.2 列表，原集合 t= [-2, 100, 5, 56, 12, 30]
        ArrayList<Integer> list_t = new ArrayList<>(t);
        list_t.add(6);  list_t.get(6);  //获取元素索引
        list_t.set(2, 60);  // 改变指定位置处 元素
        // 获取 1~4 处字串, list.subList(i, j)
        System.out.println(list_t + " 数组列表 " + list_t.subList(1,4));

        // 链表结构
        LinkedList<Integer> linkList = new LinkedList<Integer>(list_t);
        System.out.println(" 链表列表  " + linkList);

    }
}
