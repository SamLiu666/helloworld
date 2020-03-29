import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class Array {
    // i++ 用完i 再++; ++i 先i+1再用

    /*给一个数组，[1,3,7,6,5,6] 输出 6 的下标：3，以6 左边的和 = 右边的和
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

    /*  给定一个数组，返回最大值的下标，最大值都大于数组中每一个值，否则返回‘-1’
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

    /* 二位数组Z字输出问题
    思路：简化问题成对角线输出问题，[i,j] 可以行升[i-1, j+1];问题差异在偶数时反向输出
    1.初始化要返回的数组，2.外循环for遍历对角线，3.内循环while计算相应对角线元素数量，4.反向将奇数添加到中间数组
    算法复杂度：O(N*N) 二维矩阵的N*N;Space Complexity: O(min(N, M))
     */
    public int[] findDiagonalOrder(int [][] matrix){
        //检查是否为空矩阵
        if(matrix==null || matrix.length==0){
            return new int[0];
        }
        //变量追踪矩阵的大小
        int N=matrix.length;
        int M=matrix[0].length;
        //初始化结果矩阵和当前矩阵
        int [] result = new int[N*M];
        int k =0;
        ArrayList<Integer> intermediate = new ArrayList<Integer>();
        //遍历所有元素
        for(int d=0; d<N+M-1;d++){
            //每次循环都清空当前数组
            intermediate.clear();
            //找出开始元素下标
            int r=d<M? 0: d-M+1;
            int c=d<M? d:M-1;
            //循环添加元素
            while (r<N&&c>-1){
                intermediate.add(matrix[r][c]);
                ++r;--c;
            }
            if(d%2==0){
                Collections.reverse(intermediate);
            }

            for(int i=0;i<intermediate.size();i++){
                result[k++] = intermediate.get(i);
            }
        }
        return result;
    }

    /* 螺旋矩阵输出
    思路：模拟，顺时针从左到右，到下，到上，到右
     */
    public List<Integer> spiralOrder(int[][] matrix){
        List ans = new ArrayList();
        if(matrix.length==0) return ans;
        int R= matrix.length, C = matrix[0].length;
        boolean[][] seen = new boolean[R][C];
        int[] dr = {0,1,0,-1};
        int[] dc = {1,0,-1,0};
        int r=0,c=0,di=0;
        for(int i=0; i<R*C; i++){
            ans.add(matrix[r][c]);
            seen[r][c]=true;
            int cr=r+dr[di];
            int cc=c+dc[di];
            if(0 <= cr && cr < R && 0 <= cc && cc < C && !seen[cr][cc]){
                r=cr;c=cc;
            }else{
                di = (di + 1) % 4;
                r += dr[di];
                c += dc[di];
            }
        }
        return ans;
    }

    /*Pascal's Triangle
    思路：动态规划的思想
    Time complexity : O(numRows^2)
     */
    public List<List<Integer>> generate(int numRows){
        List<List<Integer>> triangle = new ArrayList<List<Integer>>();
        if(numRows==0) return triangle;
         triangle.add(new ArrayList<>());
         triangle.get(0).add(1);

         for(int rowNum=1; rowNum<numRows; rowNum++){
             List<Integer> row = new ArrayList<>();
             List<Integer> prevRow = triangle.get(rowNum-1);

             // The first row element is always 1.
             row.add(1);

             // Each triangle element (other than the first and last of each row)
             // is equal to the sum of the elements above-and-to-the-left and
             // above-and-to-the-right.
             for (int j = 1; j < rowNum; j++) {
                 row.add(prevRow.get(j-1) + prevRow.get(j));
             }

             // The last row element is always 1.
             row.add(1);

             triangle.add(row);
         }

        return triangle;
    }

}
