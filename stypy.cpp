//
// Created by DorSh on 04-Feb-23.
//

#include <string>
#include "Lexer/lexer.h"

int main(int argc, char *argv[]) {

    std::string text = "\"\"\"\n\n# The following.\n# The print function takes one or more arguments and outputs them to the console.\n# In this case, we\'re passing a single string argument: \"Hello, World!\".\n# The string is surrounded by quotes, which tell Python that this is a string literal.\n# You can use either single quotes (\') or double quotes (\") to define a string in Python.\nprint(\"Hello, World!\")\n";
    Lexer::lexerText(text);
}