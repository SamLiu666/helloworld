import java.util.List;

public class myString {
    /*两个二进制字符串相加
    思路：
     */
    public String addBinary(String a, String b){
        StringBuilder sb = new StringBuilder();
        int i = a.length() - 1, j = b.length() -1, carry = 0;
        while (i >= 0 || j >= 0) {
            int sum = carry;
            if (j >= 0) sum += b.charAt(j--) - '0';
            if (i >= 0) sum += a.charAt(i--) - '0';
            sb.append(sum % 2);
            carry = sum / 2;
        }
        if (carry != 0) sb.append(carry);
        return sb.reverse().toString();
    }

    public int strStr(String s, String t) {
        if (t.isEmpty()) return 0; // edge case: "",""=>0  "a",""=>0
        for (int i = 0; i <= s.length() - t.length(); i++) {
            for (int j = 0; j < t.length() && s.charAt(i + j) == t.charAt(j); j++)
                if (j == t.length() - 1) return i;
        }
        return -1;
    }

    /*  最长公共字串问题
        思路：最长公共子串也是一个个之间的字串
        1.水平扫描（垂直扫描） 算法复杂度：O(N)
        2.分治算法
  */
    public String longestCommonPrefix_0(String[] strs) {
        if (strs.length == 0) return "";
        //选定第一个字串为公共子串
        String prefix = strs[0];
        for (int i = 1; i < strs.length; i++)
            while (strs[i].indexOf(prefix) != 0) {
                prefix = prefix.substring(0, prefix.length() - 1);
                if (prefix.isEmpty()) return "";
            }
        return prefix;
    }

    //分治算法
    public String longestCommonPrefix(String[] strs) {
        if (strs == null || strs.length == 0) return "";
        return longestCommonPrefix(strs, 0 , strs.length - 1);
    }
    private String longestCommonPrefix(String[] strs, int l, int r) {
        if (l == r) {
            return strs[l];
        }
        else {
            int mid = (l + r)/2;
            String lcpLeft =   longestCommonPrefix(strs, l , mid);
            String lcpRight =  longestCommonPrefix(strs, mid + 1,r);
            return commonPrefix(lcpLeft, lcpRight);
        }
    }
    String commonPrefix(String left,String right) {
        int min = Math.min(left.length(), right.length());
        for (int i = 0; i < min; i++) {
            //charAt() 方法用于返回指定索引处的字符。索引范围为从 0 到 length() - 1
            if ( left.charAt(i) != right.charAt(i) )
                return left.substring(0, i);
        }
        return left.substring(0, min);
    }

    /*翻转字符串，固定时间，双指针
    思路：双指针，交换
     */
    public void reverseString(char[] s){
        int left=0, right=s.length-1;
        while (left<right){
            char temp = s[left];
            s[left++] = s[right];
            s[right--] = temp;
        }
    }

    /*两数相加=目标，给定数组已升序
    思路：双指针，大于右边--，小于左边++
     */
    public int[] twoSum(int[] numbers, int target){
        int start=0,end=numbers.length-1;
        while (start<end){
            if(numbers[start]+numbers[end] == target)break;;
            if(numbers[start]+numbers[end]<target) start++;
            else end--;
        }
        return new int[]{start+1, end+1};
    }

    //翻转数组，给定k，从k位置处翻转
    public void rotate(int[] nums, int k) {
        k %= nums.length;
        reverse(nums, 0, nums.length - 1);
        reverse(nums, 0, k - 1);
        reverse(nums, k, nums.length - 1);
    }
    public void reverse(int[] nums, int start, int end) {
        while (start < end) {
            int temp = nums[start];
            nums[start] = nums[end];
            nums[end] = temp;
            start++;
            end--;
        }
    }
}
