import requests
import i2c_lcd
import socket 

def get_external_ip():
    response = requests.get("http://ifcfg.me")
    if response.status_code == 200:
        return str(response.text)
    else:
        return"Error fetching ext Ip"

def get_local_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    s.connect(("9.9.9.9", 80))

    local_ip = str(s.getsockname()[0])

    s.close()

    return local_ip


def display(ext,local):
    lcd = i2c_lcd.lcd()
    lcd.lcd_clear()
    lcd.lcd_display_string(f"e:{ext}",1)
    lcd.lcd_display_string(f"l:{local}",2)

if __name__=="__main__":
    external_ip = get_external_ip()
    local_ip = get_local_ip()
    display(external_ip, local_ip)
