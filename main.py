from Lexer import lexer
from SyntaxAnalyzer import parse

with open("test_program.txt") as file:
    file_content = file.read()
    file_content = file_content.replace("\n", " ")
    lexical_units, key_words, two_char_ops, one_char_ops, punct, ids = lexer(file_content)
    parse(lexical_units, key_words, two_char_ops, one_char_ops, punct, ids)
