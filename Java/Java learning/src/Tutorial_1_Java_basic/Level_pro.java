package Tutorial_1_Java_basic;

public enum Level_pro {
    // 类似哈希表

    high(3),
    medium(2),
    low(1);

    private int lvlNum;

    //哈希表构造器
    private Level_pro(int num){
        this.lvlNum = num;
    }

    public int getLvlNum(){
        return this.lvlNum;
    }

    public void setLvlNum(int num){
        this.lvlNum = num;
    }
}
