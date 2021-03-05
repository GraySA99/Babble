
from token import Token

class Executor:

    def __init__(self, program):
        self.program = program
        self.skip = []
    
    def execute(self, reader):
        
        token = reader.statement.pop(0)

        # print(f'Token -> {token.token} {token.value}')

        if len(self.skip) > 0 and self.skip[0]:
            return None if len(reader.statement)==0 else self.execute(reader)

        if token.token == Token.INDENT:
            self.execute(reader)
        if token.token == Token.UNINDENT:
            self.skip = self.skip[:-1]
        elif token.token == Token.ReservedWords.IF:
            self.skip.append(self.execute(reader) != 'true')
        elif token.token == Token.ReservedWords.PRINT:
            print(self.execute(reader))
        elif token.token == Token.BOOL:
            if len(reader.statement)==0:
                return 'true' if token.value else 'false'
            else:
                return 'true' if token.value else 'false'
        elif token.token == Token.NUMBER:
            if len(reader.statement)==0:
                return int(token.value)
            elif reader.statement[0].token == Token.ReservedWords.PLUS:
                reader.statement = reader.statement[1:]
                return int(token.value) + self.execute(reader)
            elif reader.statement[0].token == Token.ReservedWords.MINUS:
                reader.statement = reader.statement[1:]
                return int(token.value) - self.execute(reader)
            elif reader.statement[0].token == Token.ReservedWords.TIMES:
                reader.statement = reader.statement[1:]
                return int(token.value) * self.execute(reader)
            elif reader.statement[0].token == Token.ReservedWords.DIVIDE:
                reader.statement = reader.statement[1:]
                return int(token.value) / self.execute(reader)
            elif reader.statement[0].token == Token.ReservedWords.EQUALS:
                reader.statement = reader.statement[1:]
                nextVal = self.execute(reader)
                reader.statement = [Token(Token.BOOL, int(token.value) == nextVal)] + reader.statement
                return self.execute(reader)
            elif reader.statement[0].token == Token.ReservedWords.GREATER:
                reader.statement = reader.statement[1:]
                nextVal = self.execute(reader)
                reader.statement = [Token(Token.BOOL, int(token.value) > nextVal)] + reader.statement
                return self.execute(reader)
            elif reader.statement[0].token == Token.ReservedWords.LESS:
                reader.statement = [Token(Token.BOOL, int(token.value) < self.execute(reader))] + reader.statement[1:]
                return self.execute(reader)
            else:
                return int(token.value)
        elif token.token == Token.STRING:
            if len(reader.statement)==0:
                return token.value
            elif reader.statement[0].token == Token.ReservedWords.PLUS:
                reader.statement = reader.statement[1:]
                return token.value + self.execute(reader)
            else:
                return token.value
        elif token.token == Token.VAR:
            if len(reader.statement)==0:
                return self.program.get_variable(token.value)
            elif reader.statement[0].token == Token.ReservedWords.IS:
                reader.statement = reader.statement[1:]
                self.program.set_variable(token.value, self.execute(reader))
            else:
                new_token = Token.STRING
                if type(self.program.get_variable(token.value)) is int:
                    new_token = Token.NUMBER
                reader.statement = [Token(new_token, self.program.get_variable(token.value))] + reader.statement
                return self.execute(reader)
                


