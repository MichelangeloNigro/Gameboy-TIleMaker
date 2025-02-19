import tkinter as tk
import constant
from PIL import ImageGrab, Image, ImageTk
from tilemapTile import *
def createTilemap(app):
    for r in range(18):  
                app.tilemapView.grid_rowconfigure(r, weight=1)  # Allow rows to expand
                for c in range(20):
                    app.tilemapView.grid_columnconfigure(c, weight=1)  # Allow rows to expand
                    # Create the tile graphic (Label widget)
                    tileGraphic = tk.Canvas(
                        app.tilemapView, width=1, height=1, bg="red", bd=0
                    )

                    # Bind the event after the tile is created
                    #tileGraphic.bind("<Button-1>", lambda event, r=r, c=c,k=k: changeTile(self,(r * 16 + c)+(127*k)+(1*k)))
                    
                    # Position the tile in the grid
                    tileGraphic.grid(row=r, column=c, sticky="nsew")
                    tileGraphic.bind("<Button-1>", lambda event: drawTileMapTile(app,event))
                    constant.tileMapReal.append(tilemapTile(tileGraphic,None,None,r,c))



def drawTileMapTile(app,event):
    button = event.widget
    tilemaprealElement = next((t for t in constant.tileMapReal if t.button == button), None)
    img=constant.tileSet[constant.currTileIndex].img
    canvas_width = button.winfo_width()
    canvas_height = button.winfo_height()
    button.delete("all")  # Clears any existing drawing
    # Resize the image to fit the canvas size dynamically
    resized_img = img.resize((canvas_width, canvas_height), Image.Resampling.LANCZOS)
    # Convert the resized image to a PhotoImage object for Tkinter
    tk_resized_img = ImageTk.PhotoImage(resized_img)
    # Apply the resized image as the background
    button.create_image(0, 0, image=tk_resized_img, anchor="nw")
    tilemaprealElement.img=img
    tilemaprealElement.tile=constant.currTileIndex
    tilemaprealElement.hex=constant.tileSet[constant.currTileIndex].hex
    # Prevent garbage collection by keeping a reference to the resized image
    button.image = tk_resized_img
    updateInfo(app,tilemaprealElement)

def updateInfo(app,tile):
      #app.tile_index.config(text=f"{tile.tile} (${hex(tile.tile%256)[2:]}) @VRAM 00:9{tile.tile%256:02x}0")
      app.index.config(text=f"Index:            {constant.tileMapReal.index(tile)+tile.row*12} (${(tile.row*12+constant.tileMapReal.index(tile)):02x}) @ VRAM 00:{(38912+tile.row*12+constant.tileMapReal.index(tile)):02x} | row: {tile.row} | column: {tile.column} ")