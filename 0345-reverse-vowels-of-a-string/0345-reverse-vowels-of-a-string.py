class Solution:
    def reverseVowels(self, s: str) -> str:
        # Define vowels as a string for direct comparison
        vowels = "aeiouAEIOU"
        s = list(s)  # Convert string to a list for mutability
        left, right = 0, len(s) - 1  # Initialize pointers

        while left < right:
            # Move the left pointer to the next vowel
            while left < right and s[left] not in vowels:
                left += 1
            # Move the right pointer to the previous vowel
            while left < right and s[right] not in vowels:
                right -= 1
            
            # If both pointers are at vowels, swap them
            if left < right:
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1

        return ''.join(s)  # Convert list back to string

