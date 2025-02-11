
class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        ans = []
        n = len(arr)
        
        for value in range(n, 0, -1):  # Move largest values to their correct place
            index = arr.index(value)  # Find the position of the current largest number
            
            if index == value - 1:  # If already in the correct place, continue
                continue 
            
            if index != 0:
                ans.append(index + 1)  # Bring the largest number to the front
                arr[:index + 1] = reversed(arr[:index + 1])
            
            ans.append(value)  # Move the largest number to its correct position
            arr[:value] = reversed(arr[:value])
        
        return ans
