from enum import IntEnum, auto


class TokenKind(IntEnum):
    # Comments(syntax)
    # https://www.w3schools.com/python/python_comments.asp
    OneLineCommentTokenKind = auto(),  # "#"
    BlockCommentTokenKind = auto(),  # "\"\"\"" (3 double quotation mark)

    # Keywords
    # https://www.w3schools.com/python/python_ref_keywords.asp
    AndTokenKind = auto(),  # add
    AsTokenKind = auto(),  # as
    BreakTokenKind = auto(),  # break
    ContinueTokenKind = auto(),  # continue
    DefTokenKind = auto(),  # def
    ElifTokenKind = auto(),  # elif
    ElseTokenKind = auto(),  # else
    FalseTokenKind = auto(),  # False
    ForTokenKind = auto(),  # for
    IfTokenKind = auto(),  # if
    NoneTokenKind = auto(),  # None
    NotTokenKind = auto(),  # not
    OrTokenKind = auto(),  # or
    PassTokenKind = auto(),  # pass
    ReturnTokenKind = auto(),  # Return
    TrueTokenKind = auto(),  # True
    WhileTokenKind = auto(),  # while
    # TODO: add other keywords

    # Separators
    CodeLevelerTokenKind = auto(),  # \t or "    "  (4 spaces)
    OpenParenthesisTokenKind = auto(),  # (
    CloseParenthesisTokenKind = auto(),  # )
    OpenBracketTokenKind = auto(),  # ]
    CloseBracketTokenKind = auto(),  # [
    OpenBraceTokenKind = auto(),  # 
    CloseBraceTokenKind = auto(),  # 
    CommaTokenKind = auto(),  # ,
    ColonTokenKind = auto(),  # :
    DotTokenKind = auto(),  # .
    SemicolonTokenKind = auto(),  # ;

    # https://www.w3schools.com/python/python_operators.asp
    # Arithmetic Operators
    AdditionTokenKind = auto(),  # +
    SubtractionTokenKind = auto(),  # -
    MultiplicationTokenKind = auto(),  # *
    DivisionTokenKind = auto(),  # /
    ModulusTokenKind = auto(),  # %
    ExponentiationTokenKind = auto(),  # **
    FloorDivisionTokenKind = auto(),  # //

    # (One char) Assignment Operators
    AssignmentTokenKind = auto(),  # =

    # Assignment Operators
    PlusAssignmentTokenKind = auto(),  # +=
    MinusAssignmentTokenKind = auto(),  # -=
    AsteriskAssignmentTokenKind = auto(),  # *=
    ForwardSlashAssignmentTokenKind = auto(),  # /=
    ModuloAssignmentTokenKind = auto(),  # %=
    DoubleForwardSlashAssignmentTokenKind = auto(),  # #=
    DoubleAsteriskSlashAssignmentTokenKind = auto(),  # **=
    ANDAssignmentTokenKind = auto(),  # &=
    ORAssignmentTokenKind = auto(),  # |=
    XORAssignmentTokenKind = auto(),  # ^=
    RightShiftAssignmentTokenKind = auto(),  # >>=
    LeftShiftAssignmentTokenKind = auto(),  # <<=

    # Comparison Operators
    EqualsTokenKind = auto(),  # ==
    NotEqualTokenKind = auto(),  # !=
    GreaterThenTokenKind = auto(),  # >
    LessThenTokenKind = auto(),  # <
    GreaterThanOrEqualsToTokenKind = auto(),  # >=
    LessThanOrEqualsToTokenKind = auto(),  # >=

    # Bitwise Operators
    ANDTokenKind = auto(),  # &
    ORTokenKind = auto(),  # |
    XORTokenKind = auto(),  # ^
    NOTTokenKind = auto(),  # ~
    RightShiftTokenKind = auto(),  # >>
    LeftShiftTokenKind = auto()  # <<


# string to keyword dictionary
string_to_keyword = {
    "and": TokenKind.AndTokenKind,
    "as": TokenKind.AsTokenKind,
    "break": TokenKind.BreakTokenKind,
    "continue": TokenKind.ContinueTokenKind,
    "def": TokenKind.DefTokenKind,
    "elif": TokenKind.ElifTokenKind,
    "else": TokenKind.ElseTokenKind,
    "False": TokenKind.FalseTokenKind,
    "for": TokenKind.ForTokenKind,
    "if": TokenKind.IfTokenKind,
    "None": TokenKind.NoneTokenKind,
    "not": TokenKind.NotTokenKind,
    "or": TokenKind.OrTokenKind,
    "pass": TokenKind.PassTokenKind,
    "return": TokenKind.ReturnTokenKind,
    "True": TokenKind.TrueTokenKind,
    "while": TokenKind.WhileTokenKind
}

# string to separator dictionary
string_to_separator = {
    "\t": TokenKind.CodeLevelerTokenKind,
    "    ": TokenKind.CodeLevelerTokenKind,
    "(": TokenKind.OpenParenthesisTokenKind,
    ")": TokenKind.CloseParenthesisTokenKind,
    "[": TokenKind.OpenBracketTokenKind,
    "]": TokenKind.CloseBracketTokenKind,
    "{": TokenKind.OpenBraceTokenKind,
    "}": TokenKind.CloseBraceTokenKind,
    ",": TokenKind.CommaTokenKind,
    ":": TokenKind.ColonTokenKind,
    ".": TokenKind.DotTokenKind,
    ";": TokenKind.SemicolonTokenKind
}

# string to operator  dictionary
string_to_operator = {
    # the token hierarchy: ThreeChars->TwoChars->OneChar
    "**=": TokenKind.DoubleAsteriskSlashAssignmentTokenKind,
    "//=": TokenKind.DoubleForwardSlashAssignmentTokenKind,
    ">>=": TokenKind.RightShiftAssignmentTokenKind,
    "<<=": TokenKind.LeftShiftAssignmentTokenKind,
    "+=": TokenKind.PlusAssignmentTokenKind,
    "-=": TokenKind.MinusAssignmentTokenKind,
    "*=": TokenKind.AsteriskAssignmentTokenKind,
    "/=": TokenKind.ForwardSlashAssignmentTokenKind,
    "%=": TokenKind.ModuloAssignmentTokenKind,
    "&=": TokenKind.ANDAssignmentTokenKind,
    "|=": TokenKind.ORAssignmentTokenKind,
    "^=": TokenKind.XORAssignmentTokenKind,
    "**": TokenKind.ExponentiationTokenKind,
    "//": TokenKind.FloorDivisionTokenKind,
    "==": TokenKind.EqualsTokenKind,
    "!=": TokenKind.NotEqualTokenKind,
    ">=": TokenKind.GreaterThanOrEqualsToTokenKind,
    "<=": TokenKind.LessThanOrEqualsToTokenKind,
    ">>": TokenKind.RightShiftTokenKind,
    "<<": TokenKind.LeftShiftTokenKind,
    "=": TokenKind.AssignmentTokenKind,
    "+": TokenKind.AdditionTokenKind,
    "-": TokenKind.SubtractionTokenKind,
    "*": TokenKind.MultiplicationTokenKind,
    "/": TokenKind.DivisionTokenKind,
    "%": TokenKind.ModulusTokenKind,
    ">": TokenKind.GreaterThenTokenKind,
    "<": TokenKind.LessThenTokenKind,
    "&": TokenKind.ANDTokenKind,
    "|": TokenKind.ORTokenKind,
    "^": TokenKind.XORTokenKind,
    "~": TokenKind.NOTTokenKind,
}


class Token:
    def __init__(self):
        self.kind = None
        self.string = None
