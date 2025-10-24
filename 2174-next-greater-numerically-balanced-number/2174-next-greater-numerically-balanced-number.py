class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        current = n + 1
        while True:
            count = Counter(str(current))
            if all(int(digit) == freq for digit, freq in count.items()):
                return current
            current += 1