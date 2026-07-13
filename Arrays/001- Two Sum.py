class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i , num in enumerate(nums):
            need = target - num 
            if need in dic:
                return [dic[need],i]
            dic[num] = i    

        
        
