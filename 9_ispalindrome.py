class Solution:
    def isPalindrome(self, x: int) -> bool:
        a = list(str(x))
        b = list(str(x))
        b.reverse()
        if a == b:
            return True
        else:
            return False