
class Token:

    class ReservedWords:
        PRINT = 'print'
        PLUS = 'plus'
        MINUS = 'minus'
        TIMES = 'times'
        DIVIDE = 'divide'
        FUNCTION = 'function'
        IS = 'is'

    STRING = 'string'
    NUMBER = 'number'
    VAR = 'var'

    def __init__(self, token, value=None):
        self.token = token
        self.value = value
    
    def __str__(self):
        return f'Token: {self.token} || Value: {self.value}'