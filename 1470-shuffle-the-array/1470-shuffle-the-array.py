class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        x = nums[:n]
        y = nums[n:]
        z = []

        for i in range(len(x)):
            z.append(x[i])
            z.append(y[i])

        return z
