//
// Created by DorSh on 04-Feb-23.
//

#include "../Utils/Utils.h"
#include "lexer.h"
#include "token.h"
#include <iostream>

Token getCommentToken(const std::string &string, size_t index);
Token getKeywordToken(const std::string &string, size_t index);

// std::vector<Lexer::Token, std::string> Lexer::lexerText(const std::string &text) {
void Lexer::lexerText(const std::string &text) {
    // clean the text from sub strings
    std::string cleandText = text;
    replaceAllSubstring(cleandText, "\r\n", "\n");
    replaceAllSubstring(cleandText, "\r", "");

    // std::vector<Lexer::Token, std::string> tokens;
    size_t index = 0;
    while (index < text.length()) {
        if (isWhiteSpace(cleandText[index])) index++;
        // the token hierarchy: comment->separator->keyword
        Token commentToken = getCommentToken(cleandText, index);
        if (commentToken.size == 0){
            Token keywordToken = getKeywordToken(cleandText, index);
            if (keywordToken.size == 0){
                index++;
            }else{
                index += keywordToken.size;
                std::cout << keywordToken << std::endl;
            }
        }else{
            index += commentToken.size;
            std::cout << commentToken << std::endl;
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
        size_t commentStart = index + 1; // the first index after the #
        size_t commentEnd = string.find('\n', commentStart) - 1; // the last index before \n
        if (commentEnd == std::string::npos) {
            std::cerr << "there is an error" << std::endl;
            token.size = 0;
        }else{
            token.size = (commentEnd + 1) - (commentStart - 1);
        }


        // change the start index to the first none-white space char index
        while (isWhiteSpace(string[commentStart])) {
            commentStart++;
        }

        // change the end index to the last none-white space char index
        while (isWhiteSpace(string[commentEnd])) {
            commentEnd--;
        }

        token.string = string.substr(commentStart, commentEnd - commentStart + 1);

    } else if (string[index] == '\"' && string[index + 1] == '\"' && string[index + 2] == '\"')  // check if block comment
    {
        token.type = TokenType::Comment;
        token.kind = TokenKind::BlockComment;
        size_t commentStart = index + 3;  // the first index after the """
        size_t commentEnd = string.find(R"(""")", commentStart) - 1; // the last index before the first " of the comment clock closer
        if (commentEnd == std::string::npos) std::cerr << "there is an error" << std::endl;
        token.size = (commentEnd + 3) - (commentStart - 3);

        // change the start index to the first none-white space char index
        while (isWhiteSpace(string[commentStart])) {
            commentStart++;
        }

        // change the end index to the last none-white space char index
        while (isWhiteSpace(string[commentEnd])) {
            commentEnd--;
        }

        token.string = string.substr(commentStart, commentEnd - commentStart + 1);
    }

    return token;
}


// return a token with a none-empty string if the current substring in the index is keyword starter
Token getKeywordToken(const std::string &string, size_t index) {
    Token token;

    for (const auto & keyword : keywordsStrings){
        if (string.compare(index, keyword.length(), keyword) == 0)  // check if there is a keyword in the current index
        {
            token.type = TokenType::Keyword;
            token.kind = stringToKeyword[keyword];
            token.size = keyword.length();
            token.string = keyword;
        }
    }

    return token;
}