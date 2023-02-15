import string
from Parser.token import *


def lexer_text(code: str):
    """return a list of all the token of the code in order"""
    tokens = []

    current_index = 0
    while current_index < len(code):
        char = code[current_index]

        # Handle separators that are CodeLevelers
        if char == "\t":
            tokens.append((TokenKind.CodeLevelerTokenKind, "\t"))
            current_index += 1
        elif code[current_index:current_index + 4] == "    " and code[current_index + 4] != " ":
            tokens.append((TokenKind.CodeLevelerTokenKind, "    "))
            current_index += 4

        # Handle whitespaces
        elif char in string.whitespace:
            current_index += 1

        # Handle comments
        elif char == '#':  # one line comment
            start = current_index
            while current_index < len(code) and code[current_index] != '\n':
                current_index += 1
            comment = code[start:current_index]
            tokens.append((TokenKind.OneLineCommentTokenKind, comment))
        elif char == '\"' and code[current_index + 1] == '\"' and code[current_index + 2] == '\"':  # block comment
            start = current_index
            current_index += 3
            while current_index < len(code) and code[current_index - 2:current_index + 1] != "\"\"\"":
                current_index += 1
            current_index += 1
            comment = code[start:current_index]
            tokens.append((TokenKind.BlockCommentTokenKind, comment))

        # Handle names (variables and keywords)
        elif char.isalpha() or char == '_':
            start = current_index
            while current_index < len(code) and (code[current_index].isalnum() or code[current_index] == '_'):
                current_index += 1
            name = code[start:current_index]
            token_kind = string_to_keyword.get(name)
            if token_kind:  # a keyword
                tokens.append((token_kind, name))
            else:  # a identifier
                tokens.append((TokenKind.IdentifierTokenKind, name))

        # Handle numbers literals
        elif char.isdigit():
            start = current_index
            while current_index < len(code) and (code[current_index].isdigit() or code[current_index] == '.'):
                current_index += 1
            number = code[start:current_index]
            try:
                if number.index('.'):
                    tokens.append((TokenKind.FloatTokenKind, number))
            except ValueError:
                tokens.append((TokenKind.IntegerTokenKind, number))

        # Handle strings literals
        elif char == '\"':
            start = current_index
            current_index += 1
            while current_index < len(code) and code[current_index] != '\"':
                current_index += 1
            current_index += 1
            string_ = code[start:current_index]
            tokens.append((TokenKind.StringTokenKind, string_))

        # Handle chars literals
        elif char == '\'':
            start = current_index
            current_index += 1
            while current_index < len(code) and code[current_index] != '\'':
                current_index += 1
            current_index += 1
            string_ = code[start:current_index]
            tokens.append((TokenKind.CharTokenKind, string_))

        # Handle separators that aren't CodeLevelers
        elif char in "()[]{},:.;":
            tokens.append((string_to_separator[char], char))
            current_index += 1

        else:  # we shouldn't get here
            current_index += 1

    print(tokens)
