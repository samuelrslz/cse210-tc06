import random

class Board:
    """A designated playing surface. The responsibility of Board is to keep track of the player's codes.
    
    Stereotype: 
        Information Holder

    Attributes:
        _items (dictionary): The code, guess, and hint.
    """
    def __init__(self):
        """The class constructor.
        
        Args:
            self (Board): an instance of Board.
        """
        self._items = {}

    def apply(self, guess, name):
        """Applies the given move to the playing surface. In this case, comparing the guess
        with the code.
        
        Args:
            self (Board): an instance of Board.
            guess (Move): The move to apply.
            name (player): The name of the player.
        """
        guess = guess.get_guess()
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
        """Determines if guess is correct.
        
        Args:
            self (Board): an instance of Board.

        Returns:
            boolean: True if guess is correct.
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

    def _prepare(self, player):
        """Sets up the board with an entry for each player.
        
        Args:
            self (Board): an instance of Board.
        """
        name = player.get_name()
        code = str(random.randint(10000, 100000))
        guess = "-----"
        hint = "*****"
        self._items[name] = [code, guess, hint]