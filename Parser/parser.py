import Parser.token as tk
import enum

global_types: list[str] = [
    "str",  # standard string
    "int",  # standard integer
    "float"  # standard float
]

# currently each variable is a global variable
global_variable: list['Variable'] = []

"""class Node:
    def __init__(self):
        self.parent: node = None
        self.child: node = None

    def set_parent(self, parent: Node):
        assert not parent, "unable to set parent, because parent is none"
        self.parent = parent

    def set_child(self, child: Node):
        assert not child, "unable to set child, because child is none"
        self.child = child"""


class Integer:
    """Integer Node"""

    def __init__(self, value: int):
        self.value: int = value

    def __str__(self):
        return str(self.value)


class Float:
    """Float Node"""

    def __init__(self, value: float):
        self.value: float = value

    def __str__(self):
        return str(self.value)


class Variable:
    """Variable Node"""

    def __init__(self, name: str, vtype: str):
        self.name: str = name
        self.type: str = vtype

    def __str__(self):
        return f"[name: {self.name}, type: {self.type}]"


class Expression:
    """Expression Node"""

    # expression is every thing that is able to return/have a value.
    class expressionType(enum.IntEnum):
        Integer = enum.auto()
        Float = enum.auto()
        Variable = enum.auto()
        Operator = enum.auto()

    def __init__(self, node, etype: expressionType):
        self.type: expressionType = etype
        # node is a void pointer
        self.node = node

    def __str__(self):
        return str(self.node)


class Operator:
    """Operator Node"""

    def __init__(self, tk_operation: tk.Token, left_operand: Expression, right_operand: Expression):
        self.operation: tk.Token = tk_operation
        self.left_operand: Expression = left_operand
        self.right_operand: Expression = right_operand

    def __str__(self):
        return f"[operation: {str(self.operation)}, left: {str(self.left_operand)}, right: {str(self.right_operand)}]"


class Assignment:
    """Assignment Node"""

    def __init__(self, var: Variable, value: Expression):
        self.var: Variable = var
        self.value: Expression = value

    def __str__(self):
        return f"[var: {str(self.var)}, value: {str(self.value)}]"


class VariableInitialisation(Assignment):
    """Variable Initialisation Node"""

    def __init__(self, var: Variable, value: Expression):
        super().__init__(var, value)


class parser:
    def __init__(self, tokens):
        self.tokens: list[tk.Token] = tokens
        self.index = 0  # The current index of the parser in the token.
        self.level = 0  # The current indentation level of the parser.
        self.abstract_syntax_tree: Node = None

    def parse(self) -> None:
        while self.index < len(self.tokens):
            stt = self.variable_initialisation()
            if stt is None:
                self.bump(1)
            else:
                print(stt)

    def bump(self, bump_by: int) -> None:
        self.index += bump_by

    def peek(self, index: int, raiseError: Exception = None) -> tk.Token:
        if raiseError is not None:
            if not 0 <= index < len(self.tokens): raise raiseError
        return self.tokens[index]

    def get_token(self, index: int) -> tk.Token:
        if not 0 <= index < len(self.tokens): assert False, "the token index is out of range"
        return self.tokens[index]

    def variable_initialisation(self) -> VariableInitialisation:
        if self.peek(self.index).kind == tk.TokenKind.Identifier and \
                self.peek(self.index + 1).kind == tk.TokenKind.Colon and \
                self.peek(self.index + 2, SyntaxError("the type is needed after the \':\'")).kind == tk.TokenKind.Identifier:  # checks for "name : type"

            if self.peek(self.index + 3).kind == tk.TokenKind.Equal:  # checks for assignment operator '='
                self.bump(4)  # move the current index to the expression index

                i: int = 0
                while self.index + i < len(self.tokens) and self.peek(self.index + i).kind != tk.TokenKind.NewLine and self.peek(self.index + i).type != tk.TokenType.Comment:
                    i += 1

                sub_expression: Expression = self.build_expression(self.index, i)
                sub_AST: VariableInitialisation = VariableInitialisation(Variable(self.tokens[self.index - 4].string, self.tokens[self.index - 2].string),
                                                                         sub_expression)
                return sub_AST

    def build_expression(self, start_index: int, length: int) -> Expression:
        if length == 0: raise SyntaxError("expression is needed")
        if length == 1:  # one token expression
            if self.tokens[start_index].kind == tk.TokenKind.Integer:
                return Expression(Integer(int(self.tokens[start_index].string)), Expression.expressionType.Integer)
            elif self.tokens[start_index].kind == tk.TokenKind.Float:
                return Expression(Float(float(self.tokens[start_index].string)), Expression.expressionType.Float)
