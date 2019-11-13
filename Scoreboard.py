# IMPORTS

 # Standard Library
from tkinter import *                    # GUI Framework
import time                              # For time.sleep()
import random                            # Random Numbers
import RPi.GPIO as GPIO                  # Allows us to interact with Raspberry PI GPIO

 # Custom
from ButtonFactory import ButtonFactory  # A class that will set up the buttons
import Constants                         # Constant Values that will be called in the program
import String_Converter                  # Will change the lengths of strings so that they match


# Gets the finish value from Constants
Finish_Value = Constants.Finish_Value
 

# Creates Root Window Object for the GUI
root = Tk()

# Sets the size and location of the window (In pixels)
root.geometry(f'{Constants.Window_Width}x{Constants.Window_Height}+{Constants.SpawnPoint_X}+{Constants.SpawnPoint_Y}')

# Root Background Colors
root.configure(bg=Constants.Window_Background_Color.lower())

# Creates Grid Object on the Window for placement
# of Labels
mainframe = Frame(root)
# Sets the background color of the frame
mainframe["bg"] = Constants.Window_Background_Color.lower()
# Sets up sticky so that it can be used when placing labels
mainframe.grid(sticky=(N, W, E, S))

# Sets up the columns
mainframe.columnconfigure(Constants.Window_Number_Of_Columns,
                          weight=Constants.Window_Column_Weight)

# Sets up the rows
mainframe.rowconfigure(Constants.Window_Number_Of_Rows,
                       weight=Constants.Window_Row_Weight)

Team_Names = [Constants.Team1_Name, Constants.Team2_Name]
Team_Names = String_Converter.ChangeLengths(Team_Names)


###########
## Row 1 ##
###########

# Sets up the Team1 label and gets the string to be displayed
Team1_Name_Var = StringVar()
Team1_Name_Var.set(Team_Names[0])


# Applies the settings and displays the label
Team1_Name_Label = Label(mainframe,
                      textvariable=Team1_Name_Var,
                      bg=Constants.Team1_Name_Background,
                      fg=Constants.Team1_Name_Font_Color,
                      font=f'{Constants.Team1_Name_Font} {Constants.Team1_Name_Font_Size} bold')

Team1_Name_Label.grid(row=Constants.Team1_Name_Row,
                   column=Constants.Team1_Name_Column,
                   padx=Constants.Team1_Name_padx,
                   pady=Constants.Team1_Name_pady)



# Sets up the image settings and displays the image
PHOTO = PhotoImage(file=Constants.Photo_Image_File)

photo_label = Label(mainframe,
                    image=PHOTO,
                    bg=Constants.Image_Background)
photo_label.grid(row=Constants.Image_Row,
                 rowspan = Constants.Image_Rowspan,
                 column = Constants.Image_Column,
                 sticky = W+E+N+S,
                 padx = Constants.Image_padx,
                 pady=Constants.Image_pady)


# Sets up the Team2 label and gets the string to be displayed
Team2_Name_Var = StringVar()
Team2_Name_Var.set(Team_Names[1])


# Applies the settings and displays the label
Team2_Name_Label = Label(mainframe,
                      textvariable=Team2_Name_Var,
                      bg=Constants.Team2_Name_Background,
                      fg=Constants.Team2_Name_Font_Color,
                      font=f'{Constants.Team2_Name_Font} {Constants.Team2_Name_Font_Size} bold')
Team2_Name_Label.grid(row=Constants.Team2_Name_Row,
                   column=Constants.Team2_Name_Column,
                   padx=Constants.Team2_Name_padx,
                   pady=Constants.Team2_Name_pady)



###########
## Row 2 ##
###########

# Sets up the Team1 Count Variable and Label
Team1_Count = StringVar()
Team1_Count.set('00')

Team1_Count_Label = Label(mainframe,
                     textvariable=Team1_Count,
                     bg=Constants.Team1_Count_Background,
                     fg=Constants.Team1_Count_Font_Color,
                     font=f'{Constants.Team1_Count_Font} {Constants.Team1_Count_Font_Size} bold')
Team1_Count_Label.grid(row=Constants.Team1_Count_Row,
                  column=Constants.Team1_Count_Column,
                  padx=Constants.Team1_Count_padx,
                  pady=Constants.Team1_Count_pady)


# Sets up 2nd Count Variable and Label
Team2_Count = StringVar()
Team2_Count.set("00")

Team2_Count_Label = Label(mainframe,
                     textvariable=Team2_Count,
                     bg=Constants.Team2_Count_Background,
                     fg=Constants.Team2_Count_Font_Color,
                     font=f'{Constants.Team2_Count_Font} {Constants.Team2_Count_Font_Size} bold')
Team2_Count_Label.grid(row=Constants.Team2_Count_Row,
                  column=Constants.Team2_Count_Column,
                  padx=Constants.Team2_Count_padx,
                  pady=Constants.Team2_Count_pady)



###########
## Row 3 ##
###########

# Sets Up Title Label and Variable
Title = StringVar()
Title.set(Constants.Title_Text)

Title_Label = Label(mainframe,
                       textvariable=Title,
                       bg=Constants.Title_Background,
                       fg=Constants.Title_Font_Color,
                       font=f'{Constants.Title_Font} {Constants.Title_Font_Size} bold')
