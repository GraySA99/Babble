
from token import Token

class Executor:

    def __init__(self, program):
        self.program = program
    
    def execute(self, tokens):
        
        token = tokens.pop(0)

        if token.token == Token.ReservedWords.PRINT:
            print(self.execute(tokens))
        elif token.token == Token.NUMBER:
            if len(tokens)==0:
                return int(token.value)
            elif tokens[0].token == Token.ReservedWords.PLUS:
                return int(token.value) + self.execute(tokens[1:])
            elif tokens[0].token == Token.ReservedWords.MINUS:
                return int(token.value) - self.execute(tokens[1:])
            elif tokens[0].token == Token.ReservedWords.TIMES:
                return int(token.value) * self.execute(tokens[1:])
            elif tokens[0].token == Token.ReservedWords.DIVIDE:
                return int(token.value) / self.execute(tokens[1:])
            else:
                return int(token.value)
        elif token.token == Token.STRING:
            if len(tokens)==0:
                return token.value
            elif tokens[0].token == Token.ReservedWords.PLUS:
                return token.value + self.execute(tokens[1:])
        elif token.token == Token.VAR:
            if len(tokens)==0:
                return self.program.get_variable(token.value)
            elif tokens[0].token == Token.ReservedWords.IS:
                self.program.set_variable(token.value, self.execute(tokens[1:]))
            else:
                new_token = Token.STRING
                if type(self.program.get_variable(token.value)) is int:
                    new_token = Token.NUMBER
                return self.execute([Token(new_token, self.program.get_variable(token.value))] + tokens)
                


