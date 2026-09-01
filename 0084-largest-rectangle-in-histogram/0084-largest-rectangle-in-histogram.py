class Solution:
    def largestRectangleArea(self, h: List[int]) -> int:
        stack = []
        ans = 0
        h.append(0)
        for i, x in enumerate(h):
            while stack and h[stack[-1]] > x:
                height = h[stack.pop()]
                left = stack[-1] if stack else -1
                ans = max(ans, height * (i - left - 1))
            stack.append(i)
        return ans
        