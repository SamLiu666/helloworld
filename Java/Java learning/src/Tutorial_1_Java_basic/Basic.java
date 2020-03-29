package Tutorial_1_Java_basic;

public class Basic {
    private final int x;
    private final int y;

    private static void show() {
        System.out.println("123");
    }

    public Basic(int x, int y) {
        this.x = x;
        this.y = y;
    }

    public static void main(String[] args){
//        Integer x = new Integer(123);
//        Integer y = new Integer(123);
//        System.out.println(x == y);    // false
//        Integer z = Integer.valueOf(123);
//        Integer k = Integer.valueOf(123);
//        System.out.println(z == k);   // true
//        int a =3; int b=3;
//        System.out.print(a == b);
//        String s1 = new String("aaa");
//        String s2 = new String("aaa");
//        String s1 = "abc";
//        String s2 = "abc";
//        System.out.println(s1 == s2);
//        String s3 = s1.intern();
//        String s4 = s1.intern();
//        System.out.println(s3 == s4);           // true
        //等价和相等， this.equals() ==
//        Tutorial_1_Java_basic.Basic a1 = new Tutorial_1_Java_basic.Basic();
//        show();
//        Character x = new Character('a');
//        Character y = new Character('a');
//        System.out.println(x.equals(y)); // true
//        System.out.println(x == y);      // false
//        Tutorial_1_Java_basic.Basic e1 = new Tutorial_1_Java_basic.Basic(1, 1);
//        Tutorial_1_Java_basic.Basic e2 = new Tutorial_1_Java_basic.Basic(1, 1);
//        System.out.println(e1.equals(e2)); // true
        Integer x = 5;
        System.out.println(x.toString());
        System.out.println(Integer.toString(12));
    }

}
