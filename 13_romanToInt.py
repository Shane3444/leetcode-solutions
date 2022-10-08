d = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}

class Solution:
    def romanToInt(self, s: str) -> int:
        val = 0
        s1 = list(s)
        i = len(s) - 1
        while i >= 0:
            if i == len(s) - 1:
                val += d[s1[i]]
            elif d[s1[i]] >= d[s1[i+1]]:
                val += d[s1[i]]
            else:
                val -= d[s1[i]]
            i -= 1
        return val