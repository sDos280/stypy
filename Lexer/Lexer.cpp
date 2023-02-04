//
// Created by DorSh on 04-Feb-23.
//

#include "Lexer.h"
#include <iostream>

const std::string Lexer::Token::keywords[] = {"if", "while"};
const std::string Lexer::Token::operators[] = {"+", "-", "*", "/"};
const std::string Lexer::Token::separators[] = {"\r\n", " ", "(", ")"};
const std::string Lexer::Token::commentSeparators[] = {"/*", "*/", "//"};

static bool checkIfStringsEqualAtIndex(const std::string &textByIndex, const unsigned int index, const std::string &text);
static unsigned int checkIfSubstringInArray(const std::string &element, const unsigned int index, const std::string array[], const unsigned int arraySize);

// std::vector<Lexer::Token, std::string> Lexer::lexerText(const std::string &text) {
void Lexer::lexerText(const std::string &text) {
    // std::vector<Lexer::Token, std::string> tokens;
    unsigned int currentIndex = 0;
    std::string currentTokenString;
    unsigned int textLength = text.length();
    while (currentIndex <= textLength) {
        unsigned int isSeparators = checkIfSubstringInArray(text, currentIndex, Lexer::Token::separators, 4);
        if (isSeparators == 0)// check if the substring in the current index is not a separators
        {
            currentTokenString += text[currentIndex];
            currentIndex++;
        }
        else
        {
            std::cout << currentTokenString << std::endl;
            currentTokenString.clear();
            currentTokenString += text.substr(currentIndex, isSeparators);
            std::cout << currentTokenString << std::endl;
            currentTokenString.clear();

            currentIndex+=isSeparators;
        }
    }
    std::cout << currentTokenString << std::endl;

    // return tokens;
}

// add the current token to the tokens list
void Lexer::bump(unsigned int currentIndex, const std::string &text, std::vector<Lexer::Token, std::string> tokens) {

}

static bool checkIfStringsEqualAtIndex(const std::string &textByIndex, const unsigned int index, const std::string &text){
    return textByIndex.substr(index, text.length()) == text;
}

template<typename T> bool CheckIfElementInArray(const T element, const T& array, const unsigned int arraySize){
    bool isIn = false;
    for (int i = 0; i < arraySize; i++){
        isIn |= element == array[i];
    }
    return isIn;
}

static unsigned int checkIfSubstringInArray(const std::string &element, const unsigned int index, const std::string array[], const unsigned int arraySize){
    for (unsigned int i = 0; i < arraySize; i++){
        if (checkIfStringsEqualAtIndex(element, index, array[i])){
            return array[i].length();
        }
    }
    return 0;
}