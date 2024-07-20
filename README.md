# Arduino and VPython Integration Projects

This repository contains several Python scripts designed to interface with Arduino hardware and visualize data using VPython. Each script demonstrates different functionalities and visualizations. Below is a description of each file and its purpose.

## Files

### 1a. client_server.ino

This sketch demonstrates a basic client-server communication setup using Arduino. It sets up the Arduino as either a client or a server, capable of sending and receiving data over a network. This can be useful for projects requiring remote data transmission or control.

### 1b. client_server.py
  1. This script sets up a serial communication with an Arduino device and reads incoming data packets containing three float values (x, y, z). The script then prints these values to the console.
  2. This script visualizes voltage data from an Arduino using VPython. It reads the potentiometer value from the Arduino, converts it to a voltage, and visualizes it as the length of a blue cylinder.
  3. This script sends user-entered commands to an Arduino via serial communication. It reads the commands from the user, appends a carriage return, and sends them to the Arduino.

### 2a. joystick.ino

This sketch is designed to interface with a joystick. It reads the joystick's position and possibly other inputs like button presses, and processes this data to control other components or send it to another device. The joystick will also be served as a part of the marble game.

### 2b. marble.py 
These scripts create a virtual room using VPython and animate a marble moving within it using the joystick arduino codes. They handle collisions with the walls and the floor and ceiling, and in marble_4.py, a paddle is added for a game-like interaction. The game is controlled by the joystick project earlier. 
<img width="752" alt="Screenshot 2024-07-16 at 14 44 34" src="https://github.com/user-attachments/assets/6e8a24b9-5634-48b2-8129-9eb491cac0b3">

### 3a. RGB.ino

This sketch controls an RGB LED. It allows for setting the LED to different colors by adjusting the red, green, and blue components. This can be useful for visual feedback in various projects.

### 3b. RGB.py 
This script controls an RGB LED connected to an Arduino. It allows the user to input RGB values, which are then sent to the Arduino to set the LED color. The LED's state is visualized using VPython.

### 4. humidity.ino
This sketch might be related to MIDI (Musical Instrument Digital Interface) control. It could be used to send or receive MIDI signals, making it useful for music-related projects or interfacing with MIDI-compatible instruments.

<img width="286" alt="Screenshot 2024-07-16 at 14 39 45" src="https://github.com/user-attachments/assets/d67cddbd-0660-477c-ac42-067dfb2480b2">

### 4a. humidity_1.py
This script reads temperature and humidity data from an Arduino and visualizes it using VPython. It adjusts the length of a cylinder to represent the temperature and updates the display value.
### 4b. humidity_2.py
This script visualize an arrow's movement and a cylinder's length based on temperature and humidity values received from an Arduino. The arrow's angle is adjusted according to the humidity values, and the cylinder represents the temperature.

### 5a. voltmeter.ino
This sketch seems to involve a specific component or sensor, possibly related to voltage measurement or control. It might be used to read voltage levels or control devices based on voltage inputs.
### 5b. voltmeter_1 & voltmeter_2.py
These scripts creates a visual voltmeter using VPython. It reads potentiometer values from the Arduino and adjusts the position of an arrow to indicate the voltage level.

<img width="437" alt="Screenshot 2024-07-16 at 14 42 11" src="https://github.com/user-attachments/assets/abe080e8-7817-4be0-a6f1-d73d67c7f315">

## Getting Started

To use these sketches, follow the steps below:

1. **Install the Arduino IDE**: Download and install the Arduino IDE from [here](https://www.arduino.cc/en/software).
2. **Connect your Arduino**: Connect your Arduino board to your computer using a USB cable.
3. **Open a sketch**: Open one of the `.ino` files in the Arduino IDE.
4. **Upload the sketch**: Select the correct board and port from the `Tools` menu, then click the upload button.
5. **Monitor the output**: Use the Serial Monitor in the Arduino IDE to view any serial output from the Arduino.

## Requirements

- Arduino IDE
- Appropriate Arduino board for your project (e.g., Arduino Uno, Arduino Mega, etc.)
- Any additional components required by the sketches (e.g., joystick, RGB LED, network module)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Thanks to the Arduino community for their continuous support and contributions.

---

For any questions or issues, please open an issue on this repository.
