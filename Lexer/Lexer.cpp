//
// Created by DorSh on 04-Feb-23.
//

#include "../Utils/Utils.h"
#include "Lexer.h"
#include "Lexer Types.h"
#include <vector>
#include <iostream>

Token getCommentToken(const std::string &string, unsigned int index);

// std::vector<Lexer::Token, std::string> Lexer::lexerText(const std::string &text) {
void Lexer::lexerText(const std::string &text) {
    // std::vector<Lexer::Token, std::string> tokens;
    unsigned int index = 0;
    while (index < text.length()){
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

        if (token.tokenString.empty()){
            index++;
        }else
        {
            index += token.tokenString.length();
            std::cout << token << std::endl;
        }



    }

    // return tokens;
}

// return a token with a none-empty string if the current substring in the index is a comment starter
Token getCommentToken(const std::string &string, unsigned int index){
    unsigned int stringLength = string.length();
    Token token;
    token.tokenType = TokenType::Comment;


    std::vector<std::string> commentStarter = getMapKeys(stringToComment);
    std::string commentStarterString;
    for (const auto & comment : commentStarter){
        if (string.compare(index, comment.length(), comment) == 0){
            commentStarterString = comment;
            break;
        }
    }
    if (commentStarterString.empty()){
        return token;
    }

    switch (stringToComment[commentStarterString]) {
        case OneLineStart:
            token.commentType = CommentTypes::OneLineStart;
            unsigned int indexCopy = index;
            do{
                indexCopy++;
                char temp = string[indexCopy];
                int sdfdsf = 0;
            } while (string[indexCopy] != '\n' && indexCopy <= stringLength);
            token.tokenString = string.substr(index, indexCopy - index);
    }
    return token;
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

