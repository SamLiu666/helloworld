import java.util.Scanner;

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

    // 4、if elif else 判断语句
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

    public static void main(String[] args){

    }
}
