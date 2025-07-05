class Solution:
    def findLucky(self, arr: List[int]) -> int:
        x = Counter(arr)
        maxx = 0

        for i,j in x.items():
            if i == j:
                maxx = max(i,maxx)
        

        if maxx != 0:
            return maxx
        else:
            return -1
    
        