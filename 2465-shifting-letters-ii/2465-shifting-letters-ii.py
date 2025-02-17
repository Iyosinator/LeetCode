class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        s = list(s)
        pos = [0]*(len(s)+1)
        for start, end, shift in shifts:
            if shift == 1:
                pos[start]+=1
                pos[end+1]-=1
            else:
                pos[start]-=1
                pos[end+1]+=1
        pfx = [0]*(len(s))
        pfx[0] = pos[0]%26
        for i in range(1, len(pfx)):
            pfx[i] = (pfx[i-1] + pos[i])%26

        # print(pfx)
        for idx, ch in enumerate(s):
            order = pfx[idx] + ord(ch)
            print(order)
            if order > 122:
                order = 97 + (order - 123)
            elif order < 97:

                order = 123 - (97 - order)

            s[idx] = chr(order)
        return "".join(s)
        




        
        
