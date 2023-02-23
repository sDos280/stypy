from enum import Enum, auto


# note: TK => Token Type

class TokenKind(Enum):
    # Comments(syntax)
    # https://www.w3schools.com/python/python_comments.asp
    SingleLineComment = auto()  # "#"
    BlockComment = auto()  # """ (3 double quotation mark)

    # Keywords
    # KW -> Keyword
    # https://www.w3schools.com/python/python_ref_keywords.asp
    AndKW = auto()  # and
    BreakKW = auto()  # break
    ContinueKW = auto()  # continue
    DefKW = auto()  # def
    ElifKW = auto()  # elif
    ElseKW = auto()  # else
    FalseKW = auto()  # False
    ForKW = auto()  # for
    IfKW = auto()  # if
    NotKW = auto()  # not
    OrKW = auto()  # or
    ReturnKW = auto()  # return
    TrueKW = auto()  # True
    WhileKW = auto()  # while

    # Separators
    CodeLeveler = auto()  # \t or "    "  (4 spaces)
    NewLine = auto()  # \n
    OpenParenthesis = auto()  # (
    CloseParenthesis = auto()  # )
    OpenBracket = auto()  # ]
    CloseBracket = auto()  # [
    OpenBrace = auto()  # {
    CloseBrace = auto()  # }
    Comma = auto()  # ,
    Colon = auto()  # :
    Dot = auto()  # .
    Semicolon = auto()  # ;

    # https://www.w3schools.com/python/python_operators.asp
    DoubleAsteriskEqual = auto()  # **=
    DoubleForwardSlashEqual = auto()  # //=
    RightShiftEqual = auto()  # >>=
    LeftShiftEqual = auto()  # <<=
    PlusEqual = auto()  # +=
    MinusEqual = auto()  # -=
    AsteriskEqual = auto()  # *=
    ForwardSlashEqual = auto()  # /=
    PercentEqual = auto()  # %=
    ANDEqual = auto()  # &=
    OREqual = auto()  # |=
    XOREqual = auto()  # ^=
    DoubleAsterisk = auto()  # **
    DoubleBackslash = auto()  # //
    EqualEqual = auto()  # ==
    NotEqual = auto()  # !=
    GreaterThanEqual = auto()  # >=
    LessThanEqual = auto()  # <=
    RightShift = auto()  # >>
    LeftShift = auto()  # <<
    Equal = auto()  # =
    PlusSign = auto()  # +
    MinusSign = auto()  # -
    Asterisk = auto()  # *
    ForwardSlash = auto()  # /
    PercentSign = auto()  # %
    GreaterThen = auto()  # >
    LessThen = auto()  # <
    AND = auto()  # &
    OR = auto()  # |
    XOR = auto()  # ^
    NOT = auto()  # ~

    # Literals
    String = auto()
    Integer = auto()
    Float = auto()

    # Identifier
    Identifier = auto()


# string to keyword dictionary
string_to_keyword: dict[str, TokenKind] = {
    # the token hierarchy is by string length
    "and": TokenKind.AndKW,
    "break": TokenKind.BreakKW,
    "continue": TokenKind.ContinueKW,
    "def": TokenKind.DefKW,
    "elif": TokenKind.ElifKW,
    "else": TokenKind.ElseKW,
    "False": TokenKind.FalseKW,
    "for": TokenKind.ForKW,
    "if": TokenKind.IfKW,
    "not": TokenKind.NotKW,
    "or": TokenKind.OrKW,
    "return": TokenKind.ReturnKW,
    "True": TokenKind.TrueKW,
    "while": TokenKind.WhileKW,
}

# string to separator dictionary
string_to_separator: dict[str, TokenKind] = {
    # the token hierarchy is by string length
    "    ": TokenKind.CodeLeveler,
    "\t": TokenKind.CodeLeveler,
    "\n": TokenKind.NewLine,
    "(": TokenKind.OpenParenthesis,
    ")": TokenKind.CloseParenthesis,
    "[": TokenKind.OpenBracket,
    "]": TokenKind.CloseBracket,
    "{": TokenKind.OpenBrace,
    "}": TokenKind.CloseBrace,
    ",": TokenKind.Comma,
    ":": TokenKind.Colon,
    ".": TokenKind.Dot,
    ";": TokenKind.Semicolon,
}

# string to operator dictionary
string_to_operator: dict[str, TokenKind] = {
    # the token hierarchy is by string length
    "**=": TokenKind.DoubleAsteriskEqual,
    "//=": TokenKind.DoubleForwardSlashEqual,
    ">>=": TokenKind.RightShiftEqual,
    "<<=": TokenKind.LeftShiftEqual,
    "+=": TokenKind.PlusEqual,
    "-=": TokenKind.MinusEqual,
    "*=": TokenKind.AsteriskEqual,
    "/=": TokenKind.ForwardSlashEqual,
    "%=": TokenKind.PercentEqual,
    "&=": TokenKind.ANDEqual,
    "|=": TokenKind.OREqual,
    "^=": TokenKind.XOREqual,
    "**": TokenKind.DoubleAsterisk,
    "//": TokenKind.DoubleBackslash,
    "==": TokenKind.EqualEqual,
    "!=": TokenKind.NotEqual,
    ">=": TokenKind.GreaterThanEqual,
    "<=": TokenKind.LessThanEqual,
    ">>": TokenKind.RightShift,
    "<<": TokenKind.LeftShift,
    "=": TokenKind.Equal,
    "+": TokenKind.PlusSign,
    "-": TokenKind.MinusSign,
    "*": TokenKind.Asterisk,
    "/": TokenKind.ForwardSlash,
    "%": TokenKind.PercentSign,
    ">": TokenKind.GreaterThen,
    "<": TokenKind.LessThen,
    "&": TokenKind.AND,
    "|": TokenKind.OR,
    "^": TokenKind.XOR,
    "~": TokenKind.NOT,
}


class TokenType(Enum):
    Identifier = auto()
    Keyword = auto()
    Separator = auto()
    Operator = auto()
    Literal = auto()
    Comment = auto()


class Token:
    def __init__(self, ttype: TokenType, kind: TokenKind, string: str):
        self.type: TokenType = ttype
        self.kind: TokenKind = kind
        self.string: str = string

    def __str__(self):
        string_ = ""
        string_ += f"{str(self.kind).split('.')[1]}: {self.string}"
        return string_
