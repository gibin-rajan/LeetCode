class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # compute the opitimal partition to execute 2 trades 
        # Where can we split the array to maximize our profits?
        # i = k execute best time to buy and sell stock on prices[0:k] and prices[k:n]
        n = len(prices)
        dp1 = [0] * n

        
        maxprofit = 0
        buy = prices[0]
        #loop to compute dp1[i] where dp1[i] is the max profit from buying and selling between day 0 and i 
        for i in range(n):
            if prices[i] < buy:
                buy = prices[i]
            else:
                maxprofit = max(maxprofit, prices[i] - buy)
            dp1[i] = maxprofit
        
        dp2 = [0] * n
        #loop to compute dp2[i] where dp2[i] is the max profit from buying and selling between day i and n 
        maxprofit = 0
        sell = prices[-1]
        for i in range(n-2, -1, -1):
            if prices[i] > sell:
                sell = prices[i]
            else:
                maxprofit = max(maxprofit, sell-prices[i])
            dp2[i] = maxprofit
        
        maxprofit = dp1[-1]

        for i in range(1,n-1):
            maxprofit = max(maxprofit, dp1[i]+dp2[i])
        return maxprofit