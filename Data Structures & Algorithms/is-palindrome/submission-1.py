class Solution:
    def isPalindrome(self, s: str) -> bool:
        tgt = "".join(char for char in s.lower() if char.isalnum())
        print(tgt)
        return (tgt == tgt[::-1])