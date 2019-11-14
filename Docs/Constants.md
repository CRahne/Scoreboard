# Constants Variables

An explanation for all variables in [Constants.py](Constants.py). As a note, all variable with a type of [Color](https://www.google.com/search?q=tkinter+colors&oq=tkinter+colors&aqs=chrome.0.69i59j0l4j69i60.1914j0j7&sourceid=chrome&ie=UTF-8) or [Font](http://www.scoberlin.de/content/media/http/informatik/tkinter/x444-fonts.htm) must use one that is supported by the Tkinter package.

---

### Button Pins

These Variables control the GPIO pin values for the buttons on the Raspberry PI.

| Variable Name      | Type | Desc                       |
|--------------------|------|----------------------------|
| Team1_Add          | Int  | Left Add Button            |
| Team1_Sub          | Int  | Left Subtraction Button    |
| Team2_Add          | Int  | Right Addition Button      |
| Team2_Sub          | Int  | Right Subtraction Button   |
| Scoreboard_Reset   | Int  | Auto Finish Button         |

---

### Button Bouncetime

The bouncetime is how long the user must wait for the button to be pressed again. This can eliminate the problem of 'Double-Pressing'. It acts as a cooldown, as it won't allow the user to press the button without waiting a certain amount of time.

| Variable Name               | Type | Desc                                        |
|-----------------------------|------|---------------------------------------------|
| Team1_Add_Bouncetime        | Int  | Left Add Bouncetime (milliseconds)          |
| Team2_Add_Bouncetime        | Int  | Left Subtraction Bouncetime (milliseconds)  |
| Team1_Sub_Bouncetime        | Int  | Right Addition Bouncetime (milliseconds)    |
| Team2_Sub_Bouncetime        | Int  | Right Subtraction Bouncetime (milliseconds) |
| Scoreboard_Reset_Bouncetime | Int  | Auto Finish Bouncetime (milliseconds)       |

---

### Window Variables

The window variables change the display of the window. It will also edit some elements of the grid display for the GUI.

| Variable Name              | Type    | Desc                                                     |
|----------------------------|---------|----------------------------------------------------------|
| Window_Background_Color    | Color   | Background color of the window. Must be Tkinter Color    |
| Window_Number_Of_Columns   | Int     | Number of Columns in the Tkinter Grid                    |
| Window_Column_Weight       | Int     | Default Weight, in pixels, of each column                |
| Window_Number_Of_Rows      | Int     | Number of Rows in the Tkinter Grid                       |
| Window_Row_Weight          | Int     | Default Weight, in pixels, of each row                   |

---

### Tkinter Geometry

Alters the geometry configuration of the window. These variables are passed into the ```tkinter.Tk().geometry()``` method.

| Variable Name   | Type | Desc                                              |
|-----------------|------|---------------------------------------------------|
| SpawnPoint_X    | Int  | The X coordinate of where the window will open    |
| SpawnPoint_Y    | Int  | The Y coordinate of where the window will open    |
| Window_Width    | Int  | The width of the window                           |
| Window_Height   | Int  | The height of the window                          |

---

### Team 1 Label (Left)

These variables set up the label with the Team 1 name. All of these variables are linked to settings to tkinter.Label(). 

| Variable Name           | Type    | Desc                                                   |
|-------------------------|---------|--------------------------------------------------------|
| Team1_Name              | String  | The name of the team that will pop up on the screen    |
| Team1_Name_Row          | Int     | Row number where the Label is placed on the grid       |
| Team1_Name_Column       | Int     | Column number where the Label is placed on the grid    |
| Team1_Name_padx         | Int     | The padding along the x axis for the Label             |
| Team1_Name_pady         | Int     | The padding along the y axis for the Label             |
| Team1_Name_Background   | Color   | Background color of the area with the Label in it      |
| Team1_Name_Font_Color   | Color   | Font Color of the Label Text                           |
| Team1_Name_Font         | Font    | The font family of the Label text                      |
| Team1_Name_Font_Size    | Int     | Font Size of the Label Text                            |

---

### Team 2 Label (Right)

These variables set up the label with the Team 2 name. All of these variables are linked to settings to tkinter.Label(). 

| Variable Name           | Type    | Desc                                                   |
|-------------------------|---------|--------------------------------------------------------|
| Team2_Name              | String  | The name of the team that will pop up on the screen    |
| Team2_Name_Row          | Int     | Row number where the Label is placed on the grid       |
| Team2_Name_Column       | Int     | Column number where the Label is placed on the grid    |
| Team2_Name_padx         | Int     | The padding along the x axis for the Label             |
| Team2_Name_pady         | Int     | The padding along the y axis for the Label             |
| Team2_Name_Background   | Color   | Background color of the area with the Label in it      |
| Team2_Name_Font_Color   | Color   | Font Color of the Label Text                           |
| Team2_Name_Font         | Font    | The font family of the Label text                      |
| Team2_Name_Font_Size    | Int     | Font Size of the Label Text                            |

---

### Team 1 Count (Left)

These variables set up the label with the Team 1 Counter. All of these variables are linked to settings to tkinter.Label(). 

| Variable Name            | Type    | Desc                                                   |
|--------------------------|---------|--------------------------------------------------------|
| Team1_Count_Row          | Int     | Row number where the Label is placed on the grid       |
| Team1_Count_Column       | Int     | Column number where the Label is placed on the grid    |
| Team1_Count_padx         | Int     | The padding along the x axis for the Label             |
| Team1_Count_pady         | Int     | The padding along the y axis for the Label             |
| Team1_Count_Background   | Color   | Background color of the area with the Label in it      |
| Team1_Count_Font_Color   | Color   | Font Color of the Label Text                           |
| Team1_Count_Font         | Font    | The font family of the Label text                      |
| Team1_Count_Font_Size    | Int     | Font Size of the Label Text                            |

---

### Team 2 Count (Right)

These variables set up the label with the Team 2 Counter. All of these variables are linked to settings to tkinter.Label(). 

| Variable Name            | Type    | Desc                                                   |
|--------------------------|---------|--------------------------------------------------------|
| Team2_Count_Row          | Int     | Row number where the Label is placed on the grid       |
| Team2_Count_Column       | Int     | Column number where the Label is placed on the grid    |
| Team2_Count_padx         | Int     | The padding along the x axis for the Label             |
| Team2_Count_pady         | Int     | The padding along the y axis for the Label             |
| Team2_Count_Background   | Color   | Background color of the area with the Label in it      |
| Team2_Count_Font_Color   | Color   | Font Color of the Label Text                           |
| Team2_Count_Font         | Font    | The font family of the Label text                      |
| Team2_Count_Font_Size    | Int     | Font Size of the Label Text                            |

### Finish Settings

Variables that control when the scoreboard stops counting, and the flash colors. These variables are passed into the ```tkinter.Tk().geometry()``` method.

| Variable Name                         | Type    | Desc                                              |
|---------------------------------------|---------|---------------------------------------------------|
| Finish_Value                          | Int     | The value at which the counts will stop updating  |
| Finish_Flash_Time                     | Int     | Time each flash will last (seconds)               |
| Finish_Team1_Flash_Font_Color         | Color   | Font color that flashes when Team 1 wins          |
| Finish_Team1_Flash_Background_Color   | Color   | Background color that flashes when Team 1 wins    |
| Finish_Team2_Flash_Font_Color         | Color   | Font color that flashes when Team 2 wins          |
| Finish_Team2_Flash_Background_Color   | Color   | Background color that flashes when Team 2 wins    |