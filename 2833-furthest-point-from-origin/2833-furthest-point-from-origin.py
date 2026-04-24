class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        return len(moves) - (min(moves.count("L"), moves.count("R")) * 2)