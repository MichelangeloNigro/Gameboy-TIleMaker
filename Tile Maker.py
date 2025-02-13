import tkinter as tk
from tkinter import messagebox

box_colors = ["#FEFEFE", "#C0C0C0", "#404040", "#000000"]  # white, light grey, grey, black
selectedColor = "#FEFEFE"  # Default selected color
currTile=[]

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Tkinter Grid Layout")
        self.geometry("900x600")  # Adjust as needed

        # === Navigation Panel (Left Side) ===
        self.nav_frame = tk.Frame(self, width=150, bg="gray")
        self.nav_frame.pack(side="left", fill="y")

        # === Main Content Frame ===
        self.main_frame = tk.Frame(self, bg="white")
        self.main_frame.pack(side="right", expand=True, fill="both")

        # Initialize First View
        self.create_first_view()
        self.bind("<space>", self.on_spacebar_press)

    def on_spacebar_press(self, event):
        if self.checkTileComplete():
            print("tile is complete")

        else:
            print("tile is missing pixel")


    def create_first_view(self):
        # Clear previous widgets
        for widget in self.main_frame.winfo_children():
            widget.destroy()

        # === 16x8 Grids (Left Side) ===
        for k in range(3):  # Create 3 grids in rows 0, 1, 2
            large_grid_frame = tk.Frame(self.main_frame, bg="lightcoral")
            large_grid_frame.grid(row=k, column=0, padx=(10, 20), pady=5)  # More space on right side

            for r in range(8):
                for c in range(16):
                    tk.Label(
                        large_grid_frame, text=f"{r},{c}", width=2, height=1, relief="solid"
                    ).grid(row=r, column=c)

        # === Separator Line ===
        separator = tk.Frame(self.main_frame, width=2, bg="black")  # Thin vertical line
        separator.grid(row=0, column=1, rowspan=3, sticky="ns", padx=(0, 20))  # Runs full height

        # === 8x8 Grid (Right Side, Spanning 3 Rows) ===
        grid_frame = tk.Frame(self.main_frame, bg="lightblue")
        grid_frame.grid(row=0, column=2, rowspan=3, padx=10, pady=10)
        global currTile
        for r in range(8):
            for c in range(8):
                pixel = tk.Label(grid_frame, text=f"{r},{c}", width=4, height=2, relief="solid", bg="red")
                pixel.grid(row=r, column=c)
                currTile.append(pixel)
                # Capture the correct row (r) and column (c) for each pixel
                pixel.bind("<Button-1>", lambda event, widget=pixel: self.clickTile( widget, event))
                pixel.bind("<Button-3>", lambda event, widget=pixel: self.removeTile( widget, event))


        # === 1x4 Row (Right of 8x8 Grid, Clickable) ===
        row_frame = tk.Frame(self.main_frame, bg="lightgreen")
        row_frame.grid(row=0, column=3, rowspan=3, padx=10, pady=10)

        for i in range(4):
            box = tk.Label(row_frame, width=6, height=2, relief="solid", bg=box_colors[i])
            box.pack(side="top", pady=2)

            # Bind left and right click events
            box.bind("<Button-1>", lambda event, n=i+1, widget=box: self.on_left_click(n, widget, event))
            box.bind("<Button-3>", lambda event, n=i+1, widget=box: self.on_right_click(n, widget, event))

    def on_left_click(self, box_number, widget, event):
        """Handle left mouse click on a box."""
        global selectedColor
        selectedColor = widget.cget("bg")  # Get the background color of the clicked box
        #messagebox.showinfo("Left Click", f"You left-clicked and selected {selectedColor}")

    def on_right_click(self, box_number, widget, event):
        """Handle right mouse click on a box."""
        global selectedColor
        selectedColor = widget.cget("bg")  # Get the background color of the clicked box
        #messagebox.showwarning("Right Click", f"You right-clicked and selected {selectedColor}")
    
    def clickTile(self, widget, event):
        """Handle clicking a pixel (8x8 grid)."""
        widget.config(bg=selectedColor)  # Change the background color of the clicked tile
    
    def removeTile(self, widget, event):
        """Handle clicking a pixel (8x8 grid)."""
        widget.config(bg="red")  # Change the background color of the clicked tile

    def checkTileComplete(self):
        for i in range(len(currTile)):  # Use len(currTile) to get the count
            if currTile[i].cget("bg") == "red":
                return False
        return True

if __name__ == "__main__":
    app = App()
    app.mainloop()
