import RPi.GPIO as GPIO

# Motor

[motor_1_pin_1, motor_1_pin_2, motor_1_pin_3, motor_1_pin_4, motor_2_pin_1,
    motor_2_pin_2, motor_2_pin_3, motor_2_pin_4] = [17, 27, 23, 24, 5, 6, 26, 16]

# Servo

servo_pin = 18
steps = 2

# UDS

trig_pin = 25
echo_pin = 22
max_distance = 220
timeout = max_distance * 60

# Setup GPIO


def setup():
    GPIO.setmode(GPIO.BCM)

    # Servo

    global p

    GPIO.setup(servo_pin, GPIO.OUT)
    GPIO.output(servo_pin, GPIO.LOW)

    p = GPIO.PWM(servo_pin, 50)
    p.start(0)

    # Motor

    GPIO.setup([motor_1_pin_1, motor_1_pin_2, motor_1_pin_3, motor_1_pin_4,
               motor_2_pin_1, motor_2_pin_2, motor_2_pin_3, motor_2_pin_4], GPIO.OUT)

    # UDS

    GPIO.setup(trig_pin, GPIO.OUT)
    GPIO.setup(echo_pin, GPIO.IN)
    
