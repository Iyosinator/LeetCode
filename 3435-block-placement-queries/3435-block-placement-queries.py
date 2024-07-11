from sortedcontainers import SortedList


class Solution:
    def getResults(self, queries: List[List[int]]) -> List[bool]:
        barriers = SortedList()  # Sorted list to maintain barrier positions
        barriers.add(0)  # Add initial barrier at position 0

        # Process the add-barrier queries to populate the barriers list
        for query in queries:
            if query[0] == 1:
                it = query[1]
                barriers.add(it)

        holes = SortedList()  # Sorted list to maintain hole sizes
        holes.add(float('inf'))  # Initialize with an infinitely large hole
        hole2start = {float('inf'): barriers[-1]}

        # Calculate initial hole sizes based on the barriers
        for pos in range(len(barriers) - 1):
            start = barriers[pos]
            end = barriers[pos + 1]
            size = end - start
            if size:
                pos = holes.bisect_left(size)
                hole_size = holes[pos]
                if hole2start[hole_size] > start:
                    if hole_size > size:
                        holes.add(size)
                    hole2start[size] = start

        barriers.add(float('inf'))  # Add an infinite barrier at the end
 
        result = []
        # Process the queries in reverse order
        for query in reversed(queries):
            if query[0] == 1:  # If it's an add-barrier query
                it = query[1]
                pos = barriers.bisect_left(it)
                left = barriers[pos - 1]
                right = barriers[pos + 1]
                size = right - left

                hole_pos = holes.bisect_left(size)
                if hole2start[holes[hole_pos]] > left:
                    while hole_pos > 0 and hole2start[holes[hole_pos - 1]] > left:
                        del hole2start[holes[hole_pos - 1]]
                        del holes[hole_pos - 1]
                        hole_pos -= 1

                    hole2start[size] = left
                    if holes[hole_pos] != size:
                        holes.add(size)

                barriers.remove(it)
            else:  # If it's a check-hole query
                _, start, size = query
                hole_pos = holes.bisect_left(size)
                hole = holes[hole_pos]
                result.append(hole2start[hole] <= start - size)

        result.reverse()  # Reverse the result to match the original query order

        return result