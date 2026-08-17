class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_c=0
        current_c=0
        for num in nums:
            if num==1:
                current_c+=1
                max_c=max(max_c,current_c)
            else:
                current_c=0
        return max_c    



          
        