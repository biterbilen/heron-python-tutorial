from time import sleep
import random

# Import spout type from heronpy
from heronpy import Spout

# Helper method to provide continuous random iteration of a list of times
def random_cycle(ls):
    local_ls = ls[:] # Local defensive copy
    while True:
        random.shuffle(local_ls)
        for e in local_ls:
            yield e

# Random sentence generator Spout class that inherits from heron Spout
class RandomSentenceSpout(Spout):

    # Important : Define output field tags for the Spout
    outputs = ['sentence']

    # Spout initialization
    def initialize(self, config, context):
        # A log context is provided in the context of the spout
        self.log("Initializing Random Sentence Spout...")

        # A collection of sentences to random iterate over
        self.sentences = random_cycle([
            "the cow jumped over the moon",
            "an apple a day keeps the doctor away",
            "four score and seven years ago",
            "snow white and the seven dwarfs",
            "i am at two with nature"
        ])

    # Generate next tuple sequence for this spout
    def next_tuple(self):
        sleep(0.05) # Sleep for 50 ms to throttle Spout
        sentence = next(self.sentences) # Get next random sentence
        self.emit([sentence]) # Emit Sentence to go to next phase in the topology
