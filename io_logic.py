from PIL import ImageGrab, Image, ImageTk
import os
import time
import constant
from tkinter import messagebox
from tkinter import Tk, filedialog

#from graphic_tile_view import reloadTile
def checkTileComplete():
    """Check if all tiles are filled."""
    for i in range(len(constant.currTile)):  # Use len(currTile) to get the count
        if constant.currTile[i].color == "red":
            return False
    
    return True


# def draw_circle_on_screen(self, x, y, radius=5):
#     dot = tk.Label(self.main_frame, bg="red", width=radius*2, height=radius*2)
#     dot.place(x=x - radius, y=y - radius)

def createPaletteFile(filename="Tiles.txt"):
    global tileSet
    time.sleep(1)  # Give some time for data to be populated
    
    filename = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Tiles.txt")
    messagebox.showinfo("Save path","File saved in path: "+filename)
    with open(filename, "w") as file:
        for i in range(len(constant.tileSet)):
            pixels = constant.tileSet[i].pixels  # Get the pixel data for the tile
            for k in range(0, len(pixels), 8):  # Process 8 pixels at a time
                file.write("    dw `")  # Start each row with "dw `"
                file.write("".join(str(p) for p in pixels[k:k+8]) + "\n")  # Write 8 characters per row
        #ld a, %11100100
        #ld [rBGP], a
        palettebit=""
        for clr in constant.palette:
            palettebit+=constant.reverse_color_map[clr.cget("bg")] 
        file.write(f";this is the palette used\n;ld a, %{palettebit}\n;ld [rBGP], a")


def createTilemapFile(event, filename="tileMap.txt"):
    time.sleep(1)  # Give some time for data to be populated
    filename = os.path.join(os.path.dirname(os.path.abspath(__file__)), "tileMap.txt")
    messagebox.showinfo("Save path","File saved in path: "+filename)
    with open(filename, "w") as file:
        for i in range(0, len(constant.tileMapReal), 20):
            file.write("    db ")
            chunk = constant.tileMapReal[i:i+20]  # Get a slice of up to 20 elements
            file.write(", ".join(f"${tile.hex.zfill(2)}" for tile in chunk))  # Ensure two-digit hex
            file.write(", 0,0,0,0,0,0,0,0,0,0,0,0\n")


def capture_grid(self, grid_frame):
    """Captures the 8x8 grid as an image."""
    # Get coordinates of the grid frame
    self.tk_1.update_idletasks()  # Ensure layout updates
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
    target_tile = constant.tileMap[index]  # Access the correct tile label
    canvas_width = target_tile.winfo_width()
    canvas_height = target_tile.winfo_height()
    target_tile.delete("all")  # Clears any existing drawing
    # Resize the image to fit the canvas size dynamically
    resized_img = self.img.resize((canvas_width, canvas_height), Image.Resampling.LANCZOS)
    
    # Convert the resized image to a PhotoImage object for Tkinter
    tk_resized_img = ImageTk.PhotoImage(resized_img)
    constant.tileSet[constant.currTileIndex].img=self.img

    # Apply the resized image as the background
    target_tile.create_image(0, 0, image=tk_resized_img, anchor="nw")
    
    # Prevent garbage collection by keeping a reference to the resized image
    target_tile.image = tk_resized_img

def loadPaletteIO():  
    root = Tk()
    root.withdraw()  # Hide the root window
    path = filedialog.askopenfilename(title="Select Tiles File", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    root.destroy()
    with open(path, "r") as file:
        lines = file.readlines()  # Read all lines

    tile_index = 0
    pixels = []  # Temporary list to hold pixel data

    for line in lines:
        line = line.strip()
        if not line.startswith("dw `"):  
            continue  # Skip lines that don't start with "dw `"
        if line.startswith("dw `"):  # Ensure it's a valid tile row
            pixel_data = line[4:]  # Extract the pixel values after "dw `"
            pixels.extend(int(p) for p in pixel_data)  # Convert characters to integers

            if len(pixels) == 64:  # Each tile has 8x8 = 64 pixels
                constant.tileSet[tile_index].pixels = pixels  # Assign to the tile
                constant.tileSet[tile_index].modified = True  # Assign to the tile
                #reloadTile(constant.app,tile_index)
                tile_index += 1  # Move to the next tile
                pixels = []  # Reset for the next tile

    # Handle any extra data (optional)
    if pixels:
        print(f"Warning: Incomplete tile data found ({len(pixels)} pixels)")



def loadTilemapFileIO():
    # Open file explorer for user to select a tilemap file
    filename = filedialog.askopenfilename(title="Select Tilemap File", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])

    if not filename:  # If the user cancels, exit function
        print("No file selected.")
        return

    with open(filename, "r") as file:
        lines = file.readlines()  # Read all lines


    tile_index = 0  # Track where we are in constant.tileMapReal

    for line in lines:
        line = line.strip()

        if not line.startswith("db "):  # Ignore non-data lines
            continue

        hex_values = line[3:].split(",")  # Remove "db " and split values

        for hex_value in hex_values:
            hex_value = hex_value.strip()  # Remove extra spaces
            if hex_value.startswith("$"):  # Ensure it's a hex number
                if tile_index < len(constant.tileMapReal):  # Prevent index out of range
                    constant.tileMapReal[tile_index].tile = int(hex_value[1:], 16)  # Convert to int
                tile_index += 1  # Move to next tile



    print(f"Successfully loaded {len(constant.tileMapReal)} tiles from {filename}.")
    messagebox.showinfo("Load Complete", f"Tilemap loaded from: {filename}")
