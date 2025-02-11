class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        hindex  = 0
        for i in range(len(citations)):
            '''
            if len(citations) == 1:
                hindex = 1
            if len(citations) == 1 and citations[i] == 0:
                hindex = 0
            '''
            hindex = max(hindex,min(citations[i],len(citations)-i))
        return hindex