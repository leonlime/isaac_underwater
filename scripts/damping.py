"""Module providind a function to calculate the drags forces of an object"""

def setup(db):
    """
    Initializes any necessary variables or data structures.
    """
    pass  # No initialization actions needed in this case

def compute(db):
    """
    Calculates the drag forces of an object based on its position and velocity.

    Args:
        db: The database object.
    
    Returns:
        Linear and angular damping
    """
    # Retrieve inputs
    z_pos = db.inputs.z_position

    # Calculate damping based on position
    if z_pos >= 0.5:
        linear_damping = 0.01
        angular_damping = 0.01
    elif z_pos < -0.5:
        linear_damping = 2.0
        angular_damping = 2.0
    elif -0.5 <= z_pos < 0.5:
        linear_damping = abs(2.0 * (z_pos - 0.5))
        angular_damping = abs(2.0 * (z_pos - 0.5))

    # Assign output
    db.outputs.linear_damping = linear_damping
    db.outputs.angular_damping = angular_damping
    