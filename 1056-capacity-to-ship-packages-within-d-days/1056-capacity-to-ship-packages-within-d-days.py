class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        def can_ship(capacity: int) -> bool:
            total_weight = 0
            days_needed = 1
            
            for weight in weights:
                total_weight += weight
                if total_weight > capacity:
                    days_needed += 1
                    total_weight = weight
                    if days_needed > days:
                        return False
            return True
        
        low, high = max(weights), sum(weights)
        
        while low < high:
            mid = (low + high) // 2
            if can_ship(mid):
                high = mid
            else:
                low = mid + 1
        
        return low
