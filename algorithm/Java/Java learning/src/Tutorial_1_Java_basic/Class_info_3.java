package Tutorial_1_Java_basic;

import java.util.Scanner;

public class Class_info_3 {

    // 静态公共方法可直接调用
    public static void myOwnClass(String str, int x){
        for (int i=0; i<x; i++)
            System.out.println(str);
    }

    // 两种创建类方法的方式，传递参数
    public String myOwn(String str){
        System.out.println(str + "  myOwn");
        return str + "  Return";
    }


    public static void main(String[] args){
        // 类实例化
        Class_info_3 m = new Class_info_3();
        Scanner sc = new Scanner(System.in);
        String str = sc.nextLine();
        int i =3;

        myOwnClass(str, i);    //调用静态方法
        String ss = m.myOwn(str);       //调用内部方法
        System.out.println(ss);
    }
}
