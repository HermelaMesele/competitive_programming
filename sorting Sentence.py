class Solution:
    def sortSentence(self, s: str) -> str:
        words = s.split()
        ans = [None] * len(words)
        for w in words:
            i = int(w[-1]) - 1
            ans[i] = w[:-1]
        return ' '.join(ans)
class Solution:
    def sortSentence(self, S: str) -> str:
        s = S.split()
        n = len(s)
        res = [""] * n
        
        for c in s:
            i = int(c[-1])
            res[i - 1] = c[:-1]
        
        return " ".join(res)
