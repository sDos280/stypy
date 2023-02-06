//
// Created by DorSh on 04-Feb-23.
//

#include <string>
#include <fstream>
#include <iostream>
#include "Lexer/lexer.h"

int main(int argc, char *argv[]) {
    std::string fileName = "../test_txt.py";
    std::ifstream file(fileName);

    if (file.is_open()) {
        std::string contents((std::istreambuf_iterator<char>(file)),
                             std::istreambuf_iterator<char>());

        Lexer::lexerText(contents);

    } else {
        std::cerr << "Cannot open file '" << fileName << "'." << std::endl;
    }
    return 0;


}