from .errors import LexingError
from .token import SourcePosition, Token


class Lexer(object):
    tokens = (
        "WHATEVR",
        "VISIBLE",
        "KTHXBAI",
        "GIMME",
        "MKAY",
        "HAS",
        "HAI",
        "ITZ",
        "OF",
        "BANG",
        "BY",
        "AN",
        "A",
        "R",
        "I",
        "MULTI_COMMENT",
        "NEWLINE",
        "PRIMITIVE_TYPE",
        "NUMBAR_LITERAL",
        "NUMBR_LITERAL",
        "TROOF_LITERAL",
        "YARN_LITERAL",
        "MATH_BINARY_OPERATOR",
        "MATH_UNARY_OPERATOR",
        "LOGICAL_BINARY_OPERATOR",
        "LOGICAL_UNARY_OPERATOR",
        "LOGICAL_VARIABLE_OPERATOR",
        "COMPARISON_BINARY_OPERATOR",
        "ASSIGNMENT_OPERATOR",
        "SINGLE_COMMENT",
        "IDENTIFIER",
        "LETTR_LITERAL",
        "ERROR"
    )

    def __init__(self, rules, ignore_rules):
        self.rules = rules
        self.ignore_rules = ignore_rules

    def lex(self, s):
        return LexerStream(self, s)


class LexerStream(object):
    def __init__(self, lexer, s):
        self.lexer = lexer
        self.s = s
        self.idx = 0

        self._lineno = 1

    def __iter__(self):
        return self

    def _update_pos(self, match):
        self.idx = match.end
        self._lineno += self.s.count("\n", match.start, match.end)
        last_nl = self.s.rfind("\n", 0, match.start)
        if last_nl < 0:
            return match.start + 1
        else:
            return match.start - last_nl

    def next(self):
        while True:
            if self.idx >= len(self.s):
                raise StopIteration
            for rule in self.lexer.ignore_rules:
                match = rule.matches(self.s, self.idx)
                if match:
                    self._update_pos(match)
                    break
            else:
                break

        for rule in self.lexer.rules:
            match = rule.matches(self.s, self.idx)
            if match:
                lineno = self._lineno
                colno = self._update_pos(match)
                source_pos = SourcePosition(match.start, lineno, colno)
                token = Token(
                    rule.name, self.s[match.start:match.end], source_pos
                )
                return token
        else:
            raise LexingError(None, SourcePosition(self.idx, -1, -1))

    def __next__(self):
        return self.next()
