//
// Created by DorSh on 04-Feb-23.
//

#include <string>
#include "Lexer/lexer.h"

int main(int argc, char *argv[]) {
    std::string text = "(cur\r\n"
                       "checkIfSubstringInArray(\r\n"
                       "while (currentIndex <= textLength) {\r\n"
                       "\tunsigned int isSeparators = checkIfSubstringInArray(text, currentIndex, Lexer::Token::separators, 2);\r\n"
                       "if (isSeparators == 0)// check if the substring in the current index is not a separators";
    Lexer::lexerText(text);
}