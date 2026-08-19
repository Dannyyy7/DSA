class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        posi=[]
        neg=[]
        for num in nums:
            if num>0:
                posi.append(num)
            else:
                neg.append(num)
        result=[]
        for i in range(len(posi)):
            result.append(posi[i])
            result.append(neg[i])
        return result