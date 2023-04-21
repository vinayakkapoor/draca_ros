#!/bin/bash

# goto mrs_swarm_core dir
cd ../

# clone the packages
gitman update 

# install pkg to use rosapi tools in c++
sudo apt install ros-noetic-rosbridge-server ros-noetic-rosapi

# dependency for simulation bash script
sudo snap install yq --channel=v3/stable

# build all packages
catkin build
