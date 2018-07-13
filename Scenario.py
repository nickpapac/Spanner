from Testboard import Testboard
from Ifttt import Ifttt
import time

BINARY_FROM = "SPANNER"
TESTBOARD_ID = "200023001347343438323536"
IFTTT_ACCESS_TOKEN = "198caec25a8b0ab77977727cb0699f48b4b0ba37"

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
    print(value)
    if testboard.spanner_assertTrue(value) == 1:
        return 0 #Success
    else:
        return 1 #Failure

# Cloud Functionality
def validate_network_cmd_off():
    ifttt.buttonOff()

    testboard.digitalWrite(RELAY_PIN, 'LOW')
    time.sleep(2)

    # check PIN state
    value = testboard.digitalRead(RELAY_PIN)
    print(value)
    if (testboard.spanner_assertTrue(value) == 0):
        return 0 # Success
    else:
        return 1 # Failure

if __name__ == "__main__":

    run_test(validate_network_cmd_on())

    time.sleep(2)

    #run_test(validate_network_cmd_off())
    print(validate_network_cmd_off())
    print('end')
    
