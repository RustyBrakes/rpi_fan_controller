import RPi.GPIO as GPIO
import time
import os

# Setup
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)


"""
The fan curve responds as follows:


  fan speed (as % of fully on) 
     ^
     |
 max -             ............
     |            /  
     |           /
     |          /
     |         /
 min -......../
     |
     |--------|----|-----------> temperature of CPU
             low  high


"""

# Choose values to describe fan response (see graph above)
speed_max=100
speed_min=50
temperature_high=50
temperature_low=40

# Choose output pin and PWM frequency (200Hz seems to have minimal "whine")
pin_number=12
pwm_frequency=200

# Choose number of seconds to wait between each update
sleep_period_seconds=5

# Setup output pin for PWM and start
GPIO.setup(pin_number, GPIO.OUT)
pin_output = GPIO.PWM(pin_number,pwm_frequency)
pin_output.start(50)


def get_cpu_temperature():
    "This function will output the CPU temperature as an integer"
    
    temperature = os.popen('vcgencmd measure_temp').readline()
    temperature = temperature.replace("temp=","").replace("'C\n","")
    temperature = int(float(temperature))    
    return(temperature)


def calculate_fan_speed(temperature):
    "This function will calculate the fan speed based on the input temp."
    "Fan curve follows speed=(m*temp)+c straight line in the active region"

    # Calculate the graph gradient (m) and the y-intercept (c)
    m = (speed_max-speed_min)/(temperature_high-temperature_low)
    c = speed_min-(m*temperature_low)
    
    
    if temperature<temperature_low:
        return(speed_min)
    
    elif temperature>temperature_high:
        return(speed_max)
    
    else:
        return(m*temperature+c)


while True:
    
    temp = get_cpu_temperature()
    pwm_percentage = calculate_fan_speed(temp)
    pin_output.ChangeDutyCycle(pwm_percentage)
    
    print("Temperature =", temp,"'C")
    print("Fan Speed   =", pwm_percentage,"%")
    print()
        
    time.sleep(sleep_period_seconds)
