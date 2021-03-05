
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
                
                if line.strip() != '':
                    for (i, char) in enumerate(line.rstrip()):
                        
                        # print(f'"{token}" "{i}" "{char}" "{len(self.statement)}" "{in_string}"')

                        if not in_string:
                            if char == '<' and line[i+1] == '>':
                                break
                            elif char == '"':
                                in_string = True
                            elif char == ' ' or i == len(line):
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
                line = file_in.readline()

