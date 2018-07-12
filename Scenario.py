from Spanner import Spanner
from Testboard import Testboard
import Device 
import time

DEVICE_ID = "2c0019001347343438323536"
DEVICE_TOKEN = "198caec25a8b0ab77977727cb0699f48b4b0ba37"
device = Device.Particle(DEVICE_ID, DEVICE_TOKEN)

TESTBOARD_ID = "2c0019001347343438323536"
testboard = Testboard(TESTBOARD_ID)

# Our device's Output Pin will be connected to the Testboard's D7, making it our Input Pin
INPUT_PIN = "D7"

def test_switch_on_network_cmd():
    # send network command to our device
  # '3'  device.ota_local("/path/to/test.bin") -> valid only for CLI 
  # '2'  device.ota(test.bin) --> "taken from spanner user profile"
  # '1'  device.ota(auto) -> taken from BF
    
    # device.ota(auto) -> taken from BF
    # time.sleep(2)

    # check PIN state
    value = testboard.digitalRead(INPUT_PIN)
    print(value)
    res = spanner.assertTrue(value)
    print(res)
    
if __name__ == "__main__":
    test_switch_on_network_cmd()
    print('end')
