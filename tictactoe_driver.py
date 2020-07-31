# Tic Tac Toe driver module

from tictactoe_functions import TicTacToeGame

while True:
    emptyBoard = [' '] * 10
    ttt = TicTacToeGame(emptyBoard)
    letter1, letter2 = ttt.inputPlayerLetter()
    turn = 1
    ttt.drawBoard()
    gameIsPlaying = True
    ttt.initialBoard()

    while gameIsPlaying:
        if turn == 1:
            print("Player 1's turn.")
            move = ttt.getPlayerMove()
            ttt.makeMove(letter1, move)
            ttt.drawBoard()

            if ttt.isWinner(letter1):
                print('Player 1 has won the game!')
                gameIsPlaying = False
            else:
                if ttt.isBoardFull():
                    print('The game is a tie!')
                    break
                else:
                    turn = 2

        else:
            print("Player 2's turn.")
            move = ttt.getPlayerMove()
            ttt.makeMove(letter2, move)
            ttt.drawBoard()

            if ttt.isWinner(letter2):
                print('Player 2 has won the game!')
                gameIsPlaying = False
            else:
                if ttt.isBoardFull():
                    print('The game is a tie!')
                    break
                else:
                    turn = 1

    if not ttt.playAgain():
        break