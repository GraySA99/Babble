
from token import Token

class Executor:

    def __init__(self, program):
        self.program = program
    
    def execute(self, tokens):
        
        token = tokens[0]

        if token.token == Token.ReservedWords.PRINT:
            print(self.execute(tokens[1:]))
        elif token.token == Token.NUMBER:
            if len(tokens)==1:
                return int(token.value)
            elif tokens[1].token == Token.ReservedWords.PLUS:
                return int(token.value) + self.execute(tokens[2:])
            elif tokens[1].token == Token.ReservedWords.MINUS:
                return int(token.value) - self.execute(tokens[2:])
            elif tokens[1].token == Token.ReservedWords.TIMES:
                return int(token.value) * self.execute(tokens[2:])
            elif tokens[1].token == Token.ReservedWords.DIVIDE:
                return int(token.value) / self.execute(tokens[2:])
            else:
                return int(token.value)
        elif token.token == Token.STRING:
            if len(tokens)==1:
                return token.value
            elif tokens[1].token == Token.ReservedWords.PLUS:
                return token.value + self.execute(tokens[2:])
        elif token.token == Token.VAR:
            if len(tokens)==1:
                return self.program.get_variable(token.value)
            elif tokens[1].token == Token.ReservedWords.IS:
                self.program.set_variable(token.label, self.execute(tokens[2:]))
            else:
                return self.program.get_variable(token.value)


