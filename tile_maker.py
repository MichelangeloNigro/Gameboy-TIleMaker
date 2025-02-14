import tkinter as tk
from screeninfo import get_monitors
import constant
from pixel import *
from tile import *
from io_logic import *
from graphic_tile_view import *
#   ld a, %11100100
#     ld [rBGP], a
#     ld a, %11100100
#     ld [rOBP0], a

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Gameboy Tile Manager")
        # === Navigation Panel (Left Side) ===
        # Get the primary monitor's height from the monitor list
        primary_monitor = get_monitors()[0]  # Assuming the first monitor is the primary monitor

        # Set the window's height to the primary monitor's height
        self.geometry(f"{int(primary_monitor.width/2)}x{int(primary_monitor.height/2)}")  # width and height based on the primary monitor

        # Create navigation frame
        self.nav_frame = tk.Frame(self, width=200, bg="gray")
        self.nav_frame.pack(side="left", fill="y")
        self.nav_frame.pack_propagate(False)  # Prevents the frame from shrinking to fit children

        # Create buttons
        tile_view_btn = tk.Button(self.nav_frame, text="Tile View",height=20)
        full_view_btn = tk.Button(self.nav_frame, text="Full View",height=20)
        tilemap_btn = tk.Button(self.nav_frame, text="Tilemap",height=20)

        # Pack buttons inside the nav frame
        tile_view_btn.pack(fill="x", pady=5)
        full_view_btn.pack(fill="x", pady=5)
        tilemap_btn.pack(fill="x", pady=5)


        # === Main Content Frame ===
        self.main_frame = tk.Frame(self, bg="white")
        self.main_frame.pack(side="right", expand=True, fill="both")

        # Initialize First View
        create_first_view(self)
        self.bind("<B1-Motion>", self.dragTile)


   
        
    def on_left_click(self, i, event):
        """Handle left mouse click on a box."""
        for a in constant.palette:
            a.config(highlightbackground="white", highlightthickness=0)
        widget = event.widget
        widget.config(highlightbackground="red", highlightthickness=2)
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
                    self.reloadTile(i)


    def clickTile(self, widget):
        """Handle clicking a pixel (8x8 grid)."""
        for i in range(len(constant.currTile)):
            if constant.currTile[i].widget == widget:
                constant.currTile[i].set_color(constant.selectedColor)  # Change the background color of the clicked tile

    def dragTile(self, event):
        widget = event.widget.winfo_containing(event.x_root, event.y_root)
        if widget in [pixel.widget for pixel in constant.currTile]:
            self.clickTile(widget)

    def removeTile(self, widget):
        """Handle right-clicking a pixel (8x8 grid)."""
        widget.config(bg="white")  # Change the background color of the clicked tile

    def changeTile(self,index):
       # (r * 16 + c)+(127*k)+(1*k)
        print(index)
        capture_grid(self, constant.grid_frame)
        apply_image_to_tile(self,constant.currTileIndex)
        constant.tileSet[constant.currTileIndex].setPixelsPaletteNumber(constant.currTile)
        constant.tileSet[constant.currTileIndex].modified=True
        constant.currTileIndex= index
        constant.tileSet[constant.currTileIndex].modified=True
        if constant.tileSet[index].modified == False:
            create_small_grid(self)
        else:
            load_small_grid(self, constant.currTileIndex)

        #createPaletteFile() 
    def reloadTile(self,index):
       # (r * 16 + c)+(127*k)+(1*k)
        print(index)
        load_small_grid(self, index)
        constant.tileSet[index].setPixelsPaletteNumber(constant.currTile)
        capture_grid(self, constant.grid_frame)
        apply_image_to_tile(self,index)
        

if __name__ == "__main__":
    app = App()
    app.mainloop()
