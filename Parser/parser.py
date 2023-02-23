from Parser.token import TokenKind

global_types: list[str] = [
    "str",  # standard string
    "int",  # standard integer
    "float"  # standard float
]

global_variable: list['Variable'] = []

class node:
    def __init__(self):
        self.parent: node = None
        self.child: node = None

    def set_parent(self, parent: node):
        assert not parent, "unable to set parent, because parent is none"
        self.parent = parent

    def set_child(self, child: node):
        assert not child, "unable to set child, because child is none"
        self.child = child

'''
class expression(node):
    """expression node"""
    def __init__(self):
        super().__init__()

class valueNode(node):
    """literal node"""
    def __init__(self):
        super().__init__()

class operator(node):
    """operator node"""
    def __init__(self):
        # child type should be a valueNode and there shouldn't be more than 2 children
        super().__init__()'''


class mainEntry:
    """A class that represents the main entry point in the AST.

            Attributes:
                start_block (block): The start block of the main entry point
            """

    def __init__(self):
        start_block: block = None

class Variable:
    """A class that represents a Variable in the AST.

            Attributes:
                name (str): The name of the Variable.
                gtype (str): The global type of the Variable.
                level: (int): The indentation level of the Variable(block).
            """

    def __init__(self):
        name: str = None
        gtype: str = None
        level: int = 0

class Expression:
    """A class that represents a Variable in the AST.

                Attributes:
                    gtype (str): The return type of the Expression.
                    value (str | float | int): The literal value of the Expression.  TODO: make the expression class more generic
                """

    def __init__(self):
        gtype: str = None
        value: str | float | int = None

class Assignment:
    """A class that represents an Assignment in the AST.

                Attributes:
                    var (Variable): The variable of Assignment.
                    value: (expression): The value that will be assigned to the variable.
                """

    def __init__(self):
        var: Variable = None
        value: Expresion = None

class block:
    """A class that represents a block in the AST.

        Attributes:
            instructions (list[class]): The instruction that are located in the block.
        """

    def __init__(self):
        super().__init__()
        instructions: list = []


class parser:
    def __init__(self, tokens):
        self.tokens: list[tuple[TokenKind, str]] = []
        self.index = 0  # The current index of the parser in the token.
        self.level = 0  # The current indentation level of the parser.
        self.abstract_syntax_tree: mainEntry = mainEntry(block())

    def parse(self):
        while self.index < len(self.tokens):
            pass

    def parse_variable_initialisation(self):
        if self.tokens[self.index] == TokenKind.AssignmentTokenKind