class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        store = set()
        left = 0
        longest = 0
        
        for right in range(len(s)):
            while s[right] in store:
                store.remove(s[left])
                left += 1
            store.add(s[right])
            longest = max(longest,right-left+1)
        return longest
        