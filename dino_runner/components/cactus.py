import random
from dino_runner.components.obstacle import Obstacle
from dino_runner.utils.constants import SMALL_CACTUS,LARGE_CACTUS

class Cactus(Obstacle):
    Y_POS_CACTUS = 300
    CACTUS = {
    "smallcactus": SMALL_CACTUS,
    "largecactus": LARGE_CACTUS
    }
    def __init__(self):
        tipo_cactus = random.choice(["smallcactus", "largecactus"])
        if tipo_cactus == "smallcactus": self.Y_POS_CACTUS=325
        self.image = random.choice(self.CACTUS[tipo_cactus])
        super().__init__(self.image)
        self.rect.y = self.Y_POS_CACTUS