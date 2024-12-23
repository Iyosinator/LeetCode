class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_wealth = 0
        for wealth in accounts:
            single_wealth = sum(wealth)
            max_wealth = max(single_wealth,max_wealth)
        return max_wealth    
        