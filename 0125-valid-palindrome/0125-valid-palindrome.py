class Solution:
    def isPalindrome(self, s: str) -> bool:
        newStr = []
        for char in s:
            if char.isalnum():
                newStr.append(char.lower())
        return newStr == newStr[::-1]
