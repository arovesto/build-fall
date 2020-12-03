cmake_minimum_required(VERSION 3.0)

project(BuildFall)

set(CMAKE_BINARY_DIR ${CMAKE_SOURCE_DIR}/bin)
set(EXECUTABLE_OUTPUT_PATH ${CMAKE_BINARY_DIR})
set(LIBRARY_OUTPUT_PATH ${CMAKE_BINARY_DIR}/lib)

include_directories("${PROJECT_SOURCE_DIR}/generate-from-python")
add_subdirectory(generate-from-python)
set(EXTRA_LIBS ${EXTRA_LIBS} PythonGeneratedLib)
include_directories("${PROJECT_SOURCE_DIR}/custom-lib")
add_subdirectory(custom-lib)
set(EXTRA_LIBS ${EXTRA_LIBS} MyLib)


add_executable(Main cmd/main.cpp)
target_link_libraries(Main ${EXTRA_LIBS})

install(TARGETS Main DESTINATION bin)
