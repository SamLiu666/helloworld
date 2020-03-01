import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;

public class Main {
    public static void main(String[] args){
        // 初始化 动态数组
        List<Integer> v0 = new ArrayList<>();
        List<Integer> v1;

        //数组变为向量
        Integer[] a = {0, 1,2,3,4};
        v1 = new ArrayList<>(Arrays.asList(a));
        //3备份
        List<Integer> v2 = v1;
        List<Integer> v3 = new ArrayList<>(v1);
        //3输出长度
        System.out.println("The size of v1 is : " + v1.size());
        System.out.println("第一个元素: " + v1.get(0));
        //迭代向量
        System.out.print("V1: ");
        for(int i=0; i < v1.size(); ++i){
            System.out.print(" " + v1.get(i));
        }
        System.out.println();
        System.out.print("[Version 2] The contents of v1 are:");
        for (int item : v1) {
            System.out.print(" " + item);
        }
        System.out.println();
        // 6. modify element
        v2.set(0, 5);       // modify v2 will actually modify v1
        System.out.println("The first element in v1 is: " + v1.get(0));
        v3.set(0, -1);
        System.out.println("The first element in v1 is: " + v1.get(0));
        // 7. sort
        Collections.sort(v1);
        // 8. add new element at the end of the vector
        v1.add(-1);
        v1.add(1, 6);
        // 9. delete the last element
        v1.remove(v1.size() - 1);
    }
}

