"""Module providing a function to generate buoyancy forces to an object"""

def setup(db):
    """
    Initializes any necessary variables or data structures.
    """
    pass  # No initialization actions needed in this case

def compute(db):
    """Calculates a non buoyancy force on the object.
    
    Args:
        db: The database object.

    Returns:
        A non rotated buoyancy force.
    """
    # Define constants
    water_density = 1  # kg/m^3
    gravity = 9.8  # m/s^2

    # Retrieve inputs
    volume = db.inputs.Volume  # m^3
    height = db.inputs.height  # m
    z_position = db.inputs.z_position  # m

    # Calculate submerged volume
    submerged_height = calculate_submerged_height(z_position, height)
    submerged_volume = volume * submerged_height

    # Calculate buoyancy force
    buoyancy_force = water_density * submerged_volume * gravity

    db.outputs.z_force = buoyancy_force

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
