import operator

class TableElement:
    """
    A wrapper for all the supported types in a table.
    The possible types include:
        - strings
        - integers
        - floats
    The wrapper allows for the automatic comparison of string, integral, and floating
    types, even when the other operand is a string.
    """

    def __init__(self, string):
        self.value = self.convert(string)

    @staticmethod
    def convert(string):
        """ Try to convert the string to any of the supported types in a table. """
        # Converting a textual float to an int is invalid, but converting a float
        # to an int is valid. We skip floats to avoid discarding the decimals.
        if not isinstance(string, float):
            try:
                return int(string)
            except:
                pass
        try:
            return float(string)
        except:
            pass
        return string
    
    def __str__(self):
        return str(self.value)
    
    def __repr__(self):
        return str(self.value)

    def compare(self, comparator, other):
        return comparator(self.value, self.convert(other))
    
    def __lt__(self, other):
        return self.compare(operator.lt, other)
    
    def __le__(self, other):
        return self.compare(operator.le, other)
    
    def __eq__(self, other):
        return self.compare(operator.eq, other)
    
    def __ne__(self, other):
        return self.compare(operator.ne, other)
    
    def __ge__(self, other):
        return self.compare(operator.ge, other)
    
    def __gt__(self, other):
        return self.compare(operator.gt, other)
