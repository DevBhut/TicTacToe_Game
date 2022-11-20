import math 
import random

class Player:
    def __init__(self, letter):
        # letter is x or o
        self.letter = letter

    # we want all players to get their next move given a game
    def get_move(self, game):
        pass


class RandomComputerPLayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        square = random.choice(game.available_moves())
        return square 


class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        valid_square = False
        val = None
        while not valid_square:
            square = input(self.letter + "'s turn. Input move (0-8):") 
            # we're going to check that this is a correct value by trying to cast
            # it to an integer, and if it's not, then we say its invalid
            # if that spot is not available on the board, we also say its invalid
            try:
                val = int(square)
                if val not in game.availabe_moves():
                    raise ValueError       # 'raise' Keyword is used to raise exceptions or errors
                valid_square = True #if these are successful, then yay!
            except ValueError:
                print("Invalid square. Try again.")
        return val 


class SmartComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        if len(game.availabe_moves()) == 9:
            square = random.choice(game.available_moves())
        else:
            # get the square based off the minimax algorithm 
            square = self.minimax(game, self.letter)["position"]
        return square 

    def minimax(self, state, player):
        max_player = self.letter     # yourself
        other_player = "X" if player == "O" else "O"

        # first we have to check if the previous move is a winner
        if state.current_winner == other_player:
            # we should return position and score because we need to keep track
            # of the score for minimax to work

            return {"position": None, 
                    "score": 1*(state.num_empty_squares() + 1) if other_player == max_player 
                 else -1*(state.num_empty_squares() + 1) }

        elif not state.empty_squares():                    # no empty squares
            return {"position": None, "score": 0}
        
        if player == max_player:
            best = {"position": None, "score": -math.inf}   # each score should maximize
        else:
            best = {"position": None, "score": math.inf}    # each score should minimize 

        for possible_move in state.available_moves():
            # step 1: make a move, try that spot
            state.make_move(possible_move, player)

            # step 2: recurse using minimax to simulate a game after making that move 
            sim_score = self.minimax(state, other_player)   # now, we alternate players

            # step 3: undo move
            state.board[possible_move] = " "
            state.current_winner = None
            sim_score["position"] = possible_move           # this represents the most optimal next move

            if player == max_player:   # X is max player 
                if sim_score["score"] > best["score"]:
                    best = sim_score
            else:
                if sim_score["score"] < best["score"]:
                    best = sim_score
        return best 


        
        