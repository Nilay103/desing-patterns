
class Player:
    """_summary_
    """
    def __init__(self, name) -> None:
        self.name: str = name
        self.operator: int

    def get_name(self) -> str:
        return self.name

    def get_operator(self) -> int:
        return self.operator

    def set_operator(self, operator: int) -> None:
        self.operator = operator


class Board:
    """_summary_
    """
    def __init__(self, n) -> None:
        self.n = n
        self._matrix = [[0 for i in range(n)] for j in range(n)]
        self._raw_sum = [0 for i in range(n)]
        self._col_sum = [0 for i in range(n)]
        self._dia_sum = [0 for i in range(n)]
        self._rev_dia_sum = [0 for i in range(n)]


class Move(Board):
    def __init__(self, raw, col) -> None:
        self._raw = raw
        self._col = col

    def is_valid(self) -> bool:
        """_summary_

        Returns:
            bool: _description_
        """
        return (
            self._raw > 0 and 
            self._raw < 3 and 
            self._col > 0 and 
            self._col < 3 and 
            self._matrix[self._raw][self._col] != 0
        )


class Game(Board):
    def __init__(self, name1: str, name2: str) -> None:
        super().__init__()
        self.player1 = Player(name=name1)
        self.player2 = Player(name=name2)

        self.history = []
        self.__winner = None

    def __set_winner(self, player: Player):
        """_summary_

        Args:
            player (Player): _description_
        """
        self.__winner = player

    def get_winner(self) -> str:
        """_summary_

        Returns:
            str: _description_
        """
        return self.__winner.get_name()

    def is_winner(self) -> bool:
        """Checks in O(1) time complexity and O(n) space complexity

        Returns:
            bool: _description_
        """
        return (
            sum(self._col_sum) == abs(self.n) or
            sum(self._raw_sum) == abs(self.n) or
            sum(self._dia_sum) == abs(self.n) or
            sum(self._rev_dia_sum) == abs(self.n)
        )

    def make_move(self, move: Move, player: Player):
        """_summary_

        Args:
            move (Move): _description_
            player (Player): _description_

        Raises:
            Exception: _description_
        """
        if not move.is_valid():
            raise Exception

        self._matrix[move._raw][move._col] = player.get_operator()
        self._raw_sum[move._raw] += player.get_operator()
        self._col_sum[move._col] += player.get_operator()
        if move._raw == move._col:
            self._dia_sum[move._raw][move._col] += player.get_operator()

        if move._raw == self.n - move._col:
            self._rev_sum[move._raw][move._col] += player.get_operator()
        if self.is_winner():
            self.__set_winner(player=player)


if __name__ == "__main__":
    pass
