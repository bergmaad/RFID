import board
import time
from mfrc522 import MFRC522

sck = board.GP2
mosi = board.GP3
miso = board.GP4
cs = board.GP5
rst = board.GP6

rfid = MFRC522(sck, mosi, miso, cs, rst)

# Check chip version
version = rfid.read_reg(0x37)
print("MFRC522 Version: ", hex(version))
if version == 0x00 or version == 0xFF:
    print("ERROR: MFRC522 not detected. Check wiring or try 5V power.")
    while True:
        pass

print("\n***** Scan your RFid tag/card *****\n")

prev_data = None

while True:
    (status, tag_type) = rfid.request(rfid.REQALL)

    if status == rfid.OK:
        print("Card detected, tag type:", tag_type)

        (status, raw_uid) = rfid.anticoll()

        if status == rfid.OK:
            rfid_data = "{:02x}{:02x}{:02x}{:02x}".format(*raw_uid)
            if rfid_data != prev_data:
                prev_data = rfid_data
                print("Card UID:", rfid_data)

    time.sleep(0.2)
