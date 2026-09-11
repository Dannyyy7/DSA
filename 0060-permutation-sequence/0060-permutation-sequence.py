class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        numbers = [str(i) for i in range(1, n + 1)]
        ans = ""
        k -= 1
        for i in range(n, 0, -1):
            fact = 1
            for j in range(1, i):
                fact *= j
            index = k // fact
            ans += numbers[index]
            numbers.pop(index)
            k %= fact
        return ans