import tkinter as tk
from tile import *
from pixel import* 
import constant
def create_first_view(self):
    """Set up the initial layout with grids and palette."""
    # Clear previous widgets
    for widget in self.main_frame.winfo_children():
        widget.destroy()

    # Create the 16x8 grids (left side)
    create_large_grids(self)

    # Separator line between grids and tile selection area
    create_separator(self)

    # Create the 8x8 grid (right side)
    create_small_grid(self)

    # Create 1x4 color palette (right of 8x8 grid)
    create_palette(self)

def create_large_grids(self):
    """Create the 16x8 grids."""
    for k in range(3):  # Create 3 grids in rows 0, 1, 2
        large_grid_frame = tk.Frame(self.main_frame, bg="lightcoral")
        large_grid_frame.grid(row=k, column=0, padx=(10, 20), pady=5, sticky="nsew")  # Allow it to expand
        self.main_frame.grid_rowconfigure(k, weight=1)  # Allow rows to expand
        self.main_frame.grid_columnconfigure(0, weight=1)  # Allow
        for r in range(8):
            large_grid_frame.grid_rowconfigure(r, weight=1)  # Allow rows to expand
        for c in range(16):
            large_grid_frame.grid_columnconfigure(c, weight=1)  # Allow columns to expand
        for r in range(8):  
            for c in range(16):
                # Create the tile graphic (Label widget)
                tileGraphic = tk.Canvas(
                    large_grid_frame, width=1, height=1, bg="white", bd=0
                )

                # Bind the event after the tile is created
                tileGraphic.bind("<Button-1>", lambda event, r=r, c=c,k=k: self.changeTile((r * 16 + c)+(127*k)+(1*k)))
                
                # Position the tile in the grid
                tileGraphic.grid(row=r, column=c, sticky="nsew")
                constant.tileMap.append(tileGraphic)
                # Calculate the index for the 1D array
                
                # Create and append the Tile object
                tile = Tile()
                constant.tileSet.append(tile)


def create_separator(self):
    """Create a separator line."""
    separator = tk.Frame(self.main_frame, width=2, bg="black")  # Thin vertical line
    separator.grid(row=0, column=1, rowspan=3, sticky="ns", padx=(0, 20))  # Runs full height

def create_small_grid(self):
    """Create the 8x8 grid."""
    constant.grid_frame = tk.Frame(self.main_frame, bg="lightblue")  # Store as self.grid_frame
    constant.grid_frame.grid(row=0, column=2, rowspan=3, padx=10, pady=10, sticky="nsew")
    self.main_frame.grid_rowconfigure(0, weight=1)  # Allow rows to expand
    self.main_frame.grid_columnconfigure(2, weight=1)  # All
    for r in range(8):
        constant.grid_frame.grid_rowconfigure(r, weight=1)  # Allow rows to expand
    for c in range(8):
        constant.grid_frame.grid_columnconfigure(c, weight=1)  # Allow columns to expand
 
    constant.currTile.clear()
    for r in range(8):
        for c in range(8):
            pixel = tk.Canvas(constant.grid_frame, relief="solid", bg="white", width=1, height=1)
            pixel.grid(row=r, column=c,sticky="nsew")
            pixel_data = Pixel(pixel, "white")  # Creating an instance of the Pixel class
            constant.currTile.append(pixel_data)
            # Capture the correct row (r) and column (c) for each pixel
            pixel.bind("<Button-1>", lambda event, widget=pixel: self.clickTile(widget))
            pixel.bind("<Button-3>", lambda event, widget=pixel: self.removeTile(widget))


def load_small_grid(self):
    constant.grid_frame = tk.Frame(self.main_frame, bg="lightblue")  # Store as self.grid_frame
    constant.grid_frame.grid(row=0, column=2, rowspan=3, padx=10, pady=10, sticky="nsew")
    self.main_frame.grid_rowconfigure(0, weight=1)  # Allow rows to expand
    self.main_frame.grid_columnconfigure(2, weight=1)  # All
    for r in range(8):
        constant.grid_frame.grid_rowconfigure(r, weight=1)  # Allow rows to expand
    for c in range(8):
        constant.grid_frame.grid_columnconfigure(c, weight=1)  # Allow columns to expand
    constant.currTile.clear()
    toLoad= constant.tileSet[constant.currTileIndex]
    for r in range(8):
        for c in range(8):
            index = r * 8 + c
            pixel = tk.Canvas(constant.grid_frame, width=1, height=1, relief="solid", bg=constant.palette[toLoad.pixels[index]].cget("bg"))
            pixel.grid(row=r, column=c,sticky="nsew")
            pixel_data = Pixel(pixel, constant.palette[toLoad.pixels[index]].cget("bg"))
            pixel_data.paletteNumber= toLoad.pixels[index] # Creating an instance of the Pixel class
            constant.currTile.append(pixel_data)
            # Capture the correct row (r) and column (c) for each pixel
            pixel.bind("<Button-1>", lambda event, widget=pixel: self.clickTile(widget))
            #pixel.bind("<Button-3>", lambda event, widget=pixel: self.removeTile(widget))

def create_palette(self):
    """Create the 1x4 color palette."""
    row_frame = tk.Frame(self.main_frame, bg="lightgreen")
    row_frame.grid(row=0, column=3, rowspan=3, padx=10, pady=10, sticky="nsew")
    row_frame.grid_rowconfigure(0, weight=1)  # Make row 0 expand vertically
    row_frame.grid_columnconfigure(0, weight=1, minsize=100)  # Make colum
    for i in range(4):
        box = tk.Label(row_frame, relief="solid", bg=constant.box_colors[i])
        box.grid(row=i, column=0, sticky="nsew", pady=2)  # Use grid() instead of pack()
        constant.palette.append(box)
        row_frame.grid_rowconfigure(i, weight=1)  # Allow each row to expand vertically

        # Bind left and right click events
        box.bind("<Button-1>", lambda event,i=i: self.on_left_click(i))
        box.bind("<Button-3>", lambda event,i=i: self.on_right_click(event))
