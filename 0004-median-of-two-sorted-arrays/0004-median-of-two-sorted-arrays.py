class Solution:
    def findMedianSortedArrays(self, a: List[int], b: List[int]) -> float:
        if len(a) > len(b):
            a, b = b, a
        m, n = len(a), len(b)
        l, r = 0, m
        while l <= r:
            i = (l+r)//2
            j = (m+n+1)//2-i
            al = float('-inf') if i == 0 else a[i-1]
            ar = float('inf') if i == m else a[i]
            bl = float('-inf') if j == 0 else b[j-1]
            br = float('inf') if j == n else b[j]
            if al <= br and bl <= ar:
                if (m+n)%2:
                    return max(al, bl)
                return (max(al, bl)+min(ar, br))/2
            elif al > br:
                r = i-1
            else:

                l = i+1