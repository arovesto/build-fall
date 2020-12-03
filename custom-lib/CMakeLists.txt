cmake_minimum_required(VERSION 3.0)

project(MyLib)

add_library(MyLib SHARED lib.h lib.cpp)
set_target_properties(MyLib PROPERTIES LINKER_LANGUAGE CXX)
