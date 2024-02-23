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
    """
    # Retrieve inputs
    z_pos = db.inputs.z_position
    z_vel = db.inputs.velocity

    # Calculate damping based on position
    if z_pos >= 0.5:
        linear_damping = 0.01
    elif z_pos < -0.5:
        linear_damping = 2.0
    elif -0.5 <= z_pos < 0.5:
        linear_damping = abs(2.0 * (z_pos - 0.5))

    # Assign output
    db.outputs.damping = linear_damping
    