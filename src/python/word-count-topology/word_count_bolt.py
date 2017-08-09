from collections import Counter

# Import Bolt type from heronpy
from heronpy import Bolt

# Word Count Bolt that inherits from heron Bolt
class WordCountBolt(Bolt):

    # Important : Define output field tags for the Bolt
    outputs = ['word', 'count']

    def initialize(self, config, context):
        # A log context is provided in the context of the spout
        self.log("Initializing WordCountBolt...")
        # We initialize a python collections Counter for recording hte word count
        self.counter = Counter()

    # Process Periodic tick tuple to log and emit output
    def process_tick(self, tup):
        # If tuple type is tick type a special periodic interval entry generate logs and emit sequence
        for value, count in self.counter.most_common():
            self.log("Emitting a count of ({}) for word ({})".format(value, count))
            self.emit([value, count])

    # Process Word stream to aggregate to word count
    def process(self, tup):
        word = tup.values[0]
        self.counter[word] += 1
