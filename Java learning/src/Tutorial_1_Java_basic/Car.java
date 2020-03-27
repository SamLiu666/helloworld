package Tutorial_1_Java_basic;

public class Car implements Vehicle {

    private int gear=1;
    private int speed=0;

    @Override
    public void changeGear(int gear) {
        this.gear = gear;
    }

    @Override
    public void speedup(int change) {
        this.speed += change;
    }

    @Override
    public void slowdown(int change) {
        this.speed -= change;
    }

    @Override
    public void display() {
        System.out.println("Drive a car, going " + this.speed
                +" km/h and in gear " + this.gear);
        out();
    }

}
