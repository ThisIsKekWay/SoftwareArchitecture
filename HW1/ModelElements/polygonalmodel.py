from poligon import Poligon
from texture import Texture


class PoligonalModel:
    name: str
    poligons: list[Poligon]
    textures: list[Texture]

    def __init__(self, name, poligons, textures):
        self.name = name
        self.textures.append(textures)
        self.poligons = []
        for poligon in poligons:
            self.poligons.append(Poligon(poligon))

    def __repr__(self):
        return f"PoligonalModel(name: {self.name}, poligons: {self.poligons}, textures: {self.textures})"
