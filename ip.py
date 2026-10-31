import network

# --- Wi-Fi credentials: fill in your own before flashing (do NOT commit real ones) ---
WIFI_SSID = "YOUR_WIFI_NAME"
WIFI_PASSWORD = "YOUR_WIFI_PASSWORD"

import socket
from time import sleep

def setup_sta():
    wlan=network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(WIFI_SSID, WIFI_PASSWORD)
    while not wlan.isconnected():
        sleep(1)
    ip_address=wlan.ifconfig()[0]
    print("IP address", ip_address)
    return wlan

setup_sta()