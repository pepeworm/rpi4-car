import RPi.GPIO as GPIO
from pynput.keyboard import Key, Listener
from rich.console import Console

import sys
import os
sys.path.append(os.path.relpath("modules/manual"))

import subprocess
import pathlib

main_path = pathlib.Path(__file__).parent
camera_off_path = main_path.parent.parent / "camera_off.sh"        

# Setup

from setup import *

setup()

from keybinds import *
from uds import *

console = Console()


def controls():
    motor_1_pwm_1 = GPIO.PWM(motor_1_pin_1, 100)
    motor_1_pwm_2 = GPIO.PWM(motor_1_pin_2, 100)
    motor_1_pwm_3 = GPIO.PWM(motor_1_pin_3, 100)
    motor_1_pwm_4 = GPIO.PWM(motor_1_pin_4, 100)
    motor_2_pwm_1 = GPIO.PWM(motor_2_pin_1, 100)
    motor_2_pwm_2 = GPIO.PWM(motor_2_pin_2, 100)
    motor_2_pwm_3 = GPIO.PWM(motor_2_pin_3, 100)
    motor_2_pwm_4 = GPIO.PWM(motor_2_pin_4, 100)

    def motor_pwm_reset():
        GPIO.output([motor_1_pin_1, motor_1_pin_2, motor_1_pin_3, motor_1_pin_4,
                    motor_2_pin_1, motor_2_pin_2, motor_2_pin_3, motor_2_pin_4], GPIO.LOW)

        motor_1_pwm_1.stop()
        motor_1_pwm_2.stop()
        motor_1_pwm_3.stop()
        motor_1_pwm_4.stop()
        motor_2_pwm_1.stop()
        motor_2_pwm_2.stop()
        motor_2_pwm_3.stop()
        motor_2_pwm_4.stop()


    def motor_pwm_start(pin_1, pin_2, pin_3, pin_4, pin_1_dc, pin_2_dc, pin_3_dc, pin_4_dc):
        pin_1.start(pin_1_dc)
        pin_2.start(pin_2_dc)
        pin_3.start(pin_3_dc)
        pin_4.start(pin_4_dc)


    def on_press(key):
        global speed
        global string_key
        global steps

        type_str_key = f"{key}"

        if len(type_str_key) == 3:
            string_key = type_str_key[1:-1]
        else:
            string_key = type_str_key

        if string_key == speed_10:
            motor_pwm_reset()

            speed = 10
            
            console.print(f"[red1 bold]Speed set to {speed}%[/red1 bold]")
        if string_key == speed_20:
            motor_pwm_reset()

            speed = 20

            console.print(f"[red1 bold]Speed set to {speed}%[/red1 bold]")
        if string_key == speed_30:
            motor_pwm_reset()

            speed = 30

            console.print(f"[red1 bold]Speed set to {speed}%[/red1 bold]")
        if string_key == speed_40:
            motor_pwm_reset()

            speed = 40

            console.print(f"[red1 bold]Speed set to {speed}%[/red1 bold]")
        if string_key == speed_50:
            motor_pwm_reset()

            speed = 50

            console.print(f"[red1 bold]Speed set to {speed}%[/red1 bold]")
        if string_key == speed_60:
            motor_pwm_reset()

            speed = 60
            
            console.print(f"[red1 bold]Speed set to {speed}%[/red1 bold]")
        if string_key == speed_70:
            motor_pwm_reset()

            speed = 70

            console.print(f"[red1 bold]Speed set to {speed}%[/red1 bold]")
        if string_key == speed_80:
            motor_pwm_reset()

            speed = 80
            
            console.print(f"[red1 bold]Speed set to {speed}%[/red1 bold]")
        if string_key == speed_90:
            motor_pwm_reset()

            speed = 90
            
            console.print(f"[red1 bold]Speed set to {speed}%[/red1 bold]")
        if string_key == speed_100:
            motor_pwm_reset()

            speed = 100

            console.print(f"[red1 bold]Speed set to {speed}%[/red1 bold]")
        if string_key == forward:
            try:
                motor_pwm_reset()
                motor_pwm_start(motor_1_pwm_2, motor_1_pwm_4,
                                motor_2_pwm_2, motor_2_pwm_4, speed, speed, speed, speed)
            
                console.print(f"[red1 bold]Forward, Speed: {speed}%[/red1 bold]")
            except:
                speed = 100

                console.print(f"[red1 bold]New Speed set to: {speed}%[/red1 bold]")
        if string_key == left:
            try:
                motor_pwm_reset()
                motor_pwm_start(motor_1_pwm_2, motor_1_pwm_4,
                                motor_2_pwm_1, motor_2_pwm_3, speed, speed, speed, speed)
            
                console.print(f"[red1 bold]Left, Speed: {speed}%[/red1 bold]")
            except:
                speed = 100

                console.print(f"[red1 bold]New Speed set to: {speed}%[/red1 bold]")
        if string_key == reverse:
            try:
                motor_pwm_reset()
                motor_pwm_start(motor_1_pwm_1, motor_1_pwm_3,
                                motor_2_pwm_1, motor_2_pwm_3, speed, speed, speed, speed)
                
                console.print(f"[red1 bold]Reverse, Speed: {speed}%[/red1 bold]")
            except:
                speed = 100

                console.print(f"[red1 bold]New Speed set to: {speed}%[/red1 bold]")
        if string_key == right:
            try:
                motor_pwm_reset()
                motor_pwm_start(motor_1_pwm_1, motor_1_pwm_3,
                                motor_2_pwm_2, motor_2_pwm_4, speed, speed, speed, speed)
                
                console.print(f"[red1 bold]Right, Speed: {speed}%[/red1 bold]")
            except:
                speed = 100

                console.print(f"[red1 bold]New Speed set to: {speed}%[/red1 bold]")
        if string_key == stop:
            motor_pwm_reset()
            
            console.print("[red1 bold]Stop[/red1 bold]")
        if string_key == camera_left:
            if (steps <= 12):
                if steps == 7:
                    console.print("[pale_violet_red1 bold]Camera Left, Position: Middle[/pale_violet_red1 bold]")
                elif steps == 1:
                    console.print("[pale_violet_red1 bold]Camera Left, Position: Right[/pale_violet_red1 bold]")
                elif steps == 12:
                    console.print("[pale_violet_red1 bold]Camera Left, Position: Left[/pale_violet_red1 bold]")
                else:
                    console.print("[pale_violet_red1 bold]Camera Left[/pale_violet_red1 bold]")
                    
                p.ChangeDutyCycle(steps)
                time.sleep(0.1)
                p.ChangeDutyCycle(0)
                time.sleep(0.1)
                steps += 1            
        if string_key == camera_right:
            if (steps >= 1):
                if steps == 7:
                    console.print("[pale_violet_red1 bold]Camera Left, Position: Middle[/pale_violet_red1 bold]")
                elif steps == 1:
                    console.print("[pale_violet_red1 bold]Camera Left, Position: Right[/pale_violet_red1 bold]")
                elif steps == 12:
                    console.print("[pale_violet_red1 bold]Camera Left, Position: Left[/pale_violet_red1 bold]")
                else:
                    console.print("[pale_violet_red1 bold]Camera Left[/pale_violet_red1 bold]")
            
                p.ChangeDutyCycle(steps)
                time.sleep(0.1)
                p.ChangeDutyCycle(0)
                time.sleep(0.1)
                steps -= 1
        if string_key == uds_distance:
            console.print(f"[orange1 bold]{get_sonar()}[/orange1 bold]")
            
        
    def on_release(key):
        if key == Key.esc:
            # Reset Servo Position
            
            p.ChangeDutyCycle(2)
            time.sleep(0.3)
            p.stop()
            
            # Stop Motors 
            
            motor_pwm_reset()
            
            # Cleanup GPIO
            
            GPIO.cleanup()
            
            # Turn Camera Off
                        
            subprocess.call(["sh", camera_off_path.resolve()])
            
            # End Keypress Listener
            
            return False


    with Listener(
            on_press=on_press,
            on_release=on_release) as listener:
        listener.join()
