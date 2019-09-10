from rply import LexerGenerator
from rply import Token


def build_lexer():
    lexer = LexerGenerator()

    # Lexer Analysis Rules
    lexer.ignore(' ')
    lexer.add("WHATEVR", r"WHATEVR")
    lexer.add("VISIBLE", r"VISIBLE")
    lexer.add("KTHXBAI", r"KTHXBAI")
    lexer.add("GIMME", r"GIMME")
    lexer.add("MKAY", r"MKAY")
    lexer.add("HAS", r"HAS")
    lexer.add("HAI", r"HAI")
    lexer.add("ITZ", r"ITZ")
    lexer.add("OF", r"OF")
    lexer.add("BANG", r"!")
    lexer.add("BY", r"BY")
    lexer.add("AN", r"AN")
    lexer.add("A", r"A")
    lexer.add("R", r"R")
    lexer.add("I", r"I")
    lexer.add("MULTI_COMMENT", r"OBTW [.*|\n]TDLR")  # Not working at all!
    lexer.add("NEWLINE", "\n")
    lexer.add("PRIMITIVE_TYPE", r"NUMBR|NUMBAR|LETTR|TROOF")
    lexer.add("NUMBAR_LITERAL", r"-?\d+.\d+")
    lexer.add("NUMBR_LITERAL", r"-?\d+")
    lexer.add("TROOF_LITERAL", r"[WIN|FAIL]")
    lexer.add("YARN_LITERAL", r"[\"|\'].*[\"|\']")
    lexer.add("MATH_BINARY_OPERATOR", r"SUM|DIFF|PRODUKT|QUOSHUNT|BIGGR|SMALLR")
    lexer.add("MATH_UNARY_OPERATOR", r"FLIP|SQUAR")
    lexer.add("LOGICAL_BINARY_OPERATOR", r"BOTH|EIHER|WON")
    lexer.add("LOGICAL_UNARY_OPERATOR", r"NOT")
    lexer.add("LOGICAL_VARIABLE_OPERATOR", r"ALL|ANY")
    lexer.add("COMPARISON_BINARY_OPERATOR", r"SAEM|DIFFRINT|FURSTSMALLR|FURSTBIGGR")
    lexer.add("ASSIGNMENT_OPERATOR", r"CORRECT_THIS")
    lexer.add("SINGLE_COMMENT", r"BTW.*\n")  # New line required to be added to tokens list prior!
    lexer.add("IDENTIFIER", r"[a-zA-Z][a-zA-Z_]*")
    lexer.add("LETTR_LITERAL", r".")
    lexer.add("ERROR", r"^[.]*")

    return lexer.build()


def tokenize_LOLcode(lolcode_str):
    lexer = build_lexer()
    tokens = list(lexer.lex(lolcode_str))
    return tokens


def test():
    tokens = tokenize_LOLcode("""HAI 1.450
    I HAS A result ITZ A NUMBR BTW I like apples
    result R 14

    VISIBLE result
    OBTW This is a 
    multiline comment
    TLDR
    KTHXBYE""")

    expected = [Token('HAI', 'HAI'), Token('NUMBAR_LITERAL', '1.450'), Token('NEWLINE', '\n'), Token('I', 'I'), Token('HAS', 'HAS'), Token('A', 'A'), Token('IDENTIFIER', 'result'), Token('ITZ', 'ITZ'), Token('A', 'A'), Token('PRIMITIVE_TYPE', 'NUMBR'), Token('NEWLINE', '\n'), Token('IDENTIFIER', 'result'), Token('R', 'R'), Token('NUMBR_LITERAL', '14'), Token('NEWLINE', '\n'), Token('NEWLINE', '\n'), Token('VISIBLE', 'VISIBLE'), Token('IDENTIFIER', 'result'), Token('NEWLINE', '\n'), Token('NEWLINE', '\n'), Token('KTHXBYE', 'KTHXBYE')]
    print(tokens)
    example_token = tokens[1]
    print(example_token.gettokentype())
    print(example_token.getstr())
    print(expected)

    assert expected == tokens

    import pprint
    pprint.pprint(expected)


test()

