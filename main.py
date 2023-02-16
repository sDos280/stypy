import sys
import pathlib
import Parser.lexer

def main():
    pass


def usage():
    print("python main.py path_to_file")


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("you are using stypy wrong")
        usage()
        exit(1)

    path_to_file = sys.argv[1]

    try:
        with open(pathlib.Path(path_to_file)) as reader:
            file_string = reader.read()
            # clean file string
            file_string.replace("\r\n", "\n")
            file_string.replace("\r", "")

            lexer = Parser.lexer.lexer(file_string)

            tokens = lexer.lex()

    except FileNotFoundError:
        print(f"there isn't a file in the path {path_to_file}")

    main()
