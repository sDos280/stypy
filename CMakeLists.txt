cmake_minimum_required(VERSION 3.23)
project(stypy)

set(CMAKE_CXX_STANDARD 14)

include_directories(Parser)

add_executable(stypy
        Lexer/lexer.cpp
        Lexer/lexer.h
        stypy.cpp)
