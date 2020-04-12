package Tutorial_1_Java_basic;

public class Dog_main {
    public static void main(String[] args){
        Dog tim = new Dog("Tim", 5);
        tim.speak();    //类私有方法调用
        tim.setAge(15);
        tim.speak();    //类私有方法调用
        tim.add_age();
        tim.speak();

        Cat_from_dog cat = new Cat_from_dog("Polo", 20, 22);
        cat.speak();
        cat.eat(2);
        cat.speak();
        System.out.println("单一变量赋值");
        Cat_from_dog cat_1 = new Cat_from_dog("One");
        cat_1.speak();

        // STATIC 测试
//        Tutorial_1_Java_basic.Dog.count = 0;
        Dog bill = new Dog("bill", 10);
        System.out.println(Dog.count);

        // Static方法
        Dog.display("hello world");
        Cat_from_dog.display("CAT hello world");

        // 比较对象
        Dog tom = new Dog("Tim", 5);
        System.out.println("对象比较"+tim.equals(tom)
                + " 名字比较： " + tim.equals_name(tom));
        Dog tom2 = new Dog("Sim", 5);
        System.out.println("首字母进行比较 "+tim.compareTo(tom)
                + "  父类与子类的比较： " + tom.compareTo(cat)
                + " 首字母S&T 之间的距离" + tom.compareTo(tom2)
        );
        System.out.println(tom.toString()); //JAVA 默认的方法 .toString()

        Dog.InnerClass in = tom2.new InnerClass();
        in.display();

    }
}
