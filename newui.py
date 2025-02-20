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
from tilemapLogic import *
constant.app = AppBuilder(path="ui.json")

# Get the primary monitor's height from the monitor list
primary_monitor = get_monitors()[0]  # Assuming the first monitor is the primary monitor

# Set the window's height to the primary monitor's height
#app.tk_1.geometry(f"{int(primary_monitor.width/2)}x{int(primary_monitor.height/2)}")  # width and height based on the primary monitor
def loadPalette():
    load_tileview(None)
    loadPaletteIO()
    for i in range(len(constant.tileSet)):
            if constant.tileSet[i].modified == True:
                constant.currTileIndex=i
                reloadTile(constant.app,i)
def loadTilemapFile():
    load_Tilemap(None)
    loadTilemapFileIO()
    for tile in constant.tileMapReal:
        constant.currTileIndex=tile.tile
        drawTileMapTile(constant.app,constant.tileMapRealGraphic[constant.tileMapReal.index(tile)])
def load_Tilemap(event):
    constant.editingTile=False
    constant.app.frame_1.place(x=1000,y=8700)
    constant.app.frame_8.place(x=0,y=0)
    constant.app.tilmeapPage.place(x=0,y=0)
def load_fullview(event):
    constant.app.frame_8.place(x=1000,y=8700)
def load_tileview(event):
    constant.editingTile=True
    constant.app.frame_8.place(x=0,y=0)
    constant.app.frame_1.place(x=0,y=0)
    constant.app.tilmeapPage.place(x=10000,y=10000)
create_first_view(constant.app)
createTilemap(constant.app)
constant.app.connect_callbacks(globals()) # clicking the button will trigger the on_click function
constant.app.tk_1.bind("<B1-Motion>", dragTile)
constant.app.button_6.bind("<Button-1>",createPaletteFile)
constant.app.mainloop()