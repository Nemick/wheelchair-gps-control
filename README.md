# Smart Wheelchair GPS & Motion Control System

This project demonstrates a Python-based control system for a motorized wheelchair equipped with GPS and GSM modules. It uses a Raspberry Pi to track real-time location and transmit it via GSM while controlling direction with button inputs.

## 🚀 Features

- GPS location reading using serial communication
- Sends SMS with latitude and longitude
- Motor direction control via buttons:
  - Forward
  - Reverse
  - Left
  - Right
- GPIO interfacing with Raspberry Pi
- Sample GPS string parsing

## 🛠 Technologies Used

- Python 3
- Raspberry Pi GPIO (`RPi.GPIO`)
- GSM & GPS modules
- UART serial communication

## 🧪 Circuit Simulation

Below is the simulation of the wheelchair system showing the connection between the Raspberry Pi, GPS, GSM, and motor driver modules:

[Simulation Diagram](wheelchair_simulation_diagram.png)

The design was simulated using Proteus to verify the hardware logic before implementation.


## 📂 Files

- `wheelchair_control.py`: Main script for GPS, GSM, and motor control
- 'wheelchair_simulation_diagram.png' :Simulation Diagram
  
## ⚙️ How It Works

1. Press directional buttons to control the wheelchair
2. GPS coordinates are acquired
3. An SMS message with location is sent using the GSM module

## 📞 SMS Output Example
Latitude: 3014.1985N
Longitude: 09749.2873W


## 🧠 Author

[Nehemiah Kipkoech Kimutai](https://github.com/Nemick)


