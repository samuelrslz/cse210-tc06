import random

class Board:
    """A designated playing surface. The responsibility of Board is to keep track of the pieces in play.
    
    Stereotype: 
        Information Holder

    Attributes:
        _piles (list): The number of piles of stones.
    """
    def __init__(self):
        """The class constructor.
        
        Args:
            self (Board): an instance of Board.
        """
        self._items = {}

    def apply(self, move, name):
        """Applies the given move to the playing surface. In this case, that 
        means removing a number of stones from a pile.
        
        Args:
            self (Board): an instance of Board.
            move (Move): The move to apply.
        """
        guess = move.get_guess()
        print(self._items[name][0])
        self._items[name][1] = guess
        self._items[name][2] = ""

        for index, char in enumerate(guess):
            if char == self._items[name][0][index]:
                self._items[name][2] += "x"
            elif char in self._items[name][0]:
                self._items[name][2] += "o"
            else:
                self._items[name][2] += "*"

    
    def is_empty(self, name):
        """Determines if all the stones have been removed from the board.
        
        Args:
            self (Board): an instance of Board.

        Returns:
            boolean: True if the board has no stones on it; false if otherwise.
        """
        guess = self._items[name][1]
        code = self._items[name][0]
        return guess == code

    def to_string(self):
        """Converts the board data to its string representation.

        Args:
           self (Board): an instance of Board.

        Returns:
            string: A representation of the current board.
        """ 
        text =  "\n--------------------"
        for key, value in (self._items.items()):
            text += (f"\nPlayer {key}: {value[1]}, {value[2]}")
        text += "\n--------------------"
        return text

    def set_items(self, name, guess):
        self._items[name][1] = guess

    def _prepare(self, player):
        """Sets up the board with an entry for each player.
        
        Args:
            self (Board): an instance of Board.
        """
        name = player.get_name()
        code = str(random.randint(1000, 10000))
        guess = "----"
        hint = "****"
        self._items[name] = [code, guess, hint]

# board = Board()

# print(board._piles)