# Import Bolt type from heronpy
from heronpy import Bolt

# Sentence Splitting Bolt class that inherits from heron Bolt
class SplitSentenceBolt(Bolt):

    # Important : Define output field tags for the Bolt
    outputs = ['word']

    def initialize(self, config, context):
        # A log context is provided in the context of the spout
        self.log("Initializing SplitSentenceBolt...")

    # Process incoming tuple and emit output
    def process(self, tup):
        # Accept a sentence string and spit into words via space delimiter
        for word in tup.values[0].split(" "):
            # Emit individual words to next phase of the topology
            self.emit([word])
