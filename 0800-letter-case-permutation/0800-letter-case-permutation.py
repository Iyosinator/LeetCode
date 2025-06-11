class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        letter_indexes = []
        for i in range(len(s)):
            if s[i].isalpha():
                letter_indexes.append(i)

        result = []
        total = 1 << len(letter_indexes)  

        for mask in range(total): 
            temp = list(s)
            for i in range(len(letter_indexes)):
                index_in_s = letter_indexes[i]

                if (mask >> i) & 1:  
                    temp[index_in_s] = temp[index_in_s].upper()
                else: 
                    temp[index_in_s] = temp[index_in_s].lower()

            result.append("".join(temp))

        return result
