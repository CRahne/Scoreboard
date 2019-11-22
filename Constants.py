# Change Values in here are called in the main file,
# GUI_For_PI_v6.py. By using this file, you can change
# everything in one places.

# Channel Numbers on PI for Buttons
Team1_Add = 23      # Adds One to the Team1 Count
Team2_Add = 25      # Adds One to the Team2 Count
Team1_Sub = 18      # Subtracts One from the Team1 Count
Team2_Sub = 24      # Subtracts One from the Team2 Count
Scoreboard_Reset = 4 # Resets the Scoreboard

# Sets the bouncetime for the buttons (The time before the program will register another press from that button, in milliseconds)
Team1_Add_Bouncetime = 1000
Team2_Add_Bouncetime = 1000
Team1_Sub_Bouncetime = 1000
Team2_Sub_Bouncetime = 1000
Scoreboard_Reset_Bouncetime = 3000                                                                                                                                                                                       

# Tkinter Geometry Configurations
 # Spawnpoints are where the GUI pops up when initialized. They
 # should always be set to 0 (upper left-hand corner)
SpawnPoint_X = 0
SpawnPoint_Y = 0
 # These control the size of the window. If you want full screen,
 # just use the pixel dimensions of the moniter that you are using
Window_Width = 1200
Window_Height = 900

# Window Variables
Window_Background_Color = 'black'
Window_Number_Of_Columns = 3
Window_Column_Weight = 100
Window_Number_Of_Rows = 3
Window_Row_Weight = 100

# Team label 1
# Location of the label in the grid
Team1_Name = "Red"
Team1_Name_Row = 2
Team1_Name_Column = 1
# Adds spacing
Team1_Name_padx = 100
Team1_Name_pady = 100
# Label colors
Team1_Name_Background = 'black'
Team1_Name_Font_Color = 'red'
# Font settings
Team1_Name_Font = 'Consolas' # Any font can be used as long as it is installed
Team1_Name_Font_Size = 45

# Team Label 2
# Location of the label in the grid
Team2_Name = "Blue"
Team2_Name_Row = 2
Team2_Name_Column = 3
# Adds spacing
Team2_Name_padx = 100
Team2_Name_pady = 100
Team2_Name_Background = 'black'
Team2_Name_Font_Color = 'blue'
# Font settings
Team2_Name_Font = 'Consolas' # Any font can be used as long as it is installed
Team2_Name_Font_Size = 45

# Team 1 count
# Location of the label in the grid
Team1_Count_Row = 3
Team1_Count_Column = 1
# Adds spacing
Team1_Count_padx = 0
Team1_Count_pady = 100
Team1_Count_Background = 'black'
Team1_Count_Font_Color = 'red'
# Font settings
Team1_Count_Font = 'Hack' # Any font can be used as long as it is installed
Team1_Count_Font_Size = 120

# Team 2 count
# Location of the label in the grid
Team2_Count_Row = 3
Team2_Count_Column = 3
# Adds spacing
Team2_Count_padx = 0
Team2_Count_pady = 100
Team2_Count_Background = 'black'
Team2_Count_Font_Color = 'blue'
# Font settings
Team2_Count_Font = 'Hack' # Any font can be used as long as it is installed
Team2_Count_Font_Size = 120

# Question (This label uses sticky to stay centered left/right instead of padding)
# Location of the label in the grid
Title_Text = "Title"
Title_Row = 1
Title_Column = 1
Title_Columnspan = 3 # Allows the label to span 3 columns
Title_Background = 'black'
Title_Font_Color = 'gold'
Title_pady = 50
# Font settings
Title_Font = 'Consolas' # Any font can be used as long as it is installed
Title_Font_Size = 60

# Image
# File Name For the Image. Must be .png
Photo_Image_File = "logo.png"
# Location of the image in the grid
Image_Row = 2
Image_Rowspan = 2 # Allows the image to span 2 rows
Image_Column = 2
# Adds spacing
Image_padx = 80
Image_pady = 0
Image_Background = 'black'

# Finish Settings
# Limits for generating a random number for the Finish_Value
# random.randint(Finish_Value_Lower_Limit, Finish_Value_Upper_Limit)
Finish_Value = 10
# Time inbetween screen changes, in seconds
Finish_Flash_Time = 0.5
# The colors that flash when Team1 wins
Finish_Team1_Flash_Font_Color = 'Red'
Finish_Team1_Flash_Background_Color = 'red'
# The colors that flash when Team2 wins
Finish_Team2_Flash_Font_Color = 'blue'
Finish_Team2_Flash_Background_Color = 'blue'