class Solution:
    def isPalindrome(self, s: str) -> bool:
        newstr = []
        for char in s:
            if char.isalnum():
                newstr.append(char.lower())
        
        left = 0
        right = len(newstr) - 1
        while left < right:
            if newstr[left] != newstr[right]:
                return False
            left+=1
            right-=1
        return True
            