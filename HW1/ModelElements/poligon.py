from point3d import Point3D


class Poligon:
    points: list[Point3D]

    def __init__(self, points: tuple[tuple[float, float, float]]):
        self.points = []
        for point in points:
            self.points.append(Point3D(point[0], point[1], point[2]))


    def __repr__(self):
        return f"Poligon(points: {self.points})"
