import tkinter as tk
import constant
from pixel import *
from tile import *
from io_logic import *
def create_first_view(self):
    """Set up the initial layout with grids and palette."""
    # Clear previous widgets
    # for widget in self.main_frame.winfo_children():
    #     widget.destroy()
    # Create the 16x8 grids (left side)
    create_large_grids(self)
    self.frame_2.grid_rowconfigure(0, weight=1)
    self.frame_2.grid_columnconfigure(2, weight=1)
    # Ensure frame_7 expands properly
    self.frame_7.grid_rowconfigure(0, weight=1)
    self.frame_7.grid_rowconfigure(1, weight=1)
    self.frame_7.grid_rowconfigure(2, weight=1)
    self.frame_7.grid_columnconfigure(0, weight=1)

    # # Separator line between grids and tile selection area
    # create_separator(self)

    # Create the 8x8 grid (right side)
    create_small_grid(self)

    # Create 1x4 color palette (right of 8x8 grid)
    create_palette(self)

def create_large_grids(self):
    """Create the 16x8 grids."""
    for k in range(3):  # Create 3 grids in rows 0, 1, 2
        large_grid_frame = tk.Frame(self.frame_7, bg="lightcoral", highlightbackground="black", highlightthickness=2)
        large_grid_frame.grid(row=k, column=0, padx=(10, 20), pady=5, sticky="nsew")  # Allow it to expand
        # self.main_frame.grid_columnconfigure(0, weight=1)  # Allow
        large_grid_frame.grid_rowconfigure(0, weight=1)
        large_grid_frame.grid_columnconfigure(0, weight=1)        
        for r in range(8):
            large_grid_frame.grid_rowconfigure(r, weight=1)  # Allow rows to expand
        for c in range(16):
            large_grid_frame.grid_columnconfigure(c, weight=1)  # Allow columns to expand
        for r in range(8):  
            for c in range(16):
                # Create the tile graphic (Label widget)
                tileGraphic = tk.Canvas(
                    large_grid_frame, width=1, height=1, bg="white", bd=0, highlightthickness=1
                )

                # Bind the event after the tile is created
                tileGraphic.bind("<Button-1>", lambda event, r=r, c=c,k=k: changeTile(self,(r * 16 + c)+(127*k)+(1*k)))
                
                # Position the tile in the grid
                tileGraphic.grid(row=r, column=c, sticky="nsew")
                constant.tileMap.append(tileGraphic)
                # Calculate the index for the 1D array
                
                # Create and append the Tile object
                tile = Tile()
                constant.tileSet.append(tile)
    


def create_separator(self):
    """Create a separator line."""
    separator = tk.Frame(self.main_frame, width=5, bg="black")  # Thin vertical line
    separator.grid(row=0, column=1, rowspan=3, sticky="ns", padx=(0, 20))  # Runs full height

def create_small_grid(self):
    """Create the 8x8 grid."""
    
    # Ensure frame_2 expands
    
    # Create the grid frame inside frame_2
    constant.grid_frame = tk.Frame(self.frame_2, bg="lightblue")  
    constant.grid_frame.grid(row=0, column=2, rowspan=3, padx=10, pady=10, sticky="nsew")

    # Ensure grid_frame expands inside frame_2
    constant.grid_frame.grid_rowconfigure(0, weight=1)
    constant.grid_frame.grid_columnconfigure(0, weight=1)

    constant.currTile.clear()

    # Create the 8x8 grid and make each row/column expand
    for r in range(8):
        constant.grid_frame.grid_rowconfigure(r, weight=1)
        for c in range(8):
            constant.grid_frame.grid_columnconfigure(c, weight=1)
            
            pixel = tk.Canvas(constant.grid_frame, relief="solid", bg="white", width=1, height=1,highlightthickness=0)
            pixel.grid(row=r, column=c, sticky="nsew")  # Stretch to fill
            pixel_data = Pixel(pixel, "white")  # Creating an instance of the Pixel class
            constant.currTile.append(pixel_data)

            # Bind mouse click events
            pixel.bind("<Button-1>", lambda event, widget=pixel: clickTile(widget))
            pixel.bind("<Button-3>", lambda event, widget=pixel: removeTile(widget))


def load_small_grid(self, i):
    constant.grid_frame = tk.Frame(self.frame_2, bg="lightblue")  
    constant.grid_frame.grid(row=0, column=2, rowspan=3, padx=10, pady=10, sticky="nsew")

    # Ensure grid_frame expands inside frame_2
    constant.grid_frame.grid_rowconfigure(0, weight=1)
    constant.grid_frame.grid_columnconfigure(0, weight=1)
    for r in range(8):
        constant.grid_frame.grid_rowconfigure(r, weight=1)  # Allow rows to expand
    for c in range(8):
        constant.grid_frame.grid_columnconfigure(c, weight=1)  # Allow columns to expand
    constant.currTile.clear()
    toLoad= constant.tileSet[i]
    for r in range(8):
        for c in range(8):
            index = r * 8 + c
            pixel = tk.Canvas(constant.grid_frame, width=1, height=1, relief="solid", bg=constant.palette[toLoad.pixels[index]].cget("bg"),highlightthickness=0)
            pixel.grid(row=r, column=c,sticky="nsew")
            pixel_data = Pixel(pixel, constant.palette[toLoad.pixels[index]].cget("bg"))
            pixel_data.paletteNumber= toLoad.pixels[index] # Creating an instance of the Pixel class
            constant.currTile.append(pixel_data)
            # Capture the correct row (r) and column (c) for each pixel
            pixel.bind("<Button-1>", lambda event, widget=pixel: clickTile(widget))
            #pixel.bind("<Button-3>", lambda event, widget=pixel: self.removeTile(widget))

