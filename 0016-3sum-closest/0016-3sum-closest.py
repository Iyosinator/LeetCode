class Solution(object):
    def threeSumClosest(self, numbers, target_value):
        
        numbers.sort()
        nearest_sum = float('inf')
        
        for index in range(len(numbers) - 2):
            left_pointer, right_pointer = index + 1, len(numbers) - 1
            while left_pointer < right_pointer:
                current_total = numbers[index] + numbers[left_pointer] + numbers[right_pointer]
                if abs(current_total - target_value) < abs(nearest_sum - target_value):
                    nearest_sum = current_total
                if current_total < target_value:
                    left_pointer += 1
                elif current_total > target_value:
                    right_pointer -= 1
                else:
                    return current_total
        
        return nearest_sum
