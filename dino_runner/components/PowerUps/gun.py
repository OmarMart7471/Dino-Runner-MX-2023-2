from dino_runner.components.PowerUps.power_ups import PowerUp
from dino_runner.utils.constants import GUN,GUN_TYPE
class Gun(PowerUp):
    def __init__(self):
        self.image = GUN
        self.type = GUN_TYPE
        super().__init__(self.image,self.type)