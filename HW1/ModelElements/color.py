class Color:
    r: float
    g: float
    b: float

    def __init__(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b

    def __repr__(self):
        return f"Color(r: {self.r}, g: {self.g}, b: {self.b})"

