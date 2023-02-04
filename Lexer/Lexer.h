//
// Created by DorSh on 04-Feb-23.
//

#ifndef STYPY_LEXER_H
#define STYPY_LEXER_H

#include <string>
#include <vector>

class Lexer {
public:
    struct Token {
        static const std::string keywords[];  // array of all the keywords defined in the language
        static const std::string operators[];  // array of all the operators defined in the language
        static const std::string separators[];  // array of all the separator defined in the language
        static const std::string commentSeparators[];  // array of all the separator defined in the language

        // the type of token
        enum type {
            Identifier,
            Keyword,
            Separator,
            Operator,
            Literal,
            Comment
        };
    };

    //static std::vector<Lexer::Token, std::string> lexerText(const std::string &text);
    static void lexerText(const std::string &text);
    static void bump(unsigned int currentIndex, const std::string &text, std::vector<Lexer::Token, std::string> tokens);
};


#endif //STYPY_LEXER_H
