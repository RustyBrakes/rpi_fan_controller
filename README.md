# rpi_fan_controller
Transistor controlled 5V fan using PWM control programmed in Python 3

What? How? Why?
  This is using a 5V fan to cool the Raspberry Pi 3 CPU and GPU. When running at 5V this tiny thing sounds like a small jet, so I wanted to dynamically adjust the fan speed based on how hot the CPU was getting.
  The method uses a transistor to limit the current across the 5V fan, and the control signal is a PWM output from the Raspberry Pi. This ensures we can have a full speed control without trying to draw too much current from the 3.3V output. See the circuit diagram for details on the hardware setup.
   "Why" is about the most interesting question here. I've seen others who buy these fans to help combat the tropical climates they live in, but I live in England. Really it's just a fun way for me to learn some Python and do some soldering. I've been able to maintain the running temperatures at about 40 degrees C now rather than 50 degrees C, and this is at a very quiet 50% fan speed.
   
DISCLAIMERS!
1. This is my first ever script in Python, so while it does seem to work well for the purpose, those with experience might know much better ways to achieve these things. There may also be a lot of exception handling, thread handling, exit handling etc that I have completely missed, if so, please leave me some direction! I'd love to learn about these things! I'm quite confident that my script is very readable at least.
2. Replicate this at your own risk! The hardware probably isn't perfect either, I haven't really sat down and calculated too much. It works for me so that's what I'm presenting.
3. I've borrowed things from around the internet, so here's a couple of bits of credit that I can remember using: https://hackernoon.com/how-to-control-a-fan-to-cool-the-cpu-of-your-raspberrypi-3313b6e7f92c https://circuitdigest.com/microcontroller-projects/controlling-dc-motor-using-raspberry-pi
