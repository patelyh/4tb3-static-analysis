import collections
from organized_dict import organized_dict

class nested_for_optimizer:
    code_dict = organized_dict(collections.OrderedDict())  # dictionary of line : code

    def __init__(self, code_dict):
        self.code_dict = code_dict

    def search_for_optimization(self):
        for keys in self.code_dict:
            if ('for' in self.code_dict[keys]):
                # Found an if statement - now check if the next input stream is an else
                next_tuple = (self.code_dict.next_key(self.code_dict, keys))
                if ('for' in next_tuple[1]):
                    print("Nested for loop can be optimized on line: " + str(keys) + " - " + str(self.code_dict[keys]))
                    break   #Found nested for loop - break out to avoid reading another for loop that is not nested after