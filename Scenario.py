
from Tester import Tester
from Spannerpi import Spannerpi
from Ifttt import Ifttt
import time
import json

BINARY_FROM = "DESPLOY"
DEVICE_ID = "340040000f51353532343635"
ACCESS_TOKEN = "9e4c2afdbe47d87956ac7795e7287aa8c85e697b"

my_tester = Tester('340040000f51353532343635')
my_spannerpi = Spannerpi()
my_ifttt = Ifttt()

# D5 -> green led
# D1 -> blue led
# D3 -> button

# Basic Functionality
def B1_validate_button_press():
    # button pres    
    my_tester.digitalWrite("OUTPUT", "D3", "LOW")
    my_tester.setPinMode("D1", "INPUT")
    # check blue led state
    res = my_tester.digitalRead("D1")
    print (my_tester.getResult())
    # print (json.loads(res.decode('utf8').replace("'", '"'))["return_value"])
    return 0

# Network Tests
def N1_validate_wifi_connect():
    result = my_spannerpi.connect()
    print (result)

    time.sleep(4)    
    
    # check green led state
    my_tester.setPinMode("D5", "INPUT")
    value = my_tester.digitalRead("D5")

    print (value)
    return 0

# Network Tests
def N3_validate_wifi_reconnect():
    result = my_spannerpi.disconnect()
    time.sleep(2)    
    result = my_spannerpi.connect() 
    time.sleep(4)    
    # check green led state
    value = my_tester.digitalRead("D5")
    print (value)
    return 0

# Network Tests
def N2_validate_wifi_disconnect():
    result = my_spannerpi.disconnect()
    time.sleep(4)    
    # check green led blinking state
    for i in range(0, 10):
        value = my_tester.digitalRead("D5")
        time.sleep(0.05)    
        print (value)
    return 0


# Cloud Functionality
def C1_validate_ifttt_buttonOn():
    my_ifttt.buttonOn()
    time.sleep(2) 
    # check blue led state
    value = my_tester.digitalRead("D1")
    print (value)
    return 0

# Cloud Functionality
def C2_validate_ifttt_buttonOff():
    my_ifttt.buttonOff()
    time.sleep(2)     
    # check blue led state
    value = my_tester.digitalRead("D1")
    print (value)
    return 0

if __name__ == "__main__":
    # EXEC_TEST_CASE(B1_validate_button_press())
#    EXEC_TEST_CASE(N1_validate_wifi_connect())
    # EXEC_TEST_CASE(N2_validate_wifi_disconnect())
    # EXEC_TEST_CASE(N3_validate_wifi_reconnect())
    EXEC_TEST_CASE(C2_validate_ifttt_buttonOff())
    EXEC_TEST_CASE(C1_validate_ifttt_buttonOn())



