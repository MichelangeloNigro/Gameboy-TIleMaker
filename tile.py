from PIL import Image
class Tile:
    def __init__(self, pixels=None, modified=False, img=None, hex=""):
        """Initialize the Tile with a 2D list of Pixel objects (8x8 grid)."""
        self.modified=modified
        self.img=Image.new("RGB", (8, 8), "white")  # Create an 8x8 white image
        self.pixels = pixels if pixels is not None else [0] * 64  # Ensure it's always 64 elements
        self.hex=hex
    def setPixelsPaletteNumber(self,pixels):
        palette_numbers = [pixel.paletteNumber for pixel in pixels]
        self.pixels = palette_numbers  # Use the provided pixels array
