import time
from machine import Pin # type: ignore

relay = Pin(2, Pin.OUT)
relay.on()

def control_relay(ip):
    if ip.startswith('180'):
        relay.off()
        time.sleep(1)
        relay.on()