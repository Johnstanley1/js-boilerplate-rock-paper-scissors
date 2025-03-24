# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.

import random
from collections import Counter

class BasePlayer():
    def __init__(self):
        pass
     
    def reset_state(self):
        self.opponent_history = [] # Keeps track of the opponent's moves
        self.player_history = []
        self.bot_name = None
        self.counter = 0
        self.play_order = [{
              "RR": 0,
              "RP": 0,
              "RS": 0,
              "PR": 0,
              "PP": 0,
              "PS": 0,
              "SR": 0,
              "SP": 0,
              "SS": 0,
          }]

    def predict(self):
        raise NotImplementedError("Subclasses must implement predict()")
    

class DetectBot(BasePlayer):
    def __init__(self):
        super().__init__()
        self.bots = [
            Quincy(),
            Mrugesh(),
            Kris(),
            Abbey()
        ]
        self.bot_name = self.bots
        
    def detect_bot(self, prev_play):  
        if prev_play == "": # check if opponent is
            super().reset_state()

        # update states
        self.counter += 1
        self.opponent_history.append(prev_play)

        # Check opponents move patterns
        if self.counter < 5:
            player_move = 'R'
            self.player_history.append(player_move)
            return player_move
        
        if not self.bot_name:
            if len(self.opponent_history)>= 6:
                if self.opponent_history[0:6] == ["", "R", "R", "P", "P", "S"]:
                    self.bot_name = self.bots[0]
                elif self.opponent_history[0:6] == ["", "R", "R", "R", "R", "S"]:
                    self.bot_name = self.bots[1]
                elif self.opponent_history[0:6] == ["", "P", "R", "R", "R", "R"]:
                    self.bot_name = self.bots[2]
                elif self.opponent_history[0:6] == ['', 'P', 'P', 'R', 'R', 'R']:
                    self.bot_name = self.bots[3]

    
    def predict(self, prev_play):
        # choose strategy according to opponent
        if self.bot_name == self.bots[0]:
            player_move = self.bot_name.predict(prev_play)
        elif self.bot_name == self.bots[1]:
            player_move = self.bot_name.predict(prev_play)
        elif self.bot_name == self.bots[2]:
            player_move = self.bot_name.predict(prev_play)
        elif self.bot_name == self.bots[3]:
            player_move = self.bot_name.predict(prev_play)
        else:
            return random.choice(['R', 'P', 'S'])  # default strategy

        self.player_history.append(player_move)
        
        return player_move
            

class Quincy(BasePlayer):
    def __init__(self):
        super().__init__()

    def predict(self):
        choices = ["R", "P", "S", "S", "R"]
        return choices[self.counter % 5]


class Mrugesh(BasePlayer):
    def __init__(self):
        super().__init__()

    def predict(self):
        op

class Kris(BasePlayer):
    def __init__(self):
        super().__init__()

class Abbey(BasePlayer):
    def __init__(self):
        super().__init__()


bot = DetectBot()

def player(prev_play):
    return bot.predict(prev_play)