cmake_minimum_required(VERSION 2.8.3)
project(multi_uav_dynreconfig)

set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++17 -fno-diagnostics-color")

## Find catkin macros and libraries
## if COMPONENTS list like find_package(catkin REQUIRED COMPONENTS xyz)
## is used, also find other catkin packages
find_package(catkin REQUIRED COMPONENTS 
  roscpp
  dynamic_reconfigure
)

generate_dynamic_reconfigure_options(
  config/DynReconfig.cfg
)

###################################
## catkin specific configuration ##
###################################

catkin_package(
  CATKIN_DEPENDS roscpp
  )

###########
## Build ##
###########

## Specify additional locations of header files
## Your package locations should be listed before other locations
