//
// Created by DorSh on 05-Feb-23.
//

#ifndef STYPY_UTILS_H
#define STYPY_UTILS_H

#include <vector>
#include <map>
#include <string>

template<typename K, typename V> std::vector<K> getMapKeys(const std::map<K, V> &inputMap);
template <typename T> bool isInArray(T value, T arr[], int arrSize);
void replaceAllSubstring( std::string &s, const std::string &search, const std::string &replace);

template<typename K, typename V>
std::vector<K> getMapKeys(const std::map<K, V> &inputMap) {
    std::vector<K> keys;
    for (const auto &item: inputMap) {
        keys.push_back(item.first);
    }
    return keys;
}

template <typename T>
bool isInArray(T value, T arr[], int arrSize) {
    for (int i = 0; i < arrSize; i++) {
        if (value == arr[i]) {
            return true;
        }
    }
    return false;
}

void replaceAllSubstring( std::string &s, const std::string &search, const std::string &replace) {
    for( size_t pos = 0; ; pos += replace.length() ) {
        // Locate the substring to replace
        pos = s.find( search, pos );
        if( pos == std::string::npos ) break;
        // Replace by erasing and inserting
        s.erase( pos, search.length() );
        s.insert( pos, replace );
    }
}

#endif //STYPY_UTILS_H
