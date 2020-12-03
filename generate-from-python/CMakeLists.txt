cmake_minimum_required(VERSION 3.0)

project(PythonGeneratedLib)

add_custom_command(
  OUTPUT ${PROJECT_SOURCE_DIR}/index.h
  COMMAND python ${PROJECT_SOURCE_DIR}/preparing.py ${PROJECT_SOURCE_DIR}/index.h
  DEPENDS preparing.py
  COMMENT "Generate lib from python"
)

add_library(PythonGeneratedLib SHARED index.h)
set_target_properties(PythonGeneratedLib PROPERTIES LINKER_LANGUAGE CXX)

