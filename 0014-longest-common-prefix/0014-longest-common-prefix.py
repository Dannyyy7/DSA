class Solution:
    def longestCommonPrefix(self, strs):
        
        
        n = len(strs)

        for i in range(n):
            for j in range(0, n - i - 1):
                if strs[j] > strs[j + 1]:
                    strs[j], strs[j + 1] = strs[j + 1], strs[j]

       
        first = strs[0]
        last = strs[-1]

        i = 0

        while i < len(first) and i < len(last):
            if first[i] != last[i]:
                break
            i += 1

        return first[:i]