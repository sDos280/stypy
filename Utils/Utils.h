//
// Created by DorSh on 05-Feb-23.
//

#ifndef STYPY_UTILS_H
#define STYPY_UTILS_H

#include <vector>
#include <map>

template<typename K, typename V>
std::vector<K> getMapKeys(const std::map<K, V> &inputMap) {
    std::vector<K> keys;
    for (const auto &item: inputMap) {
        keys.push_back(item.first);
    }
    return keys;
}

#endif //STYPY_UTILS_H
