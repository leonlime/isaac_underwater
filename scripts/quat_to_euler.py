"""Module providing a function to convert quaternion to Euler angles"""
import numpy as np

def setup(db):
    """
    Initializes any necessary variables or data structures.
    """
    pass  # No initialization actions needed in this case

def compute(db):
    """
    Convert quaternion to Euler angles.

    Args:
        db: The database object.

    Returns:
        A list of three Euler angles in degrees.
    """
    quaternion = db.inputs.quaternion

    x = quaternion[0]
    y = quaternion[1]
    z = quaternion[2]
    w = quaternion[3]

    # Roll
    t0 = 2 * (w * x + y * z)
    t1 = 1 - 2 * (x * x + y * y)
    roll = np.arctan2(t0, t1)

    # Pitch
    t2 = 2 * (w * y - z * x)
    t2 = np.clip(t2, -1.0, 1.0)
    pitch = np.arcsin(t2)

    # Yaw
    t3 = 2 * (w * z + x * y)
    t4 = 1 - 2 * (y * y + z * z)
    yaw = np.arctan2(t3, t4)

    # Convert to degrees
    roll = np.degrees(roll)
    pitch = np.degrees(pitch)
    yaw = np.degrees(yaw)

    db.outputs.rotation = [roll, pitch, yaw]
