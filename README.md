
# draca_ros

draca_ros is an open-source project that provides a singularity container for running **DRACA - Deep Reinforcement learning based Autonomous Collision Avoidance**, a plugin for drone swarms. This project was developed at the [Multi-Robot Systems Group](http://mrs.felk.cvut.cz/), Czech Technical University in Prague as part of my undergraduate thesis.

## Description

draca_planner is built for the [MRS UAV system](https://github.com/ctu-mrs/mrs_uav_system), and uses **trained PyTorch models to control drone swarms.** It depends on the *swarm_control_manager* package, which is currently undergoing testing before being open-sourced. Therefore, draca_ros provides a containerized solution to build everything in a singularity container and run draca_planner.

## Installation

Please note that using draca_ros requires significant computing resources, including:

- Over 7 GB of internet data to download necessary dependencies and packages
- Over 50 GB of temporary root storage to build the Singularity image file
- About 10 GB of storage to run DRACA and other necessary components

Before using this project, please ensure that your machine has sufficient resources to accommodate these requirements. Additionally, please be aware that running the Singularity build process and DRACA within a container may consume significant CPU and memory resources. Please plan accordingly and ensure that you have adequate resources available before using this project.


For installing draca_ros, please carefully follow these instructions:

1. Begin by pulling the `draca_planner` submodule using the `git submodule update --init --recursive` command.
2. Install Singularity and Docker using the scripts provided in the `singularity/install` directory. If these dependencies are already installed, you may skip this step.
3. Proceed to build the Singularity container by running the `./singularity/recipe/build.sh` script. This will include the MRS UAV system, ROS Neotic with PyTorch, and all other necessary dependencies.


## Usage

To use draca_ros, follow these steps:

- Run the Singularity container using `./singularity/run_singularity.sh`.
- Move to the `user_ros_workspace` using `cd user_ros_workspace`.
- Build the `mrs_swarm_core` ROS packages and `draca_planner` using `catkin build -c`.
- Change the directory to `./src/mrs_swarm_core/simulation/` and run the simulation using `./simulate_swarm.sh -f config/sim_config.yaml`.

The simulation configurations and the Gazebo world can be changed under `mrs_swarm_core/simulation/config/sim_config.yaml` and `mrs_swarm_core/simulation/config/gazebo_config`.

**Please checkout *[draca_planner](https://github.com/vinayakkapoor/draca_planner)* to gain a better perspective on the capabilities and scope of customisation of this plugin**


## Support

If you encounter any bugs, please raise a GitHub issue. For suggestions or other forms of support, please contact us at vinayakkapoor12@gmail.com.

## Authors and Acknowledgments

I would like to thank [Dr. Martin Saska](http://mrs.felk.cvut.cz/people/martin-saska) and the entire research group for their constant help. I am eternally grateful to [Mr. Afzal Ahmad](http://mrs.felk.cvut.cz/people/afzal-ahmad) and [Dr. Daniel Bonilla Licea](http://mrs.felk.cvut.cz/members/postdocs/daniel-bonilla) for guiding me at every step of the way. It was indeed a pleasure to learn under their able guidance. I would also like to extend my gratitude to [Dr. Jitendra Singh Rathore](https://www.bits-pilani.ac.in/pilani/jitendrarathore/profile) for his support and encouragement throughout the project.

## License

draca_ros is released under the MIT License.

## Project Status

draca_ros is an actively maintained project, and we welcome feedback and contributions from the community. Please let us know if you encounter any bugs or issues.
