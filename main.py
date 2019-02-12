from lexer import Lexer

text_input = """
plot(x + y = z)
"""

lexer = Lexer().get_lexer()
tokens = lexer.lex(text_input)

print("Original string: " + text_input)
for token in tokens:
    print(token)