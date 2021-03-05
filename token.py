
class Token:

    class ReservedWords:
        PRINT = 'print'
        PLUS = 'plus'
        MINUS = 'minus'
        TIMES = 'times'
        DIVIDE = 'divide'
        FUNCTION = 'function'
        IS = 'is'
        IF = 'if'
        EQUALS = 'equals'
        GREATER = 'greater'
        LESS = 'less'

    STRING = 'string'
    NUMBER = 'number'
    VAR = 'var'
    BOOL = 'bool'
    INDENT = 't'
    UNINDENT = '/t'

    def __init__(self, token, value=None):
        self.token = token
        self.value = value
    
    def __str__(self):
        return f'Token: {self.token} || Value: {self.value}'