import requests
import i2c_lcd
import socket 
import RPi.GPIO as GPIO
import time
from datetime import datetime
from random import choice

QUOTES = [
        ('Stop looking','4 excuses'),
        ('aim 4 mastery','dont settle'),
        ('consistence >>>','perfection'),
        ('persistence >>>','perfection'),
        ('keep showing up!',' ')
        ]
lcd = i2c_lcd.lcd()
lcd.lcd_clear()


def get_external_ip()->str:
    response = requests.get("http://ifconfig.me")
    if response.status_code == 200:
        return str(response.text)
    else:
        return"Error fetching ext Ip"

def get_local_ip()->str:
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("9.9.9.9", 80))
    local_ip = str(s.getsockname()[0])
    s.close()
    return local_ip

def turn_off():
    lcd = i2c_lcd.lcd()
    lcd.backlight_on(False)

def display(msg1, msg2):
    lcd = i2c_lcd.lcd()
    lcd.lcd_clear()
    lcd.lcd_display_string(f"{msg1}",1)
    lcd.lcd_display_string(f"{msg2}",2)

def get_datetime()->tuple:
    date = datetime.now().date()
    curr_time = time.localtime()
    return (time.strftime("%H:%M EST", curr_time), str(date))

def change_display(ev=None):
    global mode_idx
    global MODES
    mode_idx = (mode_idx + 1) % len(MODES)
    curr_mode = MODES[mode_idx]
    curr_mode()

def display_ip():
    ext = get_external_ip()
    local = get_local_ip()
    display(ext, local)

def display_time():
    curr_time,date = get_datetime()
    display(curr_time,date)

def display_reminder():
    line1,line2 = choice(QUOTES)
    display(line1,line2)

if __name__=="__main__":
    MODES = [display_ip, display_time, display_reminder, turn_off]
    
    GPIO.setmode(GPIO.BCM)

    GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    mode_idx = 0
    GPIO.add_event_detect(17, GPIO.FALLING, callback=change_display, bouncetime=300)
    #GPIO.add_event_detect(17, GPIO.BOTH, callback=turn_off, bouncetime)
    while True:
        time.sleep(10)
