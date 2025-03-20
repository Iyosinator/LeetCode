class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(path):
            if len(path) == len(nums):
                result.append(path[:])
                return
            
            for i in range(len(nums)):
                if nums[i] not in path:
                    path.append(nums[i])
                    backtrack(path)
                    path.pop()

        result = []
        backtrack([])
        return result