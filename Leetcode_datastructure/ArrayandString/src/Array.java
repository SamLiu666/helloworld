public class Array {
    // i++ 用完i 再++; ++i 先i+1再用

    /*给一个数组，[1,3,7,6,5,6] 输出 6 的下标：3，
        以6 左边的和 = 右边的和
        思路： right_sum == sum - nums[index] - left_sum
        Time Complexity: O(N), where N is the length of nums.*/
    public int pivotIndex(int[] nums){

        int sum = 0, leftsum = 0;
        for(int x: nums)    sum += x;
        for(int i=0; i<nums.length; ++i){
            if(leftsum==sum - leftsum -nums[i]) return i;
            leftsum += nums[i];
        }
        return -1;
    }

    /*  给定一个数组，返回最大值的下标，最大值都大于数组中每一个值
        否则返回‘-1’
        思路：找出数组中最大值，然后For循环遍历整个数组，判断条件是否成立
        算法复杂度： O（N）, N = 数组长度*/
    public int dominant(int[] nums){
        int maxIndex = 0;
        for(int i=0; i< nums.length; ++i){
            if(nums[i] > nums[maxIndex]){
                maxIndex = i;
            }
        }
        for(int i=0; i<nums.length; ++i){
            if(maxIndex != i && nums[maxIndex] < 2*nums[i])
                return -1;
        }
        return maxIndex;
    }

    // 打印二维数组
    private static void printArray(int[][] a) {
        for (int i = 0; i < a.length; ++i) {
            System.out.println(a[i]);
        }
        for (int i = 0; i < a.length; ++i) {
            for (int j = 0; a[i] != null && j < a[i].length; ++j) {
                System.out.print(a[i][j] + " ");
            }
            System.out.println();
        }
    }


}
