import math
import time 
from player import HumanPlayer, RandomComputerPLayer, SmartComputerPlayer


class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)] # we will use a single list to represent 3x3 board 
        self.current_winner = None # keeps track of winner

    def print_board(self):
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print("| " + " | " .join(row) + " |")
    
    @staticmethod
    def print_board_nums():
        # 0 | 1 | 2  etc tells us what number corresponds to what box
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in number_board:
            print("| " + " | " .join(row) + " |")
    
    def availabe_moves(self):
        return [i for i, spot in enumerate(self.board) if spot ==" "]
        
        # the above one line code can also be written as: 
        # moves = []
        # for (i, spot) in enumerate(self.board):
        #     # ['x', 'x', 'o'] --> [(0, 'x'), (1, 'x'), (2, 'o')]  --> i.e return a tupple
        #     if spot == " ":  # if spot = space we know it's an empty space and we append the move
        #         moves.append(i)
        # return moves

    def empty_squares(self):
        return ' ' in self.board

    def num_empty_squares(self):
        return self.board.count(" ")

    def make_move(self, square, letter):
        # if valid move, then make the move (assign square to letter)
        # then return true. if invalid, return false
        if self.board[square] == " ":
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False 

    def winner(self, square, letter):
        # winner if 3 in a row anywhere. We have to check all of these!
        # first let's check the row 
        row_ind = square // 3
        row = self.board[row_ind*3 : (row_ind + 1)*3]
        if all([spot == letter for spot in row]):
            return True 

        #check column 
        col_ind = square % 3
        column = [self.board[col_ind + i*3] for i in range(3)]
        if all([spot == letter for spot in column]):
            return True

        # check diagonals
        # but only if the square is an even number (0, 2, 4, 6, 8)
        # these are the only moves possible to win a diagonal 
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0,4,8]]
            if all([spot == letter for spot in diagonal1]):
                return True

            diagonal2 = [self.board[i] for i in [2,4,6]]
            if all([spot == letter for spot in diagonal2]):
               return True
   
        return False #if all fails 


    def available_moves(self):
        return [i for i, x in enumerate(self.board) if x == " "]


def play(game, x_player, o_player, print_game=True):
    if print_game:
        game.print_board_nums()

    letter = "X" #starting letter
    # iterate while the game still has empty squares
    # we don't have to worry about wininer because we'll just return that breaks the loop
    while game.empty_squares():
        # get the move fromt the appropriate player 
        if letter == "O":
            square = o_player.get_move(game)
        else: square = x_player.get_move(game)

        #let's define a function to make a move!
        if game.make_move(square, letter):
            if print_game:
                print(letter + f" makes a move to square {square}")
                game.print_board()
                print(" ") #just empty line

            if game.current_winner:
                if print_game:
                    print(letter + " wins!")
                return letter 

            # after we made our move, we nee to alternate letters
            letter = "O" if letter == "X" else "X" # switches player
            # if letter == "X":         i.e if old/current letter is X then switch to O
            #     letter = "O"
            # else:
            #    letter = "X" 

            if print_game:
                time.sleep(0.8)

    if print_game:
        print("It's a tie!")

# for human v/s comp:  
if __name__ == "__main__":
    x_player = HumanPlayer("X")
    o_player = SmartComputerPlayer("O")
    t = TicTacToe()
    play(t, x_player, o_player, print_game=True)


# # for smartcomp v/s randomcomp for n interatioins:
# if __name__ == "__main__":
#     x_wins = 0
#     o_wins = 0
#     ties = 0
#     tic = time.time()
#     for _ in range(1000):
#         x_player = SmartComputerPlayer("X")     #keep smartcompplayer as x cause the minimax algo is written for X player 
#         o_player = RandomComputerPLayer("O")
#         t = TicTacToe()
#         result = play(t, x_player, o_player, print_game=False)
#         if result == "X":
#             x_wins += 1
#         elif result == "0":
#             o_wins += 1
#         else:
#              ties += 1

#     tok = time.time()
#     timeTaken = tok - tic 

#     print(f"After 1000 iterations, we see {x_wins} X wins, {o_wins} O wins and {ties} ties and takes {timeTaken} seconds")
    



    


