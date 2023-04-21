# multi_uav_dynreconfig

This dynamic reconfiguration node can be used to reconfigure parameters on multiple uavs from a single rqt interface.

## Features
- Dynamically reconfigure multiple nodes of in multiple UAVs simultaneously.
- No need of initial configuration. It is loaded from the .cfg default parameter.
- Saves the latest configuration in a file.
- Loads the latest configuration, if one is available.

## Instructions

- Insert the parameters into the config/DynReconfig.cfg file.
- Provide the uav_name list and node list in the config/simulation/nodes.yaml file. 
- Build the multi_uav_dynreconfig package.
- Now, use the <multi_uav_dynreconfig/DynReconfigConfig.h> in your node as the configuration header file to link the callBack.
- Use ```roslaunch multi_uav_dynreconfig dynamic_reconfigure.launch``` to lauch the reconfiguration node. You can now use the rqt interface ```rosrun rqt_gui rqt_gui -s reconfigure``` to reconfigure the nodes.

