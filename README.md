# isaac_underwater
## Overview
![readme_top](/pictures/readme_top.png)

- This repository contains study examples of my water and underwater simulations utilizing NVIDIA Isaac Sim. These examples include a floating box simulation on the water surface and two ROV (Remotely Operated Vehicle) simulations, controlled using a PS4 controller. It is important to note that these examples are not 100% physically accurate yet.

**Keywords:** simulation, Isaac, underwater, robotics

## Last updates
- Date: 21/02/2025
- Updated package to Isaac Sim 4.5.0
- Added a new example of a ROV simulation

## License 
- The source code is released under a [MIT License](LICENSE).

**Author:** 
Leonardo Lima (leo.mendes21@hotmail.com)

## Instalation
To utilize this package, simply clone the repository and install all necessary dependencies.

## Dependencies
The `isaac_underwater` package has been created and tested under Ubuntu 22.04. This is research code, expect that it changes often and any fitness for a particular purpose is disclaimed.

| OS | Isaac Sim | ROS 2 |
| :---: | :---: | :---: |
| [Ubuntu 22.04](https://releases.ubuntu.com/jammy/) | [4.5.0](https://docs.isaacsim.omniverse.nvidia.com/latest/index.html) | [Humble](https://docs.ros.org/en/humble/Installation.html) |

## Examples
### Floating cube
![box](/pictures/box.gif)

This example features a cube floating on water and represents my initial test with Isaac Sim. It is a basic simulation where the cube floats due to buoyancy forces, which are calculated by a script named `buoyancy_forces.py`, located in the `scripts` folder. There is also an associated `damping.py` script to resist movement and create a sense of drag, while this feature has not yet been fully implemented in the example. A current was simulated using the gravity property in Isaac Sim.

### ROV simulation
![rov](/pictures/rov.gif)

In this example, I attempted a more complex task by integrating the box code with an ROV controlled by a gamepad. I applied the same logic to the floating mechanism of the ROV and introduced forces based on the buttons pressed on the gamepad. The rotation matrix for buoyancy forces has not been implemented in this version.

### ROV simulation 2
![rov2](/pictures/rov2.gif)

This example was developed to test an ROV simulation with PID control. In this implementation, forces are applied independently to each ROV thruster, enabling more precise simulation dynamics. A PID controller was implemented to stabilize the ROV's orientation and prevent unwanted tilting. Special thanks to [Kira Benton](https://www.linkedin.com/in/kira-benton-505728299/) for the ROV design concept.

#### How to control the ROV
Use the PS4 controller's `left and right sticks` to maneuver and rotate the ROV, and press the `R2` button to submerge.

## Scripts
### `buoyancy_forces.py`
This code is used to calculate the buoyancy force acting on an object submerged in water. The buoyancy force is based on the amount of the object that is submerged, the density of the water, and the gravitational force.
### `buoyancy_control.py`
This follows the same principles as `buoyancy_forces.py`, but it does not yet incorporate rotational forces. The implementation remains purely linear to simplify control and movement via the PS4 controller. Further improvements are required.
### `damping.py`
This script calculates the damping forces acting on an object based on its position. Damping forces resist motion and are typically used in simulations to reduce velocity over time, either linearly or rotationally (angular damping). Further improvements are required.
### `quat_to_euler.py`
This code is used to convert an orientation represented by a quaternion into Euler angles (roll, pitch, and yaw), which are more intuitive for humans to understand and are commonly used to represent rotation along three axes: roll (tilting), pitch (forward and backward tilting), and yaw (horizontal rotation).
### `controller.py`
This script implements a PID controller to control the ROV's orientation and prevent unwanted tilting. 
### `linear_angular_control.py`
The script takes x and y joystick values and calculates appropriate thrust values for four thrusters in a configuration that allows for both linear and angular motion control.
