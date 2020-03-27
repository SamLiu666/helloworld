package Tutorial_1_Java_basic;// 只能用公共方法，无需定义

public interface Vehicle {
    final int gears = 6;   // 所有类都是6，全局变量

    void changeGear(int gear);
    void speedup(int change);
    void slowdown(int change);
    void display();

    // 默认方法，内部函数调用
    default void out(){
        System.out.println("Default method");
    }

    //外部可以直接调用接口，static 方法
    static int math_plus(int change){
        return change + 1;
    }
}
