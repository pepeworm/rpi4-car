import RPi.GPIO as GPIO

# Start Up Camera

import subprocess

# subprocess.call(["sh", "./camera_off.sh"])
# subprocess.call(["sh", "./camera_on.sh"])

import sys
import os
sys.path.append(os.path.relpath("modules/manual"))
from keypress_control import *

# Keypress Controls

controls()
