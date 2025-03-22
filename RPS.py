# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.

import random
from collections import Counter

class BasePlayer():
    def __init__(self):
        self.opponent_history = [] # Keeps track of the opponent's moves
        self.current_play = None

    def update(self, prev_play):
        if prev_play:
            self.opponent_history.append(prev_play)

    def predict(self):
        raise NotImplementedError("Subclasses must implement predict()")