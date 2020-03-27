package Tutorial_1_Java_basic;

public class Cat_from_dog extends Dog {

    private int food;   // 只有此子类可以访问

    public Cat_from_dog(String name, int age, int food) {
        // 继承
        super(name, age);
        this.food = food;
    }

    public Cat_from_dog(String name){
        // 其他继承方式
        super(name, 0);
        display("CAt call this");
    }

    public void speak(){
        System.out.println("Hello " + this.name + ", YOUR Age is " + this.age
                + " and eat " + this.food);
    }

    public void eat(int x){
        this.food -= x;
    }
}
