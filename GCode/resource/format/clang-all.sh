#! /bin/bash

find -name '*.cpp' -o -name '*.h' -o -name '*.cc' -o -name '*.cc' | xargs clang-format-6.0 -i
