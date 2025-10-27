class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        total = 0
        row_counts = [row.count('1') for row in bank]
        row_counts = [count for count in row_counts if count != 0]
    
        for i in range(1,len(row_counts)):
            total+= (row_counts[i-1] * row_counts[i])

        return total

        
