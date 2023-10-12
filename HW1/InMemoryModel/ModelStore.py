from abc import ABC

from HW1.ModelElements.polygonalmodel import PoligonalModel
from HW1.ModelElements.scene import Scene
from HW1.ModelElements.flash import Flash
from HW1.ModelElements.camera import Camera
from .IModelChanger import IModelChanger
from .IModelChangedObserver import IModelChangedObserver


class ModelStore(IModelChanger):
    def ApplyUpdateModel(self):
        pass

    def NotifyChange(self):
        pass

    i_model_changed_observer: list[IModelChangedObserver]
    models: list[PoligonalModel]
    scenes: list[Scene]
    flashes: list[Flash]
    cameras: list[Camera]

    def __init__(self, models, scenes, flashes, cameras, i_model_changed_observer):
        self.i_model_changed_observer = i_model_changed_observer
        self.models = []
        for model in models:
            self.models.append(PoligonalModel(model[0], model[1], model[2]))
        self.scenes = []
        for scene in scenes:
            self.scenes.append(Scene(scene[0], scene[1], scene[2], scene[3]))
        self.flashes = []
        for flash in flashes:
            self.flashes.append(Flash(flash[0], flash[1], flash[2], flash[3]))
        self.cameras = []
        for camera in cameras:
            self.cameras.append(Camera(camera[0], camera[1]))

    def __repr__(self):
        return (f"ModelStore(models: {self.models}, "
                f"scenes: {self.scenes}, "
                f"flashes: {self.flashes}, "
                f"cameras: {self.cameras})")

    def get_scenes(self, scene_id) -> Scene:
        return self.scenes[scene_id]
