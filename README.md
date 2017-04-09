# I'm Not A Robot Clicker
A Python Script That Clicks On I'm Not A Robot Boxes 
It is able to get that green checkmark in all of the test i have ran so far
Warning This Program will currently crash if it does not find a captcha box on your screen

# How It Works

The program will take a screenshot it will then save this as temp.png it will then open this with opencv it then scans for any ReCAPTCHA boxes in the image it will then scan for the checkbox it then checks if the checkbox it finds is inside the ReCAPTCHA Box after doing this is finds the center point of the checkbox it then clicks once to give the browser window focus it then clicks again to verify that this is infact not a robot

# where can i find a ReCAPTCHA to test this on

https://www.google.com/recaptcha/api2/demo

# to do

add error checking so it wont crash if no box is found

delete temp files after finishing

