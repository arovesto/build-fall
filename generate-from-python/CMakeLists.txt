cmake_minimum_required(VERSION 3.12)

project(PythonGeneratedLib)

find_package(Python3 COMPONENTS Interpreter)

if (NOT Python3_Interpreter_FOUND)
  message(FATAL_ERROR "Python is not found")
endif()

add_custom_command(
  OUTPUT ${PROJECT_SOURCE_DIR}/index.h
  COMMAND ${Python3_EXECUTABLE} ${PROJECT_SOURCE_DIR}/preparing.py ${PROJECT_SOURCE_DIR}/index.h
  DEPENDS preparing.py
  COMMENT "Generate lib from python"
)

add_custom_target( RunGenerator DEPENDS index.h COMMENT "Checking if file generated" )

add_library(PythonGeneratedLib SHARED index.h)
set_target_properties(PythonGeneratedLib PROPERTIES LINKER_LANGUAGE CXX)

add_dependencies( PythonGeneratedLib RunGenerator )

target_include_directories(PythonGeneratedLib PRIVATE ${CMAKE_LIBRARY_DIR})
