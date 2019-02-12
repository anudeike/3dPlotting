from rply import LexerGenerator

class Lexer():
    def __init__(self):
        self.lexer = LexerGenerator()

    def _add_tokens(self):
        #plot
        self.lexer.add('PLOT', r'plot')

        #Parenthesis
        self.lexer.add('OPEN_PAREN', r'\(')
        self.lexer.add('CLOSE_PAREN', r'\)')

        # Operators
        self.lexer.add('SUM', r'\+')
        self.lexer.add('SUB', r'\-')
        self.lexer.add('MULT', r"\*")
        self.lexer.add('DIV', r"\/")
        self.lexer.add('EQU', r'\=')
        self.lexer.add('EXP', r'\^')

        # Number
        self.lexer.add('NUMBER', r'\d+')

        # variables
        self.lexer.add('X_VAR', r'x')
        self.lexer.add('Y_VAR', r'y')
        self.lexer.add('Z_VAR', r'z')

        # Ignore spaces
        self.lexer.ignore('\s+')

    def get_lexer(self):
        self._add_tokens()
        return self.lexer.build()