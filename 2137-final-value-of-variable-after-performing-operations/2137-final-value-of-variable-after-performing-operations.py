class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        counter = 0
        for operation in operations:
            if operation in {"X++", "++X"}:
                counter += 1
            elif operation in {"X--", "--X"}:
                counter -= 1
        return counter
