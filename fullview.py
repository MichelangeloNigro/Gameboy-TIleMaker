import tkinter as tk
import constant

def redraw(event=None):
    """Recalculate and redraw the grid to use the full available space."""
    canvas = constant.app.fullviewCanvas
    canvas.delete("all")  # Clear previous drawings

    # Get the current canvas size
    width = canvas.winfo_width()
    height = canvas.winfo_height()

    # Calculate pixel width and height separately (DO NOT force square pixels)
    pixel_width = width / (16 * 8)   # 16 tiles × 8 pixels per tile
    pixel_height = height / (24 * 8)  # 24 tiles × 8 pixels per tile

    # Draw the grid and store pixel IDs
    constant.app.pixel_rects.clear()
    for tile_r in range(24):
        for tile_c in range(16):
            indexbig = tile_r * 16 + tile_c  # Corrected index calculation
            for r in range(8):
                for c in range(8):
                    index = r * 8 + c

                    # Compute pixel positions
                    x1 = int((tile_c * 8 + c) * pixel_width)
                    y1 = int((tile_r * 8 + r) * pixel_height)
                    x2 = int(x1 + pixel_width)
                    y2 = int(y1 + pixel_height)

                    # Get color safely
                    try:
                        color = constant.palette[constant.tileSet[indexbig].pixels[index]].cget("bg")
                    except (IndexError, AttributeError):
                        color = "white"  # Default to white if out of range

                    # Draw the pixel
                    rect_id = canvas.create_rectangle(
                        x1, y1, x2, y2, outline="black", fill=color, width=1
                    )
                    constant.app.pixel_rects[rect_id] = (tile_r, tile_c, r, c)  # Store pixel location


def on_canvas_click(event):
    """Handles pixel click and changes its color."""
    x, y = event.x, event.y
    col = constant.palette[constant.selectedColor].cget("bg")
    
    # Iterate through all the pixels in the canvas to find the clicked one
    for rect_id, (tile_r, tile_c, r, c) in constant.app.pixel_rects.items():
        coords = constant.app.fullviewCanvas.coords(rect_id)
        if coords[0] <= x <= coords[2] and coords[1] <= y <= coords[3]:
            # Find the correct tile in tileSet[] using tile_r and tile_c
            tile_index = tile_r * 16 + tile_c  # Calculate the index of the tile
            selected_tile = constant.tileSet[tile_index]  # Get the tile
            constant.tileSet[tile_index].modified = True
            # Find the pixel in the tile and update its color
            selected_tile.pixels[r * 8 + c] = constant.selectedColor  # Update the pixel color
            constant.app.fullviewCanvas.itemconfig(rect_id, fill=f"{col}")  # Change color on click
            # Redraw the grid to reflect the color change
            break  # Stop after finding the clicked pixel

# Function to initialize and bind events
def createfullview(app):
    """Draws the entire 8192-pixel grid using rectangles on the Canvas, scaling dynamically."""
    canvas = app.fullviewCanvas
    app.pixel_rects = {}  # Store rectangle IDs for click handling

    # Bind events
    canvas.bind("<Configure>", redraw)
    canvas.bind("<Button-1>", on_canvas_click)  # Left-click to trigger on_canvas_click
