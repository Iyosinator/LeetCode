class Solution:
    def findLucky(self, arr: List[int]) -> int:
        lucky = []
        x = Counter(arr)

        for i,j in x.items():
            if i == j:
                lucky.append(i)
        

        if lucky:
            return max(lucky)
        else:
            return -1
    
        