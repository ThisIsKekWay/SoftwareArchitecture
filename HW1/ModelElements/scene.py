from polygonalmodel import PoligonalModel
from flash import Flash
from camera import Camera


class Scene:
    id: int
    models: list[PoligonalModel]
    flashes: list[Flash]
    cameras: list[Camera]

    def __init__(self, scene_id, models, flashes, cameras):
        self.id = scene_id
        if len(models) < 1:
            raise ValueError
        else:
            self.models = models
        self.flashes = flashes
        if len(cameras) < 1:
            raise ValueError
        else:
            self.cameras = cameras

    def __repr__(self):
        return f"Scene(id: {self.id}, models: {self.models}, flashes: {self.flashes})"

    def method1(self, type) -> type:
        pass

    def method2(self, type1, type2) -> type:
        pass
