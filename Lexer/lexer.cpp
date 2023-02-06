//
// Created by DorSh on 04-Feb-23.
//

#include "../Utils/Utils.h"
#include "lexer.h"
#include "token.h"
#include <iostream>

bool isWhiteSpace(char Char);

Token getCommentToken(const std::string &string, size_t index);

// std::vector<Lexer::Token, std::string> Lexer::lexerText(const std::string &text) {
void Lexer::lexerText(const std::string &text) {
    // std::vector<Lexer::Token, std::string> tokens;
    size_t index = 0;
    while (index < text.length()) {
        if (isWhiteSpace(text[index])) index++;
        Token token = getCommentToken(text, index);
        /*bool comment_ = iSCharACommentStart(text, index);
        bool keyword_ = iSCharStartOfAKeyword(text, index);
        bool operator_ = iSCharAnOperatorStart(text, index);
        bool separator_ = iSCharASeparatorStart(text, index);

        if (comment_){
            std::cout << "here is a comment " << index << std::endl;
        }

        if (keyword_){
            std::cout << "here is a keyword " << index << std::endl;
        }

        if (operator_){
            std::cout << "here is a operator " << index << std::endl;
        }

        if (separator_){
            std::cout << "here is a separator " << index << std::endl;
        }
        */

        if (token.size == 0) {
            index++;
        } else {
            index += token.size;
            std::cout << token << std::endl;
        }


    }

    // return tokens;
}

// return a token with a none-empty string if the current substring in the index is a comment starter
Token getCommentToken(const std::string &string, size_t index) {
    Token token;

    if (string[index] == '#') // check if a one line comment
    {
        token.type = TokenType::Comment;
        token.kind = TokenKind::OneLineComment;
        size_t commentEnd = string.find('\n', index);
        token.size = commentEnd - index;

        // change index to the last none-white space char index
        do {
            commentEnd--;
        } while (isWhiteSpace(string[commentEnd]));
        token.string = string.substr(index, (commentEnd + 1) - index);
    }
    else if (string[index] == '\"' and string[index + 1] == '\"' and string[index + 1] == '\"')  // check if block comment
    {
        token.type = TokenType::Comment;
        token.kind = TokenKind::BlockComment;
        size_t commentEnd = string.find(R"(""")", index+3);
        token.size = (commentEnd + 3) - index;

        // change index to the last none-white space char index
        do {
            commentEnd--;
        } while (isWhiteSpace(string[commentEnd]));
        token.string = string.substr(index, (commentEnd + 4) - index);
    }

    return token;
}

// check if a char is a white space
bool isWhiteSpace(char Char) {
    return isInArray(Char, whiteSpaces, WHITE_SPACES_COUNT);
}



/*bool Lexer::iSCharACommentStart(const std::string &string, unsigned int index) {
    return string[index] == '#';
}

// check if the char in the specified index is a start of a keyword
bool Lexer::iSCharStartOfAKeyword(const std::string &string, unsigned int index) {
    for (const auto & keyword : Lexer::Token::keywords){
        if (string.compare(index, keyword.length(), keyword) == 0){
            return true;
        }
    }
    return false;
}

// check if the char in the specified index is a start of an operator
bool Lexer::iSCharAnOperatorStart(const std::string& string, unsigned int index) {
    for (const auto & operator_ : Lexer::Token::operators){
        if (string.compare(index, operator_.length(), operator_) == 0){
            return true;
        }
    }
    return false;
}

// check if the char in the specified index is a start of a separator
bool Lexer::iSCharASeparatorStart(const std::string &string, unsigned int index) {
    for (const auto & separator : Lexer::Token::separators){
        if (string.compare(index, separator.length(), separator) == 0){
            return true;
        }
    }
    return false;
}*/
