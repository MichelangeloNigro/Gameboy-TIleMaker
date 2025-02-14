import tkinter as tk
from screeninfo import get_monitors
import constant
from pixel import *
from tile import *
from io_logic import *
from graphic_tile_view import *
# import the formation library which loads the design for you
from formation import AppBuilder
from screeninfo import get_monitors
app = AppBuilder(path="ui.json")

# Get the primary monitor's height from the monitor list
primary_monitor = get_monitors()[0]  # Assuming the first monitor is the primary monitor

# Set the window's height to the primary monitor's height
#app.tk_1.geometry(f"{int(primary_monitor.width/2)}x{int(primary_monitor.height/2)}")  # width and height based on the primary monitor
def load_Tilemap(event):
    app.frame_8.place(x=1000,y=8700)
def load_fullview(event):
    app.frame_8.place(x=1000,y=8700)
def load_tileview(event):
    app.frame_8.place(x=0,y=0)
create_first_view(app)
app.connect_callbacks(globals()) # clicking the button will trigger the on_click function
app.tk_1.bind("<B1-Motion>", dragTile)
app.button_6.bind("<Button-1>",createPaletteFile )
app.mainloop()