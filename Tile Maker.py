import tkinter as tk
from tkinter import messagebox
import copy
from PIL import ImageGrab, Image, ImageTk
import os
from screeninfo import get_monitors



box_colors = ["#FEFEFE", "#C0C0C0", "#404040", "#000000"]  # white, light grey, grey, black
palette = []
currTile = []
tileSet= []
tileMap=[]
currTileIndex=0
grid_frame=None
selectedColor = 0  # Default selected color

#   ld a, %11100100
#     ld [rBGP], a
#     ld a, %11100100
#     ld [rOBP0], a
class Pixel:
    def __init__(self, widget=None, color="white", paletteNumber=0):
        """Initialize Pixel with a widget and an optional associated color."""
        self.widget = widget  # The tkinter widget (Label)
        self.color = color    # The associated color for this pixel
        self.paletteNumber = paletteNumber

    def set_color(self, paletteN):
        """Set the background color of the pixel."""
        self.paletteNumber = paletteN
        self.widget.config(bg=palette[self.paletteNumber].cget("bg"))
        self.color = palette[self.paletteNumber].cget("bg")

class Tile:
    def __init__(self, pixels=None, modified=False):
        """Initialize the Tile with a 2D list of Pixel objects (8x8 grid)."""
        self.modified=modified
        # If no pixels array is provided, initialize with an 8x8 grid of red pixels
        # if pixels is None:
        #     self.pixels = [[Pixel() for _ in range(8)] for _ in range(8)]
        # Create a new list containing only the paletteNumber of each Pixel
        # palette_numbers = [pixel.paletteNumber for pixel in pixels]
        self.pixels = pixels # Use the provided pixels array

    def setPixelsPaletteNumber(self,pixels):
        palette_numbers = [pixel.paletteNumber for pixel in pixels]
        self.pixels = palette_numbers  # Use the provided pixels array
    def set_pixel_color(self, row, col, color):
        """Set the color of a specific pixel in the grid."""
        if 0 <= row < 8 and 0 <= col < 8:
            self.pixels[row][col].set_color(color)
        else:
            print("Invalid pixel coordinates")

    def get_pixel_color(self, row, col):
        """Get the color of a specific pixel in the grid."""
        if 0 <= row < 8 and 0 <= col < 8:
            return self.pixels[row][col].color
        else:
            print("Invalid pixel coordinates")
            return None


class Tileset:
    def __init__(self):
        pass


