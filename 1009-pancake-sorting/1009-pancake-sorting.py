
class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        ans = []
        n = len(arr)
        
        for value in range(n, 0, -1): 
            index = arr.index(value) 
            
            if index == value - 1:  
                continue 
            
            if index != 0:
                ans.append(index + 1)  
                arr[:index + 1] = reversed(arr[:index + 1])
            
            ans.append(value)  
            arr[:value] = reversed(arr[:value])
        
        return ans
