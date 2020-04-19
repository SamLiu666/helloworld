import java.util.Random;

class configure{

    // 构造器，和类名一致，会被直接调用
    configure(){
        System.out.print("构造器重载" + '\n');
    }

    configure(int i){
        // 创建对象并初始化，构造器没有返回值
        System.out.print("hello "+ i + " ");
    }


}

public class Initialize_clean_6 {
    // this 方法，类内部会自动调用，可不写，不过在需要返回时，要明确this，这个实例
    int i = f();
    int j = g(i);

    int f() {
        return 11;
    }

    int g(int n) {
        return n * 10;
    }

    public static void main(String[] args){
        new Random(47)
                .ints(5, 20)
                .distinct()
                .limit(7)
                .sorted()
                .forEach(System.out::println);
    }
}
