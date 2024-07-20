# ~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~
#      /\_/\
#     ( o.o )
#      > ^ <
#
# Author: Johan Hanekom
# Date: July 2024
# ~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~

import os
from dotenv import load_dotenv
load_dotenv()

# =======================// DIMENSION SETTINGS //======================= #

SPRITE_WIDTH: int = int(os.getenv('SPRITE_WIDTH', 40))
SPRITE_HEIGHT: int = int(os.getenv('SPRITE_HEIGHT', 40))

CANVAS_WIDTH: int = int(os.getenv('CANVAS_WIDTH', 1280))
CANVAS_HEIGHT: int = int(os.getenv('CANVAS_HEIGHT', 720))
