class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left = max(weights)
        right = sum(weights)
        while left < right:
            mid = (left + right) // 2
            current = 0
            required = 1
            for weight in weights:
                if current + weight > mid:
                    required += 1
                    current = 0
                current += weight
            if required <= days:
                right = mid
            else:
                left = mid + 1
        return left