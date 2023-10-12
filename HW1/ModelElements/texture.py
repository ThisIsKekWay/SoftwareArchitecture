class Texture:
    path: str

    def __init__(self, path):
        self.path = path

    def __repr__(self):
        return f"Texture(path: {self.path})"

