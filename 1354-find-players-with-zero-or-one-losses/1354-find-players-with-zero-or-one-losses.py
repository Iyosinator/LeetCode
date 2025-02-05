from collections import defaultdict

class Solution:
    def findWinners(self, matches):
        loss_count = defaultdict(int)
        players = set()

        for winner, loser in matches:
            players.add(winner)
            players.add(loser)
            loss_count[loser] += 1

        no_loss = sorted([player for player in players if loss_count[player] == 0])
        one_loss = sorted([player for player in players if loss_count[player] == 1])

        return [no_loss, one_loss]
