package Tutorial_1_Java_basic;

public class Car_main {

    public static void main(String[] args){
        Car Ford = new Car();
        Ford.speedup(10);
        Ford.changeGear(2);
        Ford.display();
        System.out.println(Vehicle.math_plus(6));
        System.out.print("\n");

        Level_pro le = Level_pro.low;
        String en = le.toString();
        Level_pro[] arr = Level_pro.values();
        for (Level_pro ele: arr){
            System.out.print("  " + ele);
        }
        System.out.print("\n");

        if (le == Level_pro.high){
            System.out.print(le);
        }
        else
            System.out.println(en);

        System.out.println("分割线");
        Level_pro newL = Level_pro.low;
        System.out.println(Level_pro.valueOf("high") + "  "
                + newL.getLvlNum() + "  " );
        newL.setLvlNum(5);
        System.out.println(newL.getLvlNum());

    }
}
