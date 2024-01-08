"""Module providing a function to generate buoyancy forces to an object"""
import math
import numpy as np

def setup(db):
    """
    Initializes any necessary variables or data structures.
    """
    pass  # No initialization actions needed in this case

def compute(db):
    """Calculates buoyancy force and rotates it based on object's orientation.
    
    Args:
        db: The database object.

    Returns:
        A rotated buoyancy force.
    """
    # Define constants
    water_density = 1  # kg/m^3
    gravity = 9.8  # m/s^2

    # Retrieve inputs
    volume = db.inputs.volume  # m^3
    height = db.inputs.height  # m
    z_position = db.inputs.z_position  # m
    rotation_angles = np.deg2rad(db.inputs.rotation)  # Convert to radians

    # Calculate submerged volume
    submerged_height = calculate_submerged_height(z_position, height)
    submerged_volume = volume * submerged_height

    # Calculate buoyancy force
    buoyancy_force = water_density * submerged_volume * gravity

    # Create rotation matrices for roll, pitch, and yaw
    roll_matrix = create_rotation_matrix_x(rotation_angles[0])
    pitch_matrix = create_rotation_matrix_y(rotation_angles[1])
    yaw_matrix = create_rotation_matrix_z(rotation_angles[2])

    # Combine rotation matrices
    rotation_matrix = roll_matrix @ pitch_matrix @ yaw_matrix

    # Create buoyancy vector and rotate it
    buoyancy_vector = np.array([0, 0, buoyancy_force])
    rotated_buoyancy_vector = np.matmul(rotation_matrix, buoyancy_vector)

    # Assign outputs
    db.outputs.x_force = -rotated_buoyancy_vector[0, 0]
    db.outputs.y_force = -rotated_buoyancy_vector[0, 1]
    db.outputs.z_force = rotated_buoyancy_vector[0, 2]

def calculate_submerged_height(z_position, height):
    """
    Calculates the submerged height of the object based on its z-position.
    
    Args:
        z_position: Z position of the object.
        height: Total height of the object.

    Returns:
        Submerged height of the object.
    """
    center_of_h = height / 2
    if z_position >= center_of_h:
        return 0.0
    elif z_position < -center_of_h:
        return height
    else:
        return center_of_h - z_position

def create_rotation_matrix_x(angle):
    """
    Creates a rotation matrix for rotation around the x-axis.

    Args:
        angle: Rotation on x-axis.

    Returns:
        Rotation matrix around the x-axis.
    """
    return np.matrix([
        [1, 0, 0],
        [0, math.cos(angle), -math.sin(angle)],
        [0, math.sin(angle), math.cos(angle)]
    ])

def create_rotation_matrix_y(angle):
    """
    Creates a rotation matrix for rotation around the y-axis.

    Args:
        angle: Rotation on y-axis.

    Returns:
        Rotation matrix around the y-axis.
    """
    return np.matrix([
        [math.cos(angle), 0, math.sin(angle)],
        [0, 1, 0],
        [-math.sin(angle), 0, math.cos(angle)]
    ])

def create_rotation_matrix_z(angle):
    """
    Creates a rotation matrix for rotation around the z-axis.

    Args:
        angle: Rotation on z-axis.

    Returns:
        Rotation matrix around the z-axis.
    """
    return np.matrix([
        [math.cos(angle), -math.sin(angle), 0],
        [math.sin(angle), math.cos(angle), 0],
        [0, 0, 1]
    ])
