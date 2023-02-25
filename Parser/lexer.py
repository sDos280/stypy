import string
import Parser.token as tk


class lexer:
    def __init__(self, text: str):
        self.text: str = text
        self.index: int = 0  # char index
        self.tokens: list[Token] = []
        self.to_skip_handler = False

    def first(self) -> str:
        return self.text[self.index]

    def bump(self, bump_by: int) -> None:
        self.index += bump_by

    def get_substring_by_length(self, start: int, length: int) -> str:
        return self.text[start:start + length]

    def get_substring_by_indexes(self, start: int, end: int) -> str:
        return self.text[start:end]

    def handle_code_levelers(self) -> None:
        """Handle separators that are CodeLevelers"""
        if self.to_skip_handler: return

        if self.first() == "\n":
            self.tokens.append(tk.Token(tk.TokenType.Separator, tk.TokenKind.NewLine, "\n"))
            self.bump(1)
            self.to_skip_handler = True

        elif self.first() == "\t":
            self.tokens.append(tk.Token(tk.TokenType.Separator, tk.TokenKind.CodeLeveler, "\t"))
            self.bump(1)
            self.to_skip_handler = True

        elif self.get_substring_by_length(self.index, 4) == "    " and self.text[self.index + 4] != " ":
            self.tokens.append(tk.Token(tk.TokenType.Separator, tk.TokenKind.CodeLeveler, "    "))
            self.bump(4)
            self.to_skip_handler = True

    def handle_white_space(self) -> None:
        """Handle whitespaces"""
        if self.to_skip_handler: return

        if self.first() in string.whitespace:
            self.bump(1)
            self.to_skip_handler = True

    def handle_comments(self) -> None:
        """Handle comments"""
        if self.to_skip_handler: return

        if self.first() == '#':  # one line comment
            start_index = self.index
            while self.index < len(self.text) and self.first() != '\n':
                self.bump(1)
            comment = self.get_substring_by_indexes(start_index, self.index)
            self.tokens.append(tk.Token(tk.TokenType.Comment, tk.TokenKind.SingleLineComment, comment))
            self.to_skip_handler = True

        elif self.get_substring_by_length(self.index, 3) == "\"\"\"":  # block comment
            start_index = self.index
            self.bump(3)
            while self.index < len(self.text) and self.get_substring_by_indexes(self.index - 2, self.index + 1) != "\"\"\"":
                self.bump(1)
            self.bump(1)
            comment = self.get_substring_by_indexes(start_index, self.index)
            self.tokens.append(tk.Token(tk.TokenType.Comment, tk.TokenKind.BlockComment, comment))
            self.to_skip_handler = True

    def handle_names(self) -> None:
        """Handle names (variables and keywords)"""
        if self.to_skip_handler: return

        if self.first().isalpha() or self.first() == '_':
            start_index = self.index
            while self.index < len(self.text) and (self.first().isalnum() or self.first() == '_'):
                self.bump(1)
            name = self.get_substring_by_indexes(start_index, self.index)
            token_kind = tk.string_to_keyword.get(name)
            if token_kind:  # a keyword
                self.tokens.append(tk.Token(tk.TokenType.Keyword, token_kind, name))
                self.to_skip_handler = True
            else:  # a identifier
                self.tokens.append(tk.Token(tk.TokenType.Identifier, tk.TokenKind.Identifier, name))
                self.to_skip_handler = True

    def handle_numbers(self) -> None:
        """Handle numbers literals"""
        if self.to_skip_handler: return

        dot_count = 0
        if self.first().isdigit():
            start_index = self.index
            while start_index < len(self.text) and (self.first().isdigit() or self.first() == '.'):
                if self.first() == '.': dot_count += 1
                if dot_count == 2: break
                self.bump(1)
            number = self.get_substring_by_indexes(start_index, self.index)
            if dot_count == 1:
                self.tokens.append(tk.Token(tk.TokenType.Literal, tk.TokenKind.Float, number))
                self.to_skip_handler = True
            else:
                self.tokens.append(tk.Token(tk.TokenType.Literal, tk.TokenKind.Integer, number))
                self.to_skip_handler = True

    def handle_strings(self) -> None:
        """Handle strings literals"""
        if self.to_skip_handler: return

        char = self.first()
        if char in "\'\"":
            start_index = self.index
            self.bump(1)
            while self.index < len(self.text) and self.first() not in char:
                self.bump(1)
            self.bump(1)
            string_ = self.get_substring_by_indexes(start_index, self.index)
            self.tokens.append(tk.Token(tk.TokenType.Literal, tk.TokenKind.String, string_))
            self.to_skip_handler = True

    def handle_separators(self) -> None:
        """Handle separators"""
        if self.to_skip_handler: return

        if self.first() in "()[]{},:.;":
            self.tokens.append(tk.Token(tk.TokenType.Separator, tk.string_to_separator[self.first()], self.first()))
            self.bump(1)
            self.to_skip_handler = True

    def handle_operators(self) -> None:
        """Handle operators"""
        if self.to_skip_handler: return

        if self.first() in "*/><+-%&|=^!":
            for operator_string, operator_token_kind in tk.string_to_operator.items():
                if self.get_substring_by_length(self.index, len(operator_string)) == operator_string:
                    self.tokens.append(tk.Token(tk.TokenType.Operator, operator_token_kind, operator_string))
                    self.bump(len(operator_string))
                    self.to_skip_handler = True

    def lex(self) -> None:
        """return a list of all the token of the code in order"""

        while self.index < len(self.text):
            index_start = self.index
            self.to_skip_handler = False

            self.handle_code_levelers()

            self.handle_white_space()

            self.handle_comments()

            self.handle_numbers()

            self.handle_strings()

            self.handle_separators()

            self.handle_operators()

            self.handle_names()

            if index_start == self.index:  # we shouldn't get here
                self.bump(1)

    def to_file(self, path):
        with open(path, "w") as writer:
            file_string = ""
            for t in self.tokens:
                file_string += str(t) + "\n"

            writer.write(file_string)