class Tilemap:
    def __init__(self):
        pass


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Tkinter Grid Layout")
        self.geometry("900x600")  # Adjust as needed
        # === Navigation Panel (Left Side) ===
        # Get the primary monitor's height from the monitor list
        primary_monitor = get_monitors()[0]  # Assuming the first monitor is the primary monitor

        # Set the window's height to the primary monitor's height
        self.geometry(f"{int(primary_monitor.width/2)}x{int(primary_monitor.height/2)}")  # width and height based on the primary monitor

        self.nav_frame = tk.Frame(self, width=150, bg="gray")
        self.nav_frame.pack(side="left", fill="y")

        # === Main Content Frame ===
        self.main_frame = tk.Frame(self, bg="white")
        self.main_frame.pack(side="right", expand=True, fill="both")

        # Initialize First View
        self.create_first_view()
        self.bind("<B1-Motion>", self.dragTile)


    def create_first_view(self):
        """Set up the initial layout with grids and palette."""
        # Clear previous widgets
        for widget in self.main_frame.winfo_children():
            widget.destroy()

        # Create the 16x8 grids (left side)
        self.create_large_grids()

        # Separator line between grids and tile selection area
        self.create_separator()

        # Create the 8x8 grid (right side)
        self.create_small_grid()

        # Create 1x4 color palette (right of 8x8 grid)
        self.create_palette()

    def create_large_grids(self):
        """Create the 16x8 grids."""
        global tileMap
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
                    tileMap.append(tileGraphic)
                    # Calculate the index for the 1D array
                    
                    # Create and append the Tile object
                    tile = Tile()
                    tileSet.append(tile)


    def create_separator(self):
        """Create a separator line."""
        separator = tk.Frame(self.main_frame, width=2, bg="black")  # Thin vertical line
        separator.grid(row=0, column=1, rowspan=3, sticky="ns", padx=(0, 20))  # Runs full height

    def create_small_grid(self):
        """Create the 8x8 grid."""
        global grid_frame
        grid_frame = tk.Frame(self.main_frame, bg="lightblue")  # Store as self.grid_frame
        grid_frame.grid(row=0, column=2, rowspan=3, padx=10, pady=10, sticky="nsew")
        self.main_frame.grid_rowconfigure(0, weight=1)  # Allow rows to expand
        self.main_frame.grid_columnconfigure(2, weight=1)  # All
        for r in range(8):
            grid_frame.grid_rowconfigure(r, weight=1)  # Allow rows to expand
        for c in range(8):
            grid_frame.grid_columnconfigure(c, weight=1)  # Allow columns to expand
        global currTile
        global tileSet
        currTile.clear()
        for r in range(8):
            for c in range(8):
                pixel = tk.Label(grid_frame, text=f"{r},{c}", relief="solid", bg="white")
                pixel.grid(row=r, column=c,sticky="nsew")
                pixel_data = Pixel(pixel, "white")  # Creating an instance of the Pixel class
                currTile.append(pixel_data)
                # Capture the correct row (r) and column (c) for each pixel
                pixel.bind("<Button-1>", lambda event, widget=pixel: self.clickTile(widget))
                pixel.bind("<Button-3>", lambda event, widget=pixel: self.removeTile(widget))


    def load_small_grid(self):
        global grid_frame
        grid_frame = tk.Frame(self.main_frame, bg="lightblue")  # Store as self.grid_frame
        grid_frame.grid(row=0, column=2, rowspan=3, padx=10, pady=10, sticky="nsew")
        self.main_frame.grid_rowconfigure(0, weight=1)  # Allow rows to expand
        self.main_frame.grid_columnconfigure(2, weight=1)  # All
        for r in range(8):
            grid_frame.grid_rowconfigure(r, weight=1)  # Allow rows to expand
        for c in range(8):
            grid_frame.grid_columnconfigure(c, weight=1)  # Allow columns to expand
        global currTile
        global currTileIndex
        global tileSet
        currTile.clear()
        toLoad= tileSet[currTileIndex]
        for r in range(8):
            for c in range(8):
                index = r * 8 + c
                pixel = tk.Label(grid_frame, text=f"{r},{c}", width=4, height=2, relief="solid", bg=palette[toLoad.pixels[index]].cget("bg"))
                pixel.grid(row=r, column=c,sticky="nsew")
                pixel_data = Pixel(pixel, palette[toLoad.pixels[index]].cget("bg"))
                pixel_data.paletteNumber= toLoad.pixels[index] # Creating an instance of the Pixel class
                currTile.append(pixel_data)
                # Capture the correct row (r) and column (c) for each pixel
                pixel.bind("<Button-1>", lambda event, widget=pixel: self.clickTile(widget))
                pixel.bind("<Button-3>", lambda event, widget=pixel: self.removeTile(widget))

    def create_palette(self):
        """Create the 1x4 color palette."""
        row_frame = tk.Frame(self.main_frame, bg="lightgreen")
        row_frame.grid(row=0, column=3, rowspan=3, padx=10, pady=10, sticky="nsew")
        row_frame.grid_rowconfigure(0, weight=1)  # Make row 0 expand vertically
        row_frame.grid_columnconfigure(0, weight=1, minsize=100)  # Make colum
        for i in range(4):
            box = tk.Label(row_frame, relief="solid", bg=box_colors[i])
            box.grid(row=i, column=0, sticky="nsew", pady=2)  # Use grid() instead of pack()
            palette.append(box)
            row_frame.grid_rowconfigure(i, weight=1)  # Allow each row to expand vertically

            # Bind left and right click events
            box.bind("<Button-1>", lambda event,i=i: self.on_left_click(i))
            box.bind("<Button-3>", lambda event,i=i: self.on_right_click(i))

        
    def on_left_click(self, i):
        """Handle left mouse click on a box."""
        global selectedColor
        selectedColor = i # Get the background color of the clicked box

    def on_right_click(self, i):
        """Handle right mouse click on a box."""
        global selectedColor
        selectedColor = i # Get the background color of the clicked box

    def clickTile(self, widget):
        """Handle clicking a pixel (8x8 grid)."""
        for i in range(len(currTile)):
            if currTile[i].widget == widget:
                currTile[i].set_color(selectedColor)  # Change the background color of the clicked tile

    def dragTile(self, event):
        widget = event.widget.winfo_containing(event.x_root, event.y_root)
        if widget in [pixel.widget for pixel in currTile]:
            self.clickTile(widget)

    def removeTile(self, widget):
        """Handle right-clicking a pixel (8x8 grid)."""
        widget.config(bg="red")  # Change the background color of the clicked tile

    def changeTile(self,index):
       # (r * 16 + c)+(127*k)+(1*k)
        global currTileIndex
        print(index)
        self.capture_grid()
        self.apply_image_to_tile(currTileIndex)
        tileSet[currTileIndex].setPixelsPaletteNumber(currTile)
        tileSet[currTileIndex].modified=True
        currTileIndex= index
        if tileSet[index].modified == False:
            self.create_small_grid()
        else:
            self.load_small_grid()
    def checkTileComplete(self):
        """Check if all tiles are filled."""
        for i in range(len(currTile)):  # Use len(currTile) to get the count
            if currTile[i].color == "red":
                return False
        
        return True


    # def draw_circle_on_screen(self, x, y, radius=5):
    #     dot = tk.Label(self.main_frame, bg="red", width=radius*2, height=radius*2)
    #     dot.place(x=x - radius, y=y - radius)


    def capture_grid(self):
        global grid_frame
        """Captures the 8x8 grid as an image."""
        # Get coordinates of the grid frame
        self.update_idletasks()  # Ensure layout updates
    # Get widget position and size
        x = grid_frame.winfo_rootx()
        y = grid_frame.winfo_rooty()
        w = grid_frame.winfo_width()
        h = grid_frame.winfo_height()
        self.img = ImageGrab.grab(bbox=(x, y, x + w, y + h),all_screens=True)

        # Resize if needed
       # img = img.resize((tileMap[0].winfo_width(),tileMap[0].winfo_height()))  # Resize for fitting in a 16x8 tile

        # Convert to Tkinter PhotoImage
        self.saved_img = ImageTk.PhotoImage(self.img)
        script_dir = os.path.dirname(os.path.abspath(__file__))

        # Save the image in the same directory as the script
        img_path = os.path.join(script_dir, "captured_grid.png")
        self.img.save(img_path)
        print("Grid captured successfully!")

    def apply_image_to_tile(self, index):
        """Applies the captured grid image as background to a tile in the 16x8 grid."""
        if not hasattr(self, 'saved_img'):
            print("No image captured yet!")
            return
        global tileMap
        target_tile = tileMap[index]  # Access the correct tile label
        canvas_width = target_tile.winfo_width()
        canvas_height = target_tile.winfo_height()
        target_tile.delete("all")  # Clears any existing drawing
        # Resize the image to fit the canvas size dynamically
        resized_img = self.img.resize((canvas_width, canvas_height), Image.Resampling.LANCZOS)
        
        # Convert the resized image to a PhotoImage object for Tkinter
        tk_resized_img = ImageTk.PhotoImage(resized_img)
        
        # Apply the resized image as the background
        target_tile.create_image(0, 0, image=tk_resized_img, anchor="nw")
        
        # Prevent garbage collection by keeping a reference to the resized image
        target_tile.image = tk_resized_img

if __name__ == "__main__":
    app = App()
    app.mainloop()
