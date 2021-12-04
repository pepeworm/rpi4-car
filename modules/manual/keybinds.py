import RPi.GPIO as GPIO
from rich.prompt import Prompt

keybind = Prompt.ask("\n[magenta bold]Pick a setting to control the car direction (Forward, Left, Reverse, Right, Stop), camera positions (Left, Right), UDS (Get Distance) and Speed (10% - 100%)[/magenta bold]\n\n[green]A: W, A, S, D, Q + ArrowLeft, ArrowRight + R + 1, 2, 3, 4, 5, 6, 7, 8, 9, 0\nB: W, A, R, S, Q + ArrowLeft, ArrowRight + P + 1, 2, 3, 4, 5, 6, 7, 8, 9, 0\nC: Custom[/green]\n\n", choices=["A", "B", "C"], default="B")


def keybind_keys(key_mode):
    global keys
    global custom_keys

    keys = False
    custom_keys = False

    if key_mode == "A":
        keys = ["w", "a", "s", "d", "q", "Key.left", "Key.right",
                "r", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    elif key_mode == "B":
        keys = ["w", "a", "r", "s", "q", "Key.left", "Key.right",
                "p", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    else:
        order = ["move car forward", "move car left", "reverse car",
                 "move car right", "stop car", "turn camera left", "turn camera right", "get distance with the UDS", "set speed to 10%", "set speed to 20%", "set speed to 30%", "set speed to 40%", "set speed to 50%", "set speed to 60%", "set speed to 70%", "set speed to 80%", "set speed to 90%", "set speed to 100%"]
        key_options = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
                       "v", "w", "x", "y", "z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "Key.up", "Key.left", "Key.right", "Key.down"]
        custom_keys = []

        for i in range(0, len(order), 1):
            custom_key = Prompt.ask(
                f"\n[blue bold]Enter a key to {order[i]}[/blue bold]\n\n", choices=key_options)

            key_options.pop(key_options.index(custom_key))
            custom_keys.append(custom_key)


keybind_keys(keybind)

global forward
global left
global reverse
global right
global stop
global camera_left
global camera_right
global uds_distance

if keys is False:
    forward = custom_keys[0]
    left = custom_keys[1]
    reverse = custom_keys[2]
    right = custom_keys[3]
    stop = custom_keys[4]
    camera_left = custom_keys[5]
    camera_right = custom_keys[6]
    uds_distance = custom_keys[7]
    speed_10 = custom_keys[8]
    speed_20 = custom_keys[9]
    speed_30 = custom_keys[10]
    speed_40 = custom_keys[11]
    speed_50 = custom_keys[12]
    speed_60 = custom_keys[13]
    speed_70 = custom_keys[14]
    speed_80 = custom_keys[15]
    speed_90 = custom_keys[16]
    speed_100 = custom_keys[17]
else:
    forward = keys[0]
    left = keys[1]
    reverse = keys[2]
    right = keys[3]
    stop = keys[4]
    camera_left = keys[5]
    camera_right = keys[6]
    uds_distance = keys[7]
    speed_20 = keys[9]
    speed_10 = keys[8]
    speed_30 = keys[10]
    speed_40 = keys[11]
    speed_50 = keys[12]
    speed_60 = keys[13]
    speed_70 = keys[14]
    speed_80 = keys[15]
    speed_90 = keys[16]
    speed_100 = keys[17]
