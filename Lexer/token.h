//
// Created by DorSh on 05-Feb-23.
//

#ifndef STYPY_TOKEN_H
#define STYPY_TOKEN_H
#define WHITE_SPACES_COUNT 4

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

enum TokenKind {
    // Comments(syntax)
    // https://www.w3schools.com/python/python_comments.asp
    OneLineComment,  // "#"
    BlockComment, // "\"\"\"" (3 double quotation mark)

    // Keywords
    // https://www.w3schools.com/python/python_ref_keywords.asp
    And,       // add
    As,        // as
    Break,     // break
    Continue,  // continue
    Def,       // def
    Elif,      // elif
    Else,      // else
    False,     // False
    For,       // for
    If,        // if
    None,      // None
    Not,       // not
    Or,        // or
    Pass,      // pass
    Return,    // Return
    True,      // True
    While,     // while
    // TODO: add other keywords

    // Separators
    CodeLeveler,       // \t or "    "  (4 spaces)
    OpenParenthesis,   // (
    CloseParenthesis,  // )
    OpenBracket,       // ]
    CloseBracket,      // [
    OpenBrace,         // {
    CloseBrace,        // }
    Comma,             // ,
    Colon,             // :
    Dot,               // .
    Semicolon,         // ;

    // https://www.w3schools.com/python/python_operators.asp
    // Arithmetic Operators
    Addition,        // +
    Subtraction,     // -
    Multiplication,  // *
    Division,        // /
    Modulus,         // %
    Exponentiation,  // **
    FloorDivision,   // //

    // (One char) Assignment Operators
    Assignment,              // =

    // Assignment Operators
    PlusAssignment,                 // +=
    MinusAssignment,                // -=
    AsteriskAssignment,             // *=
    ForwardSlashAssignment,         // /=
    ModuloAssignment,               // %=
    DoubleForwardSlashAssignment,   // //=
    DoubleAsteriskSlashAssignment,  // **=
    ANDAssignment,                  // &=
    ORAssignment,                   // |=
    XORAssignment,                  // ^=
    RightShiftAssignment,           // >>=
    LeftShiftAssignment,            // <<=

    // Comparison Operators
    Equals,                 // ==
    NotEqual,               // !=
    GreaterThen,            // >
    LessThen,               // <
    GreaterThanOrEqualsTo,  // >=
    LessThanOrEqualsTo,     // >=

    // Bitwise Operators
    AND,         // &
    OR,          // |
    XOR,         // ^
    NOT,         // ~
    RightShift,  // >>
    LeftShift   // <<
};
// ----------------------------------------------------------------------------------------------------

// ----------------------------------------------------------------------------------------------------
// token type to string dictionary
std::map<TokenType, std::string> tokenTypeToString{
        {TokenType::Identifier, "Identifier"},
        {TokenType::Keyword,    "Keyword"},
        {TokenType::Separator,  "Separator"},
        {TokenType::Operator,   "Operator"},
        {TokenType::Literal,    "Literal"},
        {TokenType::Comment,    "Comment"}
};

// string to comments(syntax) dictionary
std::map<std::string, TokenKind> stringToComment{
        {"#",      TokenKind::OneLineComment},
        {R"(""")", TokenKind::BlockComment},
};

// string to keyword dictionary
std::map<std::string, TokenKind> stringToKeyword{
        {"and",      TokenKind::And},
        {"as",       TokenKind::As},
        {"break",    TokenKind::Break},
        {"continue", TokenKind::Continue},
        {"def",      TokenKind::Def},
        {"elif",     TokenKind::Elif},
        {"else",     TokenKind::Else},
        {"False",    TokenKind::False},
        {"for",      TokenKind::For},
        {"if",       TokenKind::If},
        {"None",     TokenKind::None},
        {"not",      TokenKind::Not},
        {"or",       TokenKind::Or},
        {"pass",     TokenKind::Pass},
        {"return",   TokenKind::Return},
        {"True",     TokenKind::True},
        {"while",    TokenKind::While}
};

std::vector<std::string> keywordsStrings = getMapKeys(stringToKeyword);

// string to separator dictionary
std::map<std::string, TokenKind> stringToSeparator{
        {"\t",   TokenKind::CodeLeveler},
        {"    ", TokenKind::CodeLeveler},
        {"(",    TokenKind::OpenParenthesis},
        {")",    TokenKind::CloseParenthesis},
        {"[",    TokenKind::OpenBracket},
        {"]",    TokenKind::CloseBracket},
        {"{",    TokenKind::OpenBrace},
        {"}",    TokenKind::CloseBrace},
        {",",    TokenKind::Comma},
        {":",    TokenKind::Colon},
        {".",    TokenKind::Dot},
        {";",    TokenKind::Semicolon}
};

std::vector<std::string> separatorsStrings = getMapKeys(stringToSeparator);

// string to operator dictionary
std::map<std::string, TokenKind> stringToOperator{
        // the token hierarchy: ThreeChars->TwoChars->OneChar
        {"**=", TokenKind::DoubleAsteriskSlashAssignment},
        {"//=", TokenKind::DoubleForwardSlashAssignment},
        {">>=", TokenKind::RightShiftAssignment},
        {"<<=", TokenKind::LeftShiftAssignment},
        {"+=",  TokenKind::PlusAssignment},
        {"-=",  TokenKind::MinusAssignment},
        {"*=",  TokenKind::AsteriskAssignment},
        {"/=",  TokenKind::ForwardSlashAssignment},
        {"%=",  TokenKind::ModuloAssignment},
        {"&=",  TokenKind::ANDAssignment},
        {"|=",  TokenKind::ORAssignment},
        {"^=",  TokenKind::XORAssignment},
        {"**",  TokenKind::Exponentiation},
        {"//",  TokenKind::FloorDivision},
        {"==",  TokenKind::Equals},
        {"!=",  TokenKind::NotEqual},
        {">=",  TokenKind::GreaterThanOrEqualsTo},
        {">=",  TokenKind::LessThanOrEqualsTo},
        {">>",  TokenKind::RightShift},
        {"<<",  TokenKind::LeftShift},
        {"=",   TokenKind::Assignment},
        {"+",   TokenKind::Addition},
        {"-",   TokenKind::Subtraction},
        {"*",   TokenKind::Multiplication},
        {"/",   TokenKind::Division},
        {"%",   TokenKind::Modulus},
        {">",   TokenKind::GreaterThen},
        {"<",   TokenKind::LessThen},
        {"&",   TokenKind::AND},
        {"|",   TokenKind::OR},
        {"^",   TokenKind::XOR},
        {"~",   TokenKind::NOT}

};

std::vector<std::string> OperatorsStrings = getMapKeys(stringToOperator);

// array of all white spaces
char whiteSpaces[] = {
        ' ',
        '\r',
        '\013',
        '\n'
};
// ----------------------------------------------------------------------------------------------------

// ----------------------------------------------------------------------------------------------------
// Token structure
struct Token {
    TokenKind kind;
    TokenType type;
    std::string string;
    size_t size = 0;  // the size of the token string (as in the chars in file)
};

std::ostream &operator<<(std::ostream &os, const Token &token) {
    std::stringstream ss;
    ss << "Token type: " << tokenTypeToString[token.type] << std::endl;
    ss << "Token string: " << token.string << std::endl;
    os << ss.str();
    return os;
}

bool isWhiteSpace(char Char);

// check if a char is a white space
bool isWhiteSpace(char Char) {
    return isInArray(Char, whiteSpaces, WHITE_SPACES_COUNT);
}

// ----------------------------------------------------------------------------------------------------
#endif //STYPY_TOKEN_H
