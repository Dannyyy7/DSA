class Solution:
    def magicalString(self, n):
        if n <= 0:
            return 0
        if n <= 3:
            return 1
        arr = [1, 2, 2]
        i = 2
        num = 1
        count = 1
        while len(arr) < n:
            for _ in range(arr[i]):
                arr.append(num)
            num = 3 - num
            i += 1
        return arr[:n].count(1)