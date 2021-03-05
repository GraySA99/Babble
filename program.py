
from reader import Reader
from executor import Executor
from token import Token

class Program:

    def __init__(self, filename):
        self.variables = []
        self.functions = []
        self.reserved_words = [
            Token.ReservedWords.PRINT,
            Token.ReservedWords.PLUS,
            Token.ReservedWords.MINUS,
            Token.ReservedWords.TIMES,
            Token.ReservedWords.DIVIDE,
            Token.ReservedWords.FUNCTION,
            Token.ReservedWords.IS,
            Token.ReservedWords.IF,
            Token.ReservedWords.EQUALS,
            Token.ReservedWords.GREATER,
            Token.ReservedWords.LESS
        ]
        self.reader = Reader(self, filename)
        self.executor = Executor(self)

        self.skip_line = False
    
    def run(self):
        self.reader.read()
        while len(self.reader.statement) > 0:
            self.executor.execute(self.reader)

    def set_variable(self, label, value=None):
        
        for (i, var) in enumerate(self.variables):
            if var.label == label:
                self.variables[i].value = value
                return
        self.variables.append(Variable(label, value))

    def get_variable(self, label):

        for var in self.variables:
            if var.label == label:
                return var.value
        return None

class Variable:

    def __init__(self, label, value):
        self.label = label
        self.value = value

class Function:

    def __init__(self, label, params):
        self.label = label
        self.params = []
        self.returnVal = None
        for lab in params:
            self.params.append(Variable(lab, None))
