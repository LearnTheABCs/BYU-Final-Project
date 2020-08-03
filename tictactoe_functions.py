# Tic Tac Toe class and functions

class TicTacToeGame:
    def __init__(self, board):
        self.board = board

    def initialBoard(self):

        # Text Picture of the location of the numbers of the board

        print("""
         7 | 8 | 9
        -----------
         4 | 5 | 6
        -----------
         1 | 2 | 3 
        """)

    def drawBoard(self):
        # This function prints out the board that it was passed.

        # "board" is a list of 10 strings representing the board (ignore index 0)
        #print('   |   |')
        print(' ' + self.board[7] + ' | ' + self.board[8] + ' | ' + self.board[9])
        #print('   |   |')
        print('---+---+---')
        #print('   |   |')
        print(' ' + self.board[4] + ' | ' + self.board[5] + ' | ' + self.board[6])
        #print('   |   |')
        print('---+---+---')
        #print('   |   |')
        print(' ' + self.board[1] + ' | ' + self.board[2] + ' | ' + self.board[3])
        #print('   |   |')

    def inputPlayerLetter(self):
        # Lets player 1 type which letter they want to be.
        # Returns a list with player 1's letter as the first item, and player 2's letter as the second.
        letter = ''
        while not (letter == 'X' or letter == 'O'):
            print('PLAYER 1, CHOOSE X OR O')
            letter = input().upper()

        # the first element in the tuple is player 1's letter, the second is player 2's letter.
        if letter == 'X':
            return ['X', 'O']
        else:
            return ['O', 'X']

    def playAgain(self):
        # This function returns True if the player wants to play again, otherwise it returns False.
        print('Do you want to play again? (yes or no)')
        return input().lower().startswith('y')

    def makeMove(self, letter, move):
        self.board[move] = letter

    def isWinner(self, le):
        # Given a board and a player's letter, this function returns True if that player has won.
        # We use bo instead of board and le instead of letter so we don't have to type as much.
        return ((self.board[7] == le and self.board[8] == le and self.board[9] == le) or # across the top
        (self.board[4] == le and self.board[5] == le and self.board[6] == le) or # across the middle
        (self.board[1] == le and self.board[2] == le and self.board[3] == le) or # across the bottom
        (self.board[7] == le and self.board[4] == le and self.board[1] == le) or # down the left side
        (self.board[8] == le and self.board[5] == le and self.board[2] == le) or # down the middle
        (self.board[9] == le and self.board[6] == le and self.board[3] == le) or # down the right side
        (self.board[7] == le and self.board[5] == le and self.board[3] == le) or # diagonal
        (self.board[9] == le and self.board[5] == le and self.board[1] == le)) # diagonal

    def isSpaceFree(self, move):
        # Return true if the passed move is free on the passed board.
        return self.board[move] == ' '

    def getPlayerMove(self):
        # Let the player type in his move.
        move = ' '
        while move not in '1 2 3 4 5 6 7 8 9'.split() or not self.isSpaceFree(int(move)):
            print('Choose a number (1-9)')
            move = input()
        return int(move)

    def isBoardFull(self):
        # Return True if every space on the board has been taken. Otherwise return False.
        for i in range(1, 10):
            if self.isSpaceFree(i):
                return False
        return True