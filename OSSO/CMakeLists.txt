# Project
cmake_minimum_required(VERSION 3.16)
project(OSSO)

set(CMAKE_BUILD_TYPE Debug)


# Source code
add_executable(OSSO

    source/main.cpp
    source/app.cpp
    source/login.cpp

)

# wxWidgets
find_package(wxWidgets REQUIRED COMPONENTS xml xrc gl core base net)
include(${wxWidgets_USE_FILE})
target_include_directories(OSSO PRIVATE ${wxWidgets_INCLUDE_DIRS})
target_compile_definitions(OSSO PRIVATE ${wxWidgets_DEFINITIONS})
target_link_libraries(OSSO PRIVATE ${wxWidgets_LIBRARIES})