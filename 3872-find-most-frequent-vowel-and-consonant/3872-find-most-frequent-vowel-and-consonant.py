class Solution:
    def maxFreqSum(self, s: str) -> int:
        vowel = defaultdict(int)
        consonant = defaultdict(int)

        vowel_list = ['a','e','i','o','u']


        for i in s:
            if i in vowel_list:
                vowel[i] += 1
            else:
                consonant[i] += 1

        if len(vowel) == 0:
            max_vowel = 0
        else:
            max_vowel = max(vowel.values())
        if len(consonant) == 0:
            max_consonant = 0
        else:
            max_consonant = max(consonant.values())

        summ = max_vowel + max_consonant


        return summ


        