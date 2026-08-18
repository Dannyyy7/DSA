class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        n = len(strs)

        for i in range(n):
            for j in range(0, n - i - 1):
                if strs[j] > strs[j + 1]:
                    strs[j], strs[j + 1] = strs[j + 1], strs[j]  
        first =strs[0]
        last=strs[-1]
        ans =""
        for i in range(min(len(first),len(last))):
            if first[i]!=last[i]:
                return ans
            ans+=first[i]
        return ans





        