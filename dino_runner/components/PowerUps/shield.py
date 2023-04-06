from dino_runner.components.PowerUps.power_ups import PowerUp
from dino_runner.utils.constants import SHIELD,SHIELD_TYPE

class Shield(PowerUp):
    def __init__(self):
        self.type = SHIELD_TYPE
        super().__init__(self.type)