public class DP_problem {
    public int maxProfit(int[] prices){
        int sell=0, prev_sell=0, buy = Integer.MIN_VALUE, pre_buy;
        for (int price:prices){
            pre_buy = buy;
            buy = Math.max(prev_sell-price, pre_buy);
            prev_sell = sell;
            sell = Math.max(pre_buy+price, prev_sell);
        }
        return sell;
    }
}
