from typing import List


class GameEntry:
    """Reporesents one entry of a list of high scores."""

    def __init__(self, name, score):
        self._name = name
        self._score = score

    def get_name(self):
        return self._name

    def get_score(self):
        return self._score

    def __str__(self):
        return f"({self._name}, {self._score})"


class ScoreBoard:
    """Fixed-length sequence of high scores in nondepreciating order."""

    def __init__(self, capacity=10):
        """Initialize scoreboard with given maximum capacity."""
        self._board: List[GameEntry] = [] * capacity
        self._n = 0

    def __getitem__(self, item):
        """Return entry at index k"""
        return self._board[item]

    def __str__(self):
        """Return string representation of the high score list."""
        return '\n'.join(str(i) for i in self._board)

    def add(self, entry):
        """Consider adding entry to high scores."""
        score = entry.get_score()

        good = self._n < len(self._board) or score > self._board[-1].get_score()

        if good:
            if self._n < len(self._board):
                self._n += 1

            j = self._n - 1

            while j > 0 and self._board[j - 1].get_score() < score:
                self._board[j] = self._board[j - 1]
                j -= 1
            self._board[j] = entry
