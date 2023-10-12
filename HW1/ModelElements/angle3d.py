class Angle3D:
    x_angle: float
    y_angle: float
    z_angle: float

    def __init__(self, x_angle, y_angle, z_angle):
        self.x_angle = x_angle
        self.y_angle = y_angle
        self.z_angle = z_angle

    def __repr__(self):
        return f"Angle3D(x_angle: {self.x_angle}, y_angle: {self.y_angle}, z_angle: {self.z_angle})"

