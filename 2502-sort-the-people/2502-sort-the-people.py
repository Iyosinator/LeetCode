class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        # Step 1: Create a dictionary mapping heights to names
        height_to_name = {heights[i]: names[i] for i in range(len(names))}
        
        # Step 2: Create a list of heights for sorting
        heights_list = list(heights)

        # Step 3: Bubble Sort to sort the heights in descending order
        n = len(heights_list)
        for i in range(n):
            swapped = False  # Track if any swaps were made
            for j in range(0, n - i - 1):  # Compare adjacent heights
                if heights_list[j] < heights_list[j + 1]:  # Sort in descending order
                    # Swap heights
                    heights_list[j], heights_list[j + 1] = heights_list[j + 1], heights_list[j]
                    swapped = True
            # If no swaps were made, the array is already sorted
            if not swapped:
                break

        # Step 4: Retrieve the names based on sorted heights
        sorted_names = [height_to_name[height] for height in heights_list]
        
        return sorted_names