Title_Label.grid(row=Constants.Title_Row,
                    column=Constants.Title_Column,
                    columnspan = Constants.Title_Columnspan,
                    pady=Constants.Title_pady,
                    sticky=W+E) # Centers the title lable



# Runs whenever a button is pressed (Other than Scoreboard_Reset)
def buttonPress(channel):
    
    # Accesses the Finish_Value
    global Finish_Value
    
    # If the Team1 count is at the Finish Value
    if (int(Team1_Count.get()) == Finish_Value):
        Team1_Win(channel)
    # If the Team2 count is at the Finish Value
    elif(int(Team2_Count.get()) == Finish_Value):
        Team2_Win(channel)
    
    # Adds One to Team1 Count
    elif channel == Constants.Team1_Add:
        Team1_Count.set(convert_number(int(Team1_Count.get()) + 1))
    
    # Adds one to Team2 Count
    elif channel == Constants.Team2_Add: 
        Team2_Count.set(convert_number(int(Team2_Count.get()) + 1))
    
    # Subtracts one from Team1 Count
    elif (channel == Constants.Team1_Sub) and (int(Team1_Count.get()) > 0):
        Team1_Count.set(convert_number(int(Team1_Count.get()) - 1))
    
    # Subtracts one from Team2 Count
    elif(channel == Constants.Team2_Sub) and (int(Team2_Count.get()) > 0):
        Team2_Count.set(convert_number(int(Team2_Count.get()) - 1))



# Runs when the Reset Button is pressed
# Resets the numbers
def Reset_Scores(channel):
    
    # Resets the values of both counts
    Team1_Count.set('00')
    Team2_Count.set('00')
    

# Runs when Team1_Count is equal to Finsh_Value
def Team1_Win(channel):
    
    # Makes the screen flash twice using a for loop counter
    for x in range(2):
        Flash(Constants.Finish_Team1_Flash_Font_Color,
              Constants.Finish_Team1_Flash_Background_Color)


def Team2_Win(channel):
    
    # Makes the screen flash twice using a for loop counter
    for x in range(2):
        Flash(Constants.Finish_Team2_Flash_Font_Color,
              Constants.Finish_Team2_Flash_Background_Color)
        
        

# Changes the color of the text and background
def Flash(color_fg, color_bg):
    # Question
    Title_Label.config(fg=color_fg, bg=color_bg)
    
    # Counts
    Team1_Count_Label.config(fg=color_fg, bg=color_bg)
    Team2_Count_Label.config(fg=color_fg, bg=color_bg)
    
    # Answers
    Team1_Name_Label.config(fg=color_fg, bg=color_bg)
    Team2_Name_Label.config(fg=color_fg, bg=color_bg)
    
    # Photo
    photo_label.config(bg=color_bg)
    
    # Window
    mainframe["bg"] = color_bg
    root.configure(bg=color_bg)
    
    # Will stop for a bit and then turn back.
    time.sleep(Constants.Finish_Flash_Time)    
    Revert_Colors()
    time.sleep(Constants.Finish_Flash_Time)



# This changes the colors back on the screen to the original
# colors.
def Revert_Colors():
    
    # Question Label
    Title_Label.config(fg=Constants.Title_Font_Color,
                          bg=Constants.Title_Background)
    
    # Count Labels
    Team1_Count_Label.config(fg=Constants.Team1_Count_Font_Color,
                        bg=Constants.Team1_Count_Background)
    
    Team2_Count_Label.config(fg=Constants.Team2_Count_Font_Color,
                        bg=Constants.Team2_Count_Background)
    
    #Answer Labels
    Team1_Name_Label.config(fg=Constants.Team1_Name_Font_Color,
                         bg=Constants.Team1_Name_Background)
    
    Team2_Name_Label.config(fg=Constants.Team2_Name_Font_Color,
                         bg=Constants.Team2_Name_Background)
    
    
    # Photo Label
    photo_label.config(bg=Constants.Image_Background)
    
    
    # Window Backgrounds
    mainframe["bg"] = Constants.Window_Background_Color
    root.configure(bg=Constants.Window_Background_Color)



# Will take the parameter num and if it is only one digit,
# the program will add a zero in front of it. It will return
# the value as a string
def convert_number(num):
    if num <= 9:
        return f'0{num}'
    return str(num)



# Sets up GPIO for channel reference. For BOARD vs BCM, Look Here:
# https://raspberrypi.stackexchange.com/questions/12966/what-is-the-difference-between-board-and-bcm-for-gpio-pin-numbering
GPIO.setmode(GPIO.BCM)



# Sets Up Buttons with the ButtonFactory Class in
# ButtonFactory.py. This will use values from
# Constants.py

ButtonFactory(Constants.Team1_Add, buttonPress,           # Team1 Adding Button
              Constants.Team1_Add_Bouncetime)
 
ButtonFactory(Constants.Team2_Add, buttonPress,           # Team2 Adding Button
              Constants.Team2_Add_Bouncetime)

ButtonFactory(Constants.Team1_Sub, buttonPress,           # Team1 Subtraction Button
              Constants.Team1_Sub_Bouncetime)

ButtonFactory(Constants.Team2_Sub, buttonPress,           # Team2 Subtraction Button
              Constants.Team2_Sub_Bouncetime)

ButtonFactory(Constants.Scoreboard_Reset, Reset_Scores,          # Scoreboard Reset Button
              Constants.Scoreboard_Reset_Bouncetime)



# Sets up a loop to update the GUI
root.mainloop()