
import sys

class Token:

    # Protected Words
    IS = 'is'
    PLUS = 'plus'
    MINUS = 'minus'
    TIMES = 'times'
    DIVIDE = 'divide'
    PRINT = 'print'
    FUNCTION = 'function'
    RETURN = 'return'

    # Data Types
    VAR = 'var'
    NUMBER = 'num'
    STRING = 'str'
    PARAM = 'param'

    PROTECTED_WORDS = [
        IS,
        PLUS,
        MINUS,
        TIMES,
        DIVIDE,
        PRINT,
        FUNCTION,
        RETURN,
    ]

class not_sure:

    def __init__(self, filename):
        self.filename = filename
        self.variables = {}
        self.functions = {}
    
    def interpret(self):
        
        with open(self.filename, 'r') as file_in:

            lines = []
            line = file_in.readline()
            while line:
                if line.strip() != '':
                    lines.append(line.rstrip())
                line = file_in.readline()
        
        self.compile(lines)
    
    def compile(self, lines):

        building_function = False
        function_name = ''

        for line in lines:
            building_function = line[0:4] == '    '
            tokens = line.split(' ')

            if tokens[0] == Token.FUNCTION:
                function_name = tokens[1]
                self.functions[function_name] = {}
                self.functions[function_name]['variables'] = []
                self.functions[function_name]['statements'] = []
                for i in range(2, len(tokens)):
                    self.functions[function_name]['variables'].append(tokens[i])
            else:
                statement = []
                for token in tokens:
                    if token != '':
                        if token in Token.PROTECTED_WORDS:
                            statement.append({'value': token, 'token': token})
                            
                        elif token in self.functions.keys():
                            statement.append({'value': token, 'token': Token.FUNCTION})

                        elif token not in Token.PROTECTED_WORDS:
                            if token.isnumeric():
                                statement.append({'value': int(token), 'token': Token.NUMBER})
                            elif token[0] == '"' and token[-1] == '"':
                                statement.append({'value': token[1:][:-1], 'token': Token.STRING})
                            else:
                                statement.append({'value': token, 'token': Token.VAR})
                if building_function:
                    self.functions[function_name]['statements'].append(statement)
                else:
                    self.execute(statement)

    def execute(self, statement):

        print('\n\n')
        for s in statement:
            print(s['value'], s['token'])

        if statement[0]['token'] == Token.RETURN: # Return Values
            return self.execute(statement[1:])

        elif statement[0]['token'] == Token.PRINT: # IO
            print(self.execute(statement[1:]))

        elif statement[0]['token'] == Token.FUNCTION: # Functions
            function = self.functions[statement[0]['value']]
            params = {}

            i = 1
            for var in function['variables']:
                params[var] = statement[i]['value']
                i += 1
            for s in function['statements']:
                for j in range(0, len(s)):
                    if s[j]['value'] in function['variables']:
                        s[j]['value'] = params[s[j]['value']]
                self.execute(s)

        elif statement[0]['token'] == Token.VAR: # Variables
            if len(statement)>1 and statement[1]['token'] == Token.IS:
                self.variables[statement[0]['value']] = self.execute(statement[2:])
            else: 
                statement[0]['value'] = self.variables[statement[0]['value']]
                if type(statement[0]['value']) != str:
                    statement[0]['token'] = Token.NUMBER
                else:
                    statement[0]['token'] = Token.STRING
                return self.execute(statement)   

        elif statement[0]['token'] == Token.NUMBER: # Numbers
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

        elif statement[0]['token'] == Token.STRING: # Strings
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