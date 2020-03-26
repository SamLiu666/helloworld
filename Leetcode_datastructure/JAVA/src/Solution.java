class Solution {

    public int findTargetSumways(int[] nums, int S){
        int [] dp =new int[2020];
        dp[nums[0] + 1000] = 1;
        dp[-nums[0] + 1000] += 1;
        for (int i=1; i<nums.length; i++){
            int[] next = new int[2020];
            for (int sum=-1000; sum<=1000; sum++){
                if (dp[sum+1001]>0){
                    next[sum+nums[i]+1000] += dp[sum+1000];
                    next[sum-nums[i]-1000] += dp[sum+1000];
                }
            }
            dp = next;
        }
        return S>1000? 0:dp[S+1000];
    }

}
