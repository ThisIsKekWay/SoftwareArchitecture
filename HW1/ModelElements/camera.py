from angle3d import Angle3D
from point3d import Point3D

class Camera:
    location: Point3D
    angle: Angle3D

    def __init__(self, location, angle):
        self.location = Point3D(location[0], location[1], location[2])
        self.angle = Angle3D(angle[0], angle[1], angle[2])

    def __repr__(self):
        return f"Camera(location: {self.location}, angle: {self.angle})"

    def move(self, x, y, z) -> None:
        self.location.x += x
        self.location.y += y
        self.location.z += z

    def rotate(self, x_angle, y_angle, z_angle) -> None:
        self.angle.x_angle += x_angle
        self.angle.y_angle += y_angle
        self.angle.z_angle += z_angle
