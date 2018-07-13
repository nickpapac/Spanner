from Testboard import Testboard
from Ifttt import Ifttt
from Spanner import Spanner
import time

#BINARY_FROM = "SPANNER"
TESTBOARD_ID = "2c0019001347343438323536"
IFTTT_ACCESS_TOKEN = "54c8df8cb04da38a34e26ec6da046abf92182de4"

testboard = Testboard(TESTBOARD_ID)
ifttt = Ifttt(IFTTT_ACCESS_TOKEN)

# D7 -> Relay PIN
RELAY_PIN = "D7"

# Cloud Functionality
def validate_network_cmd_on():
    ifttt.buttonOn()

    testboard.digitalWrite(RELAY_PIN, 'HIGH')
    time.sleep(2)

    value = testboard.digitalRead(RELAY_PIN)
    spanner.assertTrue(value)

# Cloud Functionality
def validate_network_cmd_off():
    ifttt.buttonOff()

    testboard.digitalWrite(RELAY_PIN, 'LOW')
    time.sleep(2)

    # check PIN state
    value = testboard.digitalRead(RELAY_PIN)
    spanner.assertTrue(value)

if __name__ == "__main__":

    validate_network_cmd_on()

    time.sleep(2)

    validate_network_cmd_off()
