# Scoreboard

A GUI that works as a scoreboard. It uses the RPi.GPIO module to interface with the buttons that are hooked up to the Raspberry Pi. Then, the program will display the scores of each team on a GUI using the Tkinter module.

---

## Set Up and Installation

### Software

1) `git clone https://github.com/CRahne/Scoreboard.git` into a desired directory on the PI.
2) You can tweak parts of the program in [Constants.py](Constants.py)
3) [Install Python 3](https://www.python.org/downloads/). This will install the tkinter module, the used GUI framework.
4) Run [Scoreboard.py](Scoreboard.py), which is in the root directory

### Wiring
![Something Should Be Here](Docs/WiringDiagram.jpg)

This is a diagram for the Raspberry PI model 4 with a 40 pin layout. You will also need to have a power supply, hdmi output, and connections to a USB mouse and keyboard.

---

## Configuration

### GUI (Window) Size

The settings for the size of the window are near the top of Constants.py. Changing these numbers will change the size of the 
window, but font size, the size of the image, and padding **will not** adjust to fit the new settings, and will have to be
adjusted manually using the padx, pady, and font size variables in Constants.py. To go full screen, get your monitor pixel dimensions/resolution.

### Center Photo

You will need to place the desired photo (which must be .png) into the root directory. Then, you must change the ```Photo_Image_File``` variable in [Constants.py](Constants.py). You may need to adjust other variables, such as padding, to account for the size of the photo.

### Changing Button GPIO Pins

The default pins of the buttons are stored in [Constants.py](Constants.py). They are as follows:

```python
# Channel Numbers on PI for Buttons
Team1_Add = 23      # Adds One to the Team1 Count
Team2_Add = 25      # Adds One to the Team2 Count
Team1_Sub = 24      # Subtracts One from the Team1 Count
Team2_Sub = 18      # Subtracts One from the Team2 Count
Scoreboard_Reset = 4 # Resets the Scoreboard
```

To edit these, you simply need to change the value assigned to the variable.

### Colors

There are many variables in [Constants.py](Constants.py) that relate to this. All of the variables are strings that come standard with the Tkinter module. They can be found [here](https://www.tutorialspoint.com/python/tk_colors.htm).

---

## Files

### [ButtonFactory.py](ButtonFactory.py)
This file is used to set up the buttons and adds event catchers for each button.

### [Constants.py](Constants.py)
This file stores most of the variables used by the program. This keeps most of the values in one spot, making 
customizing the program much easier. The variables that are stored in here are described in [Constants.md](Docs/Constants.md).

### [Scoreboard.py](Scoreboard.py)
This is where the majority of the logic takes place. All GUI setup, updates, and general control is done here.

### [logo.png](logo.png)
This is the default image to be displayed by the program.

### [String_Converter.py](String_Converter.py)
It takes the team strings and converts them to be equal length. The program will determine which one is bigger and then will add spaces to the smaller one.

