class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        # Use the first string as the initial prefix
        prefix = strs[0]
        
        # Compare the prefix with each string in the list
        for string in strs[1:]:
            # While the prefix is not a prefix of the current string
            while not string.startswith(prefix):
                # Shorten the prefix by removing the last character
                prefix = prefix[:-1]
                # If prefix becomes empty, return ""
                if not prefix:
                    return ""
        
        return prefix
