"""Module providind a function to calculate the damping forces of an object"""

def setup(db):
    """
    Initializes any necessary variables or data structures.
    """
    pass  # No initialization actions needed in this case

def compute(db):
    """
    Calculates the damping forces of an object based on its position.

    Args:
        db: The database object.
    
    Returns:
        Linear and angular damping
    """
    # Retrieve inputs
    z_pos = db.inputs.z_position  # m
    max_damp = db.inputs.max_damping
    height = db.inputs.floating_obj_height  # m
    half_height = height/2

    displacement_percentage = -z_pos / height + 0.5

    damping = 0

    # Calculate damping based on position
    if z_pos >= half_height:
        damping = 0.01
    elif z_pos < -half_height:
        damping = max_damp
    elif -half_height <= z_pos < half_height:
        damping = max_damp * displacement_percentage

    # Assign output
    db.outputs.linear_damping = damping
    db.outputs.angular_damping = damping
    