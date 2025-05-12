# RFID-traffic-light.py
import board, time,neopixel
from mfrc522 import MFRC522

# set up rfid
sck = board.GP2
mosi = board.GP3
miso = board.GP4
cs = board.GP5
rst = board.GP6
rfid = MFRC522(sck, mosi, miso, cs, rst)

# set up neopixel
strip = neopixel.NeoPixel(board.GP0,30,brightness=0.5)
BLACK = (0, 0, 0)
GREEN = (0,255,0)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)
strip.fill(BLACK)

# set up UIDs
GO_UID = "D172D6493C"
SLOW_UID = "7173D6499D"
STOP_UID = "11A0D5492D"

# set up functions
def go():
    strip.fill(GREEN)
    time.sleep(1)
    strip.fill(BLACK)

def slow():
    strip.fill(YELLOW)
    time.sleep(1)
    strip.fill(BLACK)

def stop():
    strip.fill(RED)
    time.sleep(1)
    strip.fill(BLACK)

print("\n***** Scan your RFid tag/card *****\n")

while True:
    (status, tag_type) = rfid.request(rfid.REQALL)
    if status == rfid.OK:
        (status, raw_uid) = rfid.anticoll()
        if status == rfid.OK:
            rfid_data = "".join("{:02X}".format(x) for x in raw_uid)
            if rfid_data == GO_UID:
               go()
               print("Go!")
            elif rfid_data == SLOW_UID:
                slow()
                print("Slow down")
            elif rfid_data == STOP_UID:
                stop()
                print("STOP!")
    time.sleep(0.2)
