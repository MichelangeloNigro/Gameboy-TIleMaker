import constant
class Pixel:
    def __init__(self, widget=None, color="white", paletteNumber=0):
        """Initialize Pixel with a widget and an optional associated color."""
        self.widget = widget  # The tkinter widget (Label)
        self.color = color    # The associated color for this pixel
        self.paletteNumber = paletteNumber

    def set_color(self, paletteN):
        """Set the background color of the pixel."""
        self.paletteNumber = paletteN
        self.widget.config(bg=constant.palette[self.paletteNumber].cget("bg"))
        self.color = constant.palette[self.paletteNumber].cget("bg")
