class Solution:
    def frequencySort(self, s: str) -> str:
        freq = {}

        for char in s:
            freq[char] = freq.get(char,0) + 1
        sorted_chars = sorted(freq.keys(), key=lambda x: -freq[x])
        return ''.join(char * freq[char] for char in sorted_chars)

        
        
        
