from HomeWork1.ModelElements.polygonal_model import PolygonalModel
from HomeWork1.ModelElements.flash import Flash
from HomeWork1.ModelElements.camera import Camera
from HomeWork1.ModelElements.scene import Scene
from HomeWork1.InMemoryModel.IModelChanger import IModelChanger
from HomeWork1.InMemoryModel.IModelChangedObserver import IModelChangedObserver
class ModelStore(IModelChanger):
    def __init__(self, changedObserver: IModelChangedObserver):
        self.models = []
        self.scenes = []
        self.flashes = []
        self.cameras = []
        self.__changedObserver = changedObserver

        self.models.append(PolygonalModel(None))
        self.flashes.append(Flash())
        self.cameras.append(Camera())
        self.scenes.append(Scene(0, self.models, self.flashes, self.cameras))

    def get_scene(self, id: int):
        for i in range(len(self.scenes)):
            if self.scenes[i].id == id:
                return self.scenes[i]
        return None

    def notify_change(self, sender):
        pass


