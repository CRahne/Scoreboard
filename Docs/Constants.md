# Constants Variables

An explanation for all variables in [Constants.py](Constants.py)

---

### Button Pins

These Variables control the GPIO pin values for the buttons on the Raspberry PI.

| Variable Name | Type | Desc                       |
|---------------|------|----------------------------|
| L_Add         | Int  | Left Add Button            |
| L_Sub         | Int  | Left Subtraction Button    |
| R_Add         | Int  | Right Addition Button      |
| R_Sub         | Int  | Right Subtraction Button   |
| Auto_Finish   | Int  | Auto Finish Button         |

---

### Button Bouncetime

The bouncetime is how long the user must wait for the button to be pressed again. This can eliminate the problem of 'Double-Pressing', as it won't allow the user to press the button without waiting a certain amount of time. Kind of like a cooldown for button pressing.

| Variable Name           | Type | Desc                          |
|-------------------------|------|-------------------------------|
| L_Add_Bouncetime        | Int  | Left Add Boncetime            |
| R_Add_Bouncetime        | Int  | Left Subtraction Boncetime    |
| L_Sub_Bouncetime        | Int  | Right Addition Boncetime      |
| R_Sub_Bouncetime        | Int  | Right Subtraction Boncetime   |
| Auto_Finish_Bouncetime  | Int  | Auto Finish Boncetime         |

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

### Window Variables

The window variables change the display of the window. It will also edit some elements of the grid display for the GUI.

| Variable Name              | Type                  | Desc                                       |
|----------------------------|-----------------------|--------------------------------------------|
| Window_Background_Color    | String/Tkinter Color  | Background color of the window             |
| Window_Number_Of_Columns   | Int                   | Number of Columns in the Tkinter Grid      |
| Window_Column_Weight       | Int                   | Default Weight, in pixels, of each column  |
| Window_Number_Of_Rows      | Int                   | Number of Rows in the Tkinter Grid         |
| Window_Row_Weight          | Int                   | Default Weight, in pixels, of each row     |

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

### Finish Settings

Alters the geometry configuration of the window. These variables are passed into the ```tkinter.Tk().geometry()``` method.

| Variable Name   | Type | Desc                                              |
|-----------------|------|---------------------------------------------------|
| SpawnPoint_X    | Int  | The X coordinate of where the window will open    |
| SpawnPoint_Y    | Int  | The Y coordinate of where the window will open    |
| Window_Width    | Int  | The width of the window                           |
| Window_Height   | Int  | The height of the window                          |