def create_palette(self):
    """Create the 1x4 color palette."""
    # Ensure that frame_3 expands to fill available space
    self.frame_3.grid_rowconfigure(0, weight=1)  # Make row 0 expand vertically
    self.frame_3.grid_columnconfigure(0, weight=1)  # Make column 0 expand horizontally

    # Now, create the row_frame and configure it to expand inside frame_3
    row_frame = tk.Frame(self.frame_3)
    row_frame.grid(padx=1, pady=1, sticky="nsew")

    # Allow row_frame to fill all available space in frame_3
    row_frame.grid_rowconfigure(0, weight=1)  # Allow row 0 in row_frame to expand vertically
    row_frame.grid_columnconfigure(0, weight=1)  # Allow column 0 in row_frame to expand horizontally

    # Create the 2x2 grid of boxes inside row_frame
    for i in range(4):
        row = i // 2  # Determine the row (0 for the first 2, 1 for the next 2)
        col = i % 2   # Determine the column (0 or 1)

        if i == 0:
            box = tk.Label(row_frame, relief="solid", bg=constant.box_colors[i], highlightbackground="red", highlightthickness=1)
        else:
            box = tk.Label(row_frame, relief="solid", bg=constant.box_colors[i],highlightthickness=1)

        box.grid(row=row, column=col, sticky="nsew", pady=2, padx=2)  # Place the box in the calculated row and column
        constant.palette.append(box)

        row_frame.grid_rowconfigure(row, weight=1)  # Allow each row in row_frame to expand vertically
        row_frame.grid_columnconfigure(col, weight=1)  # Allow each column in row_frame to expand horizontally

        # Bind left and right click events
        box.bind("<Button-1>", lambda event, i=i: on_left_click(i, event))
        box.bind("<Button-3>", lambda event, i=i: on_right_click(self,event))

   
    
def on_left_click(i, event):
    """Handle left mouse click on a box."""
    for a in constant.palette:
        a.config(highlightbackground="white")
    widget = event.widget
    widget.config(highlightbackground="red")
    constant.selectedColor = i # Get the background color of the clicked box

def on_right_click(self, event):
    """Handle right mouse click on a box."""
    widget = event.widget  # Get the widget that was clicked
    current_color = widget.cget("bg")  # Get the current background color

    if current_color in constant.box_colors:  # Ensure the color exists in the list
        i = constant.box_colors.index(current_color)  # Find its index
        widget.config(bg=constant.box_colors[(i + 1) % len(constant.box_colors)])  # Set next color
        constant.tileSet[constant.currTileIndex].setPixelsPaletteNumber(constant.currTile)
        for i in range(len(constant.tileSet)):
            if constant.tileSet[i].modified == True:
                reloadTile(self,i)


def clickTile(widget):
    """Handle clicking a pixel (8x8 grid)."""
    for i in range(len(constant.currTile)):
        if constant.currTile[i].widget == widget:
            constant.currTile[i].set_color(constant.selectedColor)  # Change the background color of the clicked tile

def dragTile( event):
    widget = event.widget.winfo_containing(event.x_root, event.y_root)
    if widget in [pixel.widget for pixel in constant.currTile]:
        clickTile(widget)

def removeTile( widget):
    """Handle right-clicking a pixel (8x8 grid)."""
    widget.config(bg="white")  # Change the background color of the clicked tile

def changeTile(self,index):
    # (r * 16 + c)+(127*k)+(1*k)
    if index<256:
            self.tile_index.config(text=f"Tile Index:        {index} (${hex(index)[2:]}) @VRAM 00:8{index:02x}0")
    else:
            self.tile_index.config(text=f"Tile Index:        {index%256} (${hex(index%256)[2:]}) @VRAM 00:9{index%256:02x}0")
    if(constant.editingTile):
        print(index)
        capture_grid(self, constant.grid_frame)
        apply_image_to_tile(self,constant.currTileIndex)
        constant.tileSet[constant.currTileIndex].setPixelsPaletteNumber(constant.currTile)
        constant.tileSet[constant.currTileIndex].modified=True
        constant.currTileIndex= index
        constant.tileSet[constant.currTileIndex].modified=True
        if index<256:
            self.label_3.config(text=f"{index} (${hex(index)[2:]}) @VRAM 00:8{index:02x}0")
            self.tile_index.config(text=f"{index} (${hex(index)[2:]}) @VRAM 00:8{index:02x}0")
            constant.tileSet[constant.currTileIndex].hex=hex(index)[2:]
        else:
            self.label_3.config(text=f"{index%256} (${hex(index%256)[2:]}) @VRAM 00:9{index%256:02x}0")
            self.tile_index.config(text=f"{index%256} (${hex(index%256)[2:]}) @VRAM 00:9{index%256:02x}0")
            constant.tileSet[constant.currTileIndex].hex=hex(index%256)[2:]
        if constant.tileSet[index].modified == False:
            create_small_grid(self)
        else:
            load_small_grid(self, constant.currTileIndex)
    constant.currTileIndex= index
    #createPaletteFile() 
def reloadTile(self,index):
    # (r * 16 + c)+(127*k)+(1*k)
    print(index)
    load_small_grid(self, index)
    constant.tileSet[index].setPixelsPaletteNumber(constant.currTile)
    capture_grid(self, constant.grid_frame)
    apply_image_to_tile(self,index)
    
