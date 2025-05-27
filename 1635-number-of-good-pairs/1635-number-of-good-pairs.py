class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        freq = Counter(nums)  
        good_pairs = 0
        for count in freq.values():
            good_pairs += count * (count - 1) // 2 
        return good_pairs