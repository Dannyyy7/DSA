class Solution:
    def reverseWords(self, s: str) -> str:
        words = []
        word = ""
        for ch in s:
            if ch != " ":
                word += ch
            elif word:
                words.append(word)
                word = ""
        if word:
            words.append(word)
        ans = ""
        for i in range(len(words) - 1, -1, -1):
            ans += words[i]
            if i != 0:
                ans += " "
        return ans