class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        n = len(deck)
        queue = deque()

        for i in range(n):
            queue.append(i)

        deck.sort()
        res = [0] * n
        for card in deck:
            res[queue.popleft()] = card
            if queue:
                queue.append(queue.popleft())
        return res




        