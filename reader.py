
from token import Token

class Reader:

    def __init__(self, program, filename):

        self.filename = filename
        self.program = program
        self.statement = []
    
    def read(self):

        with open(self.filename, 'r') as file_in:

            line = file_in.readline()
            while line:

                token = ''
                in_string = False
                indents = 0
                
                if line.strip() != '':

                    while line[0] == ' ':
                        indents += 1
                        if self.statement[-1].token == Token.UNINDENT:
                            self.statement = self.statement[:-1]
                        else:
                            self.statement.append(Token(Token.INDENT))
                        line = line[4:]

                    for (i, char) in enumerate(line.rstrip()):
                        
                        # print(f'"{token}" "{i}" "{char}" "{len(self.statement)}" "{in_string}"')

                        if not in_string:
                            if char == '<' and line[i+1] == '>':
                                break
                            elif char == '"':
                                in_string = True
                            elif (char == ' ' or i == len(line)) and token != '':
                                if token in self.program.reserved_words:
                                    self.statement.append(Token(token))
                                    token = ''
                                elif token.isnumeric():
                                    self.statement.append(Token(Token.NUMBER, token))
                                    token = ''
                                else:
                                    self.statement.append(Token(Token.VAR, token))
                                    token = ''
                            else:
                                if char != ' ':
                                    token += char
                        else:
                            if char == '"':
                                in_string = False
                                self.statement.append(Token(Token.STRING, token))
                                token = ''
                            else:
                                token += char
                    if token != '':
                        if token in self.program.reserved_words:
                            self.statement.append(Token(token))
                            token = ''
                        elif token.isnumeric():
                            self.statement.append(Token(Token.NUMBER, token))
                            token = ''
                        else:
                            self.statement.append(Token(Token.VAR, token))
                            token = ''
                for i in range(0, indents):
                    self.statement.append(Token(Token.UNINDENT))
                line = file_in.readline()

