from point3d import Point3D
from angle3d import Angle3D
from color import Color


class Flash:
    location: Point3D
    angle: Angle3D
    color: Color
    power: float

    def __init__(self, location, angle, color, power):
        self.location = Point3D(location[0], location[1], location[2])
        self.angle = Angle3D(angle[0], angle[1], angle[2])
        self.color = Color(color[0], color[1], color[2])
        self.power = power

    def __repr__(self):
        return f"Flash(location: {self.location}, angle: {self.angle}, color: {self.color}, power: {self.power})"

    def move(self, x, y, z) -> None:
        self.location.x += x
        self.location.y += y
        self.location.z += z

    def rotate(self, x_angle, y_angle, z_angle) -> None:
        self.angle.x_angle += x_angle
        self.angle.y_angle += y_angle
        self.angle.z_angle += z_angle
