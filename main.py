from config import ssid, password
from connection import connect_wifi
from relay import control_relay
from find_ip import get_public_ip
import time

if __name__ == "__main__":
    connect_wifi(ssid, password)
    
    while True:
        public_ip = get_public_ip()
        control_relay(public_ip)
        
        time.sleep(1)