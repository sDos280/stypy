//
// Created by DorSh on 04-Feb-23.
//

#ifndef STYPY_LEXER_H
#define STYPY_LEXER_H

#include <string>
#include <vector>
#define  KEYWORDS_COUNT 2

class Lexer {
public:


    //static std::vector<Lexer::Token, std::string> lexerText(const std::string &text);
    static void lexerText(const std::string &text);
    static bool iSCharACommentStart(const std::string& string, unsigned int index);
    static bool iSCharStartOfAKeyword(const std::string &string, unsigned int index);
    static bool iSCharAnOperatorStart(const std::string& string, unsigned int index);
    static bool iSCharASeparatorStart(const std::string& string, unsigned int index);
};


#endif //STYPY_LEXER_H
