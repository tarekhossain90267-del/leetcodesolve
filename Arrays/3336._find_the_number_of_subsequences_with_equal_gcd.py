import math
MOD = 10**9 + 7

class Solution(object):

    def gcd(self, a, b):
        while b:
            a, b = b, a % b
        return a

    def subsequencePairCount(self, nums):
        n = len(nums)
        max_val = max(nums)
                
        dp = [[[0]*(max_val+1) for _ in range(max_val+1)] for _ in range(n+1)]
        dp[0][0][0] = 1  
        
        for i in range(n):
            num = nums[i]
            for g1 in range(max_val+1):
                for g2 in range(max_val+1):
                    if dp[i][g1][g2] == 0:
                        continue
                    
                    val = dp[i][g1][g2]
                    
                    dp[i+1][g1][g2] = (dp[i+1][g1][g2] + val) % MOD
                    
                    new_g1 = self.gcd(g1, num) if g1 else num
                    dp[i+1][new_g1][g2] = (dp[i+1][new_g1][g2] + val) % MOD
                    
                    new_g2 = self.gcd(g2, num) if g2 else num
                    dp[i+1][g1][new_g2] = (dp[i+1][g1][new_g2] + val) % MOD
        
        ans = 0
        for g in range(1, max_val+1):
            ans = (ans + dp[n][g][g]) % MOD
        return ans
