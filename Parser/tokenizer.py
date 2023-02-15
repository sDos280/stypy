from Parser.token import *

current_index = 0

# return a token with a none-empty string if the current substring in the index is a comment starter
def get_comment_token(text: str):
    global current_index
    token_ = Token()
    text_length = len(text)

    if text[current_index] == ord('#'):  # check if a one line comment
        token_.kind = TokenKind.OneLineCommentTokenKind
        last_index = current_index + 1

        while last_index < text_length and text[last_index] != ord('\n'):
            last_index += 1
        token_.string = text[current_index + 1:last_index]

        current_index += last_index - (current_index + 1)
    elif text[current_index] == ord('\"') and text[current_index + 1] == ord('\"') and text[current_index + 2] == ord('\"'):
        token_.kind = TokenKind.BlockCommentTokenKind
        last_index = current_index + 3

        while last_index < text_length - 2 and text[last_index] != ord('\"') and text[last_index + 1] != ord('\"') and text[last_index + 2] != ord('\"'):
            last_index += 1
        token_.string = text[current_index + 3:last_index]

        current_index += last_index - (current_index + 3) + 3

    return token_


def lexer_text(text):
    global current_index
    """return a list of all the token of the text in order"""
    while current_index < len(text):
        commentToken = get_comment_token(text)
        if commentToken.string:
            print(commentToken.string)
            current_index += len(commentToken.string)
            continue

        current_index += 1
