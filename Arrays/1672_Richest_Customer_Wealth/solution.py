class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_wealth = max(sum(account) for account in accounts)
        return max_wealth
