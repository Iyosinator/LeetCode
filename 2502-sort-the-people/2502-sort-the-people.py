class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        height_to_name = {heights[i]: names[i] for i in range(len(names))}
        heights_list = list(heights)
        n = len(heights_list)

        for i in range(n):
            for j in range(0, n - i - 1):
                if heights_list[j] < heights_list[j + 1]:  # Sort in descending order
                    heights_list[j], heights_list[j + 1] = heights_list[j + 1], heights_list[j]

        return [height_to_name[height] for height in heights_list]
