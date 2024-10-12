class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Initalize the pointers
        left = 0
        right = len(numbers) -1

        while left < right:
            currentsum = numbers[left] + numbers[right]
            if target == currentsum:
                return [left+1,right+1]
            elif target < currentsum:
                right-=1
            else:
                left+=1




