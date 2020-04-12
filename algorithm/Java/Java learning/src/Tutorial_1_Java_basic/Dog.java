package Tutorial_1_Java_basic;

public class Dog implements Comparable<Dog> {
    //11、类 实例化 继承
    //类私有属性，只允许此类访问
    protected String name;      // 只有此类下的子类可以访问
    public int age;
    public static int count = 0;    // 同类都会增加

    // 类实例化
    public Dog(String name, int age){
        this.name = name;
        this.age = age;
        this.count += 1;      // 两种方法都可以
//        Tutorial_1_Java_basic.Dog.count += 1;
//        add_age();  // 实例化时会执行
//        speak();  //实例化时会执行
    }

    public void speak(){
        System.out.println("Hello " + this.name + ", YOUR Age is  " + this.age);
    }

    public int getAge(){
        return this.age;
    }

    public void setAge(int age){
        this.age = age;
    }

    public int add_age(){
        return this.age += 1;
    }

    // static method
    public static void display(String ss){
        System.out.println(ss);
    }

    // 类的比较
    public boolean equals_name(Dog other){
        if (this.name == other.name)
            return true;
        else
            return false;
    }

    // 类比较，引入comparable 接口
    public int compareTo(Dog other){
        return this.name.compareTo(other.name);
    }

    // 字符串显示
    public String toString(){
        return this.name;
    }

    // 内部类
    public class InnerClass{
        public void display(){
            System.out.println(" 内部类的调用 ");
        }

        public void inner(){
            InnerClass in = new InnerClass();
            in.display();
        }
    }
}
