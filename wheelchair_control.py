import RPi.GPIO as GPIO
import time
import pio
import Ports
# Configuration
GPIO.setmode(GPIO.BCM)  # GPIO pins configuration
button_pin = 5
button_pin1 = 6
button_pin2 = 12
button_pin3 = 13
motor_pin1 = 17
motor_pin2 = 18
motor1_pin1 = 27
motor1_pin2 = 22
GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(button_pin1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(button_pin2, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(button_pin3, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(motor_pin1, GPIO.OUT)
GPIO.setup(motor_pin2, GPIO.OUT)
GPIO.setup(motor1_pin1, GPIO.OUT)
GPIO.setup(motor1_pin2, GPIO.OUT)

def get_gps_coordinates():
    GPIO.setwarnings(False)
    pio.uart = Ports.UART()  # Define serial port

    while True:
        data = pio.uart.recv()
        data = "$GPGGA,045252.000,3014.4273,N,09749.0628,W,1,NKLib2rJbj15119U1511AAAA)Y5)5)I$GPRMCMLL&b1MAEQ9EeaQ191Ae]Qe91a]11]1A9Y]1EYE9QY1AMA@EM111)]c$GPGGA,045104.000,3014.1985,N,09749.2873,W,1,09,1.2,211.6,?K&&)bj11AAAA)YI5)A15"
        if data.startswith('$GPGGA'):
            # Split the data into individual parts
            parts = data.split(",")
            if len(parts) >= 5:
                # Extract the latitude and longitude
                latitude = parts[2] + parts[3]
                longitude = parts[4] + parts[5]

                # Return the latitude and longitude
                return latitude, longitude
            else:
                print("Not enough data in GPS string")
        else:
            print("Invalid GPS string")


def send_gsm_message(message):
    GPIO.setwarnings(False)
    pio.uart = Ports.UART()  # Define serial port
    time.sleep(1)
    pio.uart.println("AT")
    time.sleep(1)
    pio.uart.println("AT+CMGF=1")
    time.sleep(1)
    pio.uart.println("AT+CMGS=\"+254715271059\"\r")
    time.sleep(1)
    pio.uart.println(message)
    time.sleep(1)


# Get GPS coordinates
latitude, longitude = get_gps_coordinates()

# Create the message to send
message = "Latitude: " + latitude + "\nLongitude: " + longitude
# Call the function to send GPS coordinates via GSM
send_gsm_message(message)

def forward():
    GPIO.output(motor_pin1, GPIO.LOW)
    GPIO.output(motor_pin2, GPIO.HIGH)
    GPIO.output(motor1_pin1, GPIO.LOW)
    GPIO.output(motor1_pin2, GPIO.HIGH)
# Set the motor to move clockwise (reverse)
def reverse():
    GPIO.output(motor_pin1, GPIO.HIGH)
    GPIO.output(motor_pin2, GPIO.LOW)
    GPIO.output(motor1_pin1, GPIO.HIGH)
    GPIO.output(motor1_pin2, GPIO.LOW)

# Set the motor to move leftwards
def leftwards():
    GPIO.output(motor_pin1, GPIO.LOW)
    GPIO.output(motor_pin2, GPIO.HIGH)
    GPIO.output(motor1_pin1, GPIO.HIGH)
    GPIO.output(motor1_pin2, GPIO.LOW)

# Set the motor to move rightwards
def rightwards():
    GPIO.output(motor_pin1, GPIO.HIGH)
    GPIO.output(motor_pin2, GPIO.LOW)
    GPIO.output(motor1_pin1, GPIO.LOW)
    GPIO.output(motor1_pin2, GPIO.HIGH)

# Test the forward and reverse modes
while (1):
    if GPIO.input(button_pin) == GPIO.LOW:
        forward()
        time.sleep(0.1)
    elif GPIO.input(button_pin1) == GPIO.LOW:
        reverse()
        time.sleep(0.1)
    elif GPIO.input(button_pin2) == GPIO.LOW:
        leftwards()
        time.sleep(0.1)
    elif GPIO.input(button_pin3) == GPIO.LOW:
        rightwards()
        time.sleep(0.1)
    else:
        GPIO.output(motor_pin1, GPIO.LOW)
        GPIO.output(motor_pin2, GPIO.LOW)
        GPIO.output(motor1_pin1, GPIO.LOW)
        GPIO.output(motor1_pin2, GPIO.LOW)
        time.sleep(0.1)
	
