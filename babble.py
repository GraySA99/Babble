
import sys

class Token:

    IS = 'is'
    PLUS = 'plus'
    MINUS = 'minus'
    TIMES = 'times'
    DIVIDE = 'divide'
    PRINT = 'print'


    VAR = 'var'
    NUMBER = 'num'
    STRING = 'str'

    PROTECTED_WORDS = [
        IS,
        PLUS,
        MINUS,
        TIMES,
        DIVIDE,
        PRINT,
    ]

class not_sure:

    def __init__(self, filename):
        self.filename = filename
        self.variables = {}
    
    def interpret(self):
        
        with open(self.filename, 'r') as file_in:

            lines = []
            line = file_in.readline()
            while line:
                if line.strip() != '':
                    lines.append(line.strip())
                line = file_in.readline()
        
        self.compile(lines)
    
    def compile(self, lines):

        for line in lines:
            tokens = line.split(' ')

            statement = []
            for token in tokens:
                if token != '':
                    if token in Token.PROTECTED_WORDS:
                        statement.append({'value': token, 'token': token})
                    elif token not in Token.PROTECTED_WORDS:
                        if token.isnumeric():
                            statement.append({'value': int(token), 'token': Token.NUMBER})
                        elif token[0] == '"' and token[-1] == '"':
                            statement.append({'value': token[1:][:-1], 'token': Token.STRING})
                        else:
                            statement.append({'value': token, 'token': Token.VAR})
            self.execute(statement)

    def execute(self, statement):

        if statement[0]['token'] == Token.PRINT:
            print(self.execute(statement[1:]))
        if statement[0]['token'] == Token.VAR:
            if len(statement)>1 and statement[1]['token'] == Token.IS:
                self.variables[statement[0]['value']] = self.execute(statement[2:])
            elif len(statement) == 1:
                return self.variables[statement[0]['value']]
            else: 
                statement[0]['value'] = self.variables[statement[0]['value']]
                if type(statement[0]['value']) != str:
                    statement[0]['token'] = Token.NUMBER
                else:
                    statement[0]['token'] = Token.STRING
                return self.execute(statement)           
        elif statement[0]['token'] == Token.NUMBER:
            if len(statement) == 1:
                return statement[0]['value']
            elif statement[1]['token'] == Token.PLUS:
                return statement[0]['value'] + self.execute(statement[2:])
            elif statement[1]['token'] == Token.MINUS:
                return statement[0]['value'] - self.execute(statement[2:]) 
            elif statement[1]['token'] == Token.TIMES:
                return statement[0]['value'] * self.execute(statement[2:])
            elif statement[1]['token'] == Token.DIVIDE:
                return statement[0]['value'] / self.execute(statement[2:])
        elif statement[0]['token'] == Token.STRING:
            if len(statement) == 1:
                return statement[0]['value']
            elif statement[1]['token'] == Token.PLUS:
                return statement[0]['value'] + self.execute(statement[2:])







if __name__ == '__main__':
    
    try:
        print(sys.argv[1])
    except IndexError:
        print('Please enter a Babble file')
        sys.exit(-1)
    
    ns = not_sure(sys.argv[1])
    ns.interpret()