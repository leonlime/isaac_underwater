"""Module for PID controller implementation."""

def setup(db):
    """
    Initializes PID controller parameters and variables.

    Args:
        db: Database object containing controller parameters:
            sat_max: Maximum saturation limit for control output
            sat_min: Minimum saturation limit for control output 
            kp: Proportional gain
            ki: Integral gain
            kd: Derivative gain
            error_integral: Accumulated error for integral term
            error_prev: Previous error for derivative term
            time: Time step for discrete integration/derivation
    """
    db.sat_max = 1000
    db.sat_min = -1000
    db.kp = 100
    db.ki = 10
    db.kd = 0.01

    db.error_integral = 0
    db.error_prev = 0

    db.time = 0.01667

def compute(db):
    """
    Computes PID control output for orientation control with dive force.

    Implements a PID controller that tries to maintain 0 orientation.
    Control output is saturated between sat_min and sat_max.
    Final forces include an additional dive force component.

    Args:
        db: Database object containing:
            inputs.orientation: Current orientation measurement
            inputs.dive_force: Additional vertical force to apply

    Returns:
        Sets the following outputs in db:
            outputs.force: Force vector [x,y,z] with positive control
            outputs.minus_force: Force vector [x,y,z] with negative control
    """
    orientation = db.inputs.orientation
    dive_force = db.inputs.dive_force

    error = 0 - orientation
    db.error_integral += error

    control_output =\
        db.kp*error + db.ki*(db.error_integral)*db.time + db.kd*(error - db.error_prev)/db.time

    if control_output > db.sat_max:
        control_output = db.sat_max
    elif control_output < db.sat_min:
        control_output = db.sat_min

    db.error_prev = error

    db.outputs.force = [0,0, control_output + dive_force]
    db.outputs.minus_force = [0,0, -control_output + dive_force]
