from collections import Counter
class Solution:
    def beautySum(self, s: str) -> int:
        tot_beauty=0
        for i in range (len(s)):
            freq=Counter()
            for j in range (i,len(s)):
                freq[s[j]]+=1
                max_freq=max(freq.values())
                min_freq=min(freq.values())
                if len(freq)>1:
                    tot_beauty+=max_freq-min_freq
       
        return tot_beauty

        