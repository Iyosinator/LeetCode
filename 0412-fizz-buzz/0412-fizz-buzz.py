class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        # if i is divisible by 3 and 5 -> FizzBuzz
        # if i is divisible by 3 -> Fizz
        # if i is divisible by 5 -> Buzz
        result = []
        for i in range(1, n + 1):
            s = ""
            if i % 3 == 0:
                s += "Fizz"
            if i % 5 == 0:
                s += "Buzz"
            if not s:
                s = str(i)
            result.append(s)
        return result