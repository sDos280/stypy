//
// Created by DorSh on 05-Feb-23.
//

#ifndef STYPY_LEXER_TYPES_H
#define STYPY_LEXER_TYPES_H

#include <map>
#include <string>
#include <sstream>

// ----------------------------------------------------------------------------------------------------
// https://en.wikipedia.org/wiki/Lexical_analysis#Token
enum TokenType {
    Identifier,
    Keyword,
    Separator,
    Operator,
    Literal,
    Comment
};

// token type to string dictionary
std::map<TokenType, std::string> tokenTypeToString{
        {TokenType::Identifier, "Identifier"},
        {TokenType::Keyword, "Keyword"},
        {TokenType::Separator, "Separator"},
        {TokenType::Operator, "Operator"},
        {TokenType::Literal, "Literal"},
        {TokenType::Comment, "Comment"}
};
// ----------------------------------------------------------------------------------------------------

// ----------------------------------------------------------------------------------------------------
// https://www.w3schools.com/python/python_comments.asp
// enum of the comments(syntax) of python
enum CommentTypes {
    OneLineStart,
    // TODO: multi-line comments block
};


// string to comments(syntax) dictionary
std::map<std::string, CommentTypes> stringToComment{
        {"#", CommentTypes::OneLineStart},
};
// ----------------------------------------------------------------------------------------------------

// ----------------------------------------------------------------------------------------------------
// https://www.w3schools.com/python/python_ref_keywords.asp
// enum of the keywords of python
enum KeywordTypes {
    And,
    While
    // TODO: add other keywords
};

// string to keyword dictionary
std::map<std::string, KeywordTypes> stringToKeyword{
        {"and",   KeywordTypes::And},
        {"while", KeywordTypes::While}
};
// ----------------------------------------------------------------------------------------------------

// ----------------------------------------------------------------------------------------------------
// https://www.w3schools.com/python/python_operators.asp
// enum of the operators of python
enum OperatorTypes {
    // Arithmetic Operators
    Addition,
    Subtraction,
    Multiplication,
    Division,
    Modulus,
    Exponentiation,
    FloorDivision
    // Python Assignment Operators
    // TODO: add assignment operators
};

// string to operator dictionary
std::map<std::string, OperatorTypes> stringToOperator{
        // Arithmetic Operators
        {"+",  OperatorTypes::Addition},
        {"-",  OperatorTypes::Subtraction},
        {"*",  OperatorTypes::Multiplication},
        {"/",  OperatorTypes::Division},
        {"%",  OperatorTypes::Modulus},
        {"%",  OperatorTypes::Exponentiation},
        {"//", OperatorTypes::FloorDivision}
        // Python Assignment Operators
        // TODO: add Assignment Operators
};
// ----------------------------------------------------------------------------------------------------

// ----------------------------------------------------------------------------------------------------
// Token structure
struct Token {
    union {
        CommentTypes commentType;
        KeywordTypes keywordTypes;
        OperatorTypes operatorTypes;
    };

    TokenType tokenType;
    std::string tokenString;
};

std::ostream& operator<<(std::ostream& os, const Token& token) {
    std::stringstream ss;
    ss << "Token type: " << tokenTypeToString[token.tokenType] << std::endl;
    ss << "Token string: " << token.tokenString << std::endl;
    os << ss.str();
    return os;
}

// ----------------------------------------------------------------------------------------------------
#endif //STYPY_LEXER_TYPES_H
