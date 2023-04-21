#!/usr/bin/env python3
import rospy

from datetime import datetime
import os
import sys
from subprocess import call, DEVNULL

from dynamic_reconfigure.server import Server
from dynamic_reconfigure.client import Client

# Enter your package with .cfg
from multi_uav_dynreconfig.cfg import DynReconfigConfig

clients = []
config_file_path = ""
prev_params = []
default_params = []
initiated =  0

def client_callback(config):
    pass


def callback(config, level):
    global initiated
    global prev_params 
    global default_params
    params = {}

    # send the config to nodes and save the config in a new file
    if (initiated >= 1):

        for name in default_params:
            if name != "groups": 
                if name in config:
                    params.update({name: config[name]})
                else:
                    params.update({name: default_params[name]})

        if initiated == 1:
            rospy.loginfo("Loading initial config")
            print("\n".join(["\t" + name + ": " + str(params[name]) for name in sorted(params)]))
        else:
            rospy.loginfo("Received change in config")
            print("\n".join(["\t" + name + ": " + str(params[name]) for name in sorted(params) if (name not in prev_params) or params[name] != prev_params[name]]))

        prev_params = params  

        for client in clients:
            client.update_configuration(params)

        with open(config_file_path + "/config_" + str(datetime.now()), 'w') as file:
            file.write("\n".join([name + ": " + str(params[name]) for name in sorted(params)]))
    else:
        rospy.loginfo("Not Initiated");
        default_params = config

    initiated +=  1
    return config


if __name__ == "__main__":
    rospy.init_node("dyn_reconfig_server", anonymous=False)
    uav_list = rospy.get_param("~uav_list")
    node_list = rospy.get_param("~node_list")
    config_file_path = rospy.get_param("~config_file_path")

    client_names = []
    rospy.loginfo("Publishing to node: ")
    for uav_num in uav_list:
        for node in node_list:
            node_name = "/uav" + uav_num + "/" + node
            node_check = call('rosservice info ' + node_name + '/set_parameters', shell=True, stdout=DEVNULL, stderr=DEVNULL)
            if node_check != 0:
                rospy.logwarn("Can not find node: " + node_name)
                continue
            else:
                client_names.append(node_name)
                rospy.loginfo(node_name)
                    
    if len(client_names)== 0:
        exit(1)

    for client_name in client_names:
        clients.append(Client(client_name, timeout=1, config_callback=client_callback))

    # create the server
    srv = Server(DynReconfigConfig, callback)
    # create own client for intial setting from config file
    client = Client("/dynamic_reconfigure/dyn_reconfig_server", timeout=30, config_callback=client_callback)

    # Load last config file if available
    try:
        if len(os.listdir(config_file_path)) > 0:
            last_file = sorted(os.listdir(config_file_path))[-1]
            config_file = config_file_path + "/" + last_file
            config_dict= {}
            rospy.loginfo("Intial config file: " + config_file + "\n")
            with open(config_file, 'r') as file:
                for line in file.readlines():
                    config_dict.update({line.split(":")[0].strip(): float(line.split(":")[1])})
            rospy.loginfo("No of config items :" + str(len(config_dict)) + "\n")
            client.update_configuration(config_dict)

    except IOError as e:
        rospy.logwarn("Cannot read parameters from config file")
        rospy.logwarn("Error: " + str(e))
        rospy.loginfo("Using the received default params")
        client.update_configuration(default_params)

    rospy.spin()

