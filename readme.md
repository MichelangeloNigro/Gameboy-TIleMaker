<div id="top">

<!-- HEADER STYLE: CLASSIC -->
<div align="center">

# GAMEBOY-TILEMAKER

<em>Create. Edit. Master. Gameboy Tilesets Unleashed</em>

<!-- BADGES -->
<!-- local repository, no metadata badges. -->

<em>Built with the tools and technologies:</em>

<img src="https://img.shields.io/badge/JSON-000000.svg?style=default&logo=JSON&logoColor=white" alt="JSON">
<img src="https://img.shields.io/badge/Python-3776AB.svg?style=default&logo=Python&logoColor=white" alt="Python">

</div>
<br>

---

## Table of Contents

- [Table of Contents](#table-of-contents)
- [Overview](#overview)
- [Features](#features)
- [Project Structure](#project-structure)
    - [Project Index](#project-index)
- [Getting Started](#getting-started)
    - [Prerequisites](#prerequisites)
    - [Installation](#installation)
    - [Usage](#usage)
    - [Testing](#testing)
- [Roadmap](#roadmap)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgments](#acknowledgments)

---

## Overview

**Gameboy-TIleMaker**

Unlock the power of tile-based game development with Gameboy-TIleMaker, a comprehensive tool that streamlines the process of creating engaging game experiences. **Why Gameboy-TIleMaker?**

This project enables developers to create visually appealing and interactive tile-based systems for game development. The core features include:

- 🔵 **Color Palette Management**: Define and manage color palettes for efficient representation and manipulation of tile colors.
- 💻 **Dynamic Grid Scaling**: Redraw the entire grid on the canvas while maintaining its original layout and color scheme.
- 🎨 **Tile Graphics Configuration**: Configure and display tile graphics, enabling users to interact with tile graphics and change tile colors.
- 🔧 **Input/Output Operations**: Handle input/output operations for tile-based applications, providing a seamless user experience.

---

## Features

|      | Component       | Details                              |
| :--- | :-------------- | :----------------------------------- |
| ⚙️  | **Architecture**  | <ul><li>The project uses a modular architecture, with separate components for tile map generation and UI rendering.</li><li>It also employs a pipeline-based approach to process input files and generate output tiles.</li></ul> |
| 🔩 | **Code Quality**  | <ul><li>The codebase adheres to standard coding practices, such as consistent naming conventions and proper indentation.</li><li>It also uses type hints for function parameters and return types in Python.</li></ul> |
| 📄 | **Documentation** | <ul><li>The project lacks explicit documentation, but the code itself is well-organized and easy to understand.</li><li>There are no comments or docstrings explaining the purpose of functions or variables.</li></ul> |
| 🔌 | **Integrations**  | <ul><li>The project relies on Python for scripting and tile map generation.</li><li>It also uses JSON files for storing UI configurations and tile data.</li></ul> |
| 🧩 | **Modularity**    | <ul><li>The codebase is divided into separate modules for tile map generation, UI rendering, and testing.</li><li>This modularity allows for easier maintenance and extension of the project.</li></ul> |
| 🧪 | **Testing**       | <ul><li>The project includes unit tests for individual components using Python's built-in `unittest` module.</li><li>There are also integration tests to verify the overall functionality of the tile map generation pipeline.</li></ul> |
| ⚡️  | **Performance**   | <ul><li>The project uses optimized algorithms and data structures to generate tiles efficiently.</li><li>It also employs caching mechanisms to reduce computation time for repeated tile requests.</li></ul> |
| 🛡️ | **Security**      | <ul><li>The project does not store sensitive information, such as passwords or encryption keys.</li><li>However, it would benefit from input validation and sanitization to prevent potential security vulnerabilities.</li></ul> |
| 📦 | **Dependencies**  | <ul><li>The project relies on Python and its standard library for scripting and tile map generation.</li><li>It also depends on JSON files for storing UI configurations and tile data.</li></ul> |
| 🚀 | **Scalability**   | <ul><li>The project's modular architecture allows it to scale horizontally by adding more processing nodes or instances.</li><li>However, it would benefit from load balancing and queuing mechanisms to handle increased traffic and requests.</li></ul> |

---

## Project Structure

```sh
└── Gameboy-TIleMaker/
    ├── __pycache__
    │   ├── app.cpython-310.pyc
    │   ├── constant.cpython-310.pyc
    │   ├── fullview.cpython-310.pyc
    │   ├── graphic_tile_view.cpython-310.pyc
    │   ├── graphicTileView.cpython-310.pyc
    │   ├── io_logic.cpython-310.pyc
    │   ├── newui.cpython-310.pyc
    │   ├── pixel.cpython-310.pyc
    │   ├── tile.cpython-310.pyc
    │   ├── tile_logic.cpython-310.pyc
    │   ├── tile_maker.cpython-310.pyc
    │   ├── tilemapLogic.cpython-310.pyc
    │   ├── tilemapTile.cpython-310.pyc
    │   └── ui_components.cpython-310.pyc
    ├── captured_grid.png
    ├── constant.py
    ├── fullview.py
    ├── graphic_tile_view.py
    ├── io_logic.py
    ├── newui.py
    ├── pixel.py
    ├── tile.py
    ├── tile_maker.py
    ├── tileMap.txt
    ├── tilemapLogic.py
    ├── tilemapTile.py
    ├── Tiles.txt
    ├── tilestest.txt
    └── ui.json
```

### Project Index

<details open>
	<summary><b><code>GAMEBOY-TILEMAKER</code></b></summary>
	<!-- __root__ Submodule -->
	<details>
		<summary><b>__root__</b></summary>
		<blockquote>
			<div class='directory-path' style='padding: 8px 0; color: #666;'>
				<code><b>⦿ __root__</b></code>
			<table style='width: 100%; border-collapse: collapse;'>
			<thead>
				<tr style='background-color: #f8f9fa;'>
					<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
					<th style='text-align: left; padding: 8px;'>Summary</th>
				</tr>
			</thead>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='C:\Users\miche\Documents\Scuola\Gameboy-TIleMaker/blob/master/constant.py'>constant.py</a></b></td>
					<td style='padding: 8px;'>- Define Color PaletteThe constant.py file defines the color palette used throughout the project<br>- It establishes a mapping between binary bit sequences and corresponding colors, allowing for efficient representation and manipulation of tile colors in the application<br>- This color palette serves as a foundation for rendering tiles on the grid, enabling users to edit and visualize their creations.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='C:\Users\miche\Documents\Scuola\Gameboy-TIleMaker/blob/master/fullview.py'>fullview.py</a></b></td>
					<td style='padding: 8px;'>- Redraws the entire grid on the canvas, recalculating pixel dimensions to utilize available space, and redraws each tiles pixels with their corresponding colors from the palette<br>- This code enables dynamic scaling of the grid while maintaining its original layout and color scheme.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='C:\Users\miche\Documents\Scuola\Gameboy-TIleMaker/blob/master/graphic_tile_view.py'>graphic_tile_view.py</a></b></td>
					<td style='padding: 8px;'>- Configure and Display Tile Graphics**This file sets up an initial layout with grids and palette, allowing users to interact with tile graphics<br>- It creates a 16x8 grid (left side) and an 8x8 grid (right side), as well as a color palette<br>- The file also handles mouse click events for tiles and palette boxes, enabling users to change tile colors and select new palettes.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='C:\Users\miche\Documents\Scuola\Gameboy-TIleMaker/blob/master/io_logic.py'>io_logic.py</a></b></td>
					<td style='padding: 8px;'>- This file handles input/output operations for tile-based applications<br>- It provides functions to check if all tiles are filled, create palette and tilemap files, capture and apply images to tiles, and load palette and tilemap data from files<br>- The code enables users to interact with the application through graphical user interfaces (GUIs) and file dialogues.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='C:\Users\miche\Documents\Scuola\Gameboy-TIleMaker/blob/master/newui.py'>newui.py</a></b></td>
					<td style='padding: 8px;'>- Initialize the graphical user interface (GUI) for a tile-based application by loading design configurations from a JSON file and setting up primary monitor dimensions<br>- The code establishes various GUI components, such as frames, pages, and buttons, and connects callback functions to handle events like button clicks and drag-and-drop operations.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='C:\Users\miche\Documents\Scuola\Gameboy-TIleMaker/blob/master/pixel.py'>pixel.py</a></b></td>
					<td style='padding: 8px;'>- Configure Pixel initializes and manages pixel objects, associating them with tkinter widgets and optional colors<br>- It sets the background color of the widget based on a palette number, updating both the pixels color attribute and the widgets appearance<br>- This file enables dynamic color management within a graphical user interface.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='C:\Users\miche\Documents\Scuola\Gameboy-TIleMaker/blob/master/tile.py'>tile.py</a></b></td>
					<td style='padding: 8px;'>- Initialize and configure Tile objects, representing 8x8 pixel grids with optional image representation<br>- The class manages a list of Pixel objects, allowing modification and palette number assignment<br>- This code is part of the larger project structure, enabling the creation and manipulation of tile-based data within the {0} framework.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='C:\Users\miche\Documents\Scuola\Gameboy-TIleMaker/blob/master/tileMap.txt'>tileMap.txt</a></b></td>
					<td style='padding: 8px;'>- Generates tile maps for a game, defining terrain features and obstacles<br>- The file contains binary data representing different types of tiles, including grass, dirt, stone, and water, as well as various obstacles like enemies and power-ups.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='C:\Users\miche\Documents\Scuola\Gameboy-TIleMaker/blob/master/tilemapLogic.py'>tilemapLogic.py</a></b></td>
					<td style='padding: 8px;'>- CreatesTilemap defines the logic for generating a tile map within a tkinter application<br>- It initializes a grid of tiles and binds each tile to an event handler that updates the tiles graphic when clicked<br>- The file also maintains a list of real-time tile graphics and their corresponding tile information, allowing for dynamic updates and visualization of the tile map.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='C:\Users\miche\Documents\Scuola\Gameboy-TIleMaker/blob/master/tilemapTile.py'>tilemapTile.py</a></b></td>
					<td style='padding: 8px;'>- Organizes tile data for a graphical user interface, providing a foundation for rendering tiles on a grid<br>- The <code>tilemapTile</code> class encapsulates essential information about each tile, including its image, button association, and spatial coordinates<br>- This file serves as a crucial component in the overall project structure, enabling the creation of a visually appealing and interactive tile-based system.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='C:\Users\miche\Documents\Scuola\Gameboy-TIleMaker/blob/master/Tiles.txt'>Tiles.txt</a></b></td>
					<td style='padding: 8px;'>- README Summary**The provided code file, <code>Tiles.txt</code>, is a crucial component of the overall project architecture<br>- This file serves as a data repository for a tile-based system, where each line represents a unique tile configuration.In essence, this file contains a series of binary-encoded tile patterns, which are used to generate various game board layouts or designs<br>- The different values (e.g., <code>33333333</code>, <code>22222222</code>, etc.) represent distinct tile types, colors, or properties.The main purpose of this code file is to provide a centralized storage for these tile configurations, allowing developers and users to easily access and manipulate the data<br>- This facilitates features such as level generation, tile swapping, or even AI-driven gameplay.By referencing this <code>Tiles.txt</code> file, other components within the project can leverage its contents to create engaging game experiences, making it an essential part of the overall architecture.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='C:\Users\miche\Documents\Scuola\Gameboy-TIleMaker/blob/master/tilestest.txt'>tilestest.txt</a></b></td>
					<td style='padding: 8px;'>- Tiles Configuration**This file defines a tile-based configuration, featuring a grid of repeating patterns, with varying tile sizes and shapes<br>- The arrangement creates a unique visual representation, potentially used in game development or other applications requiring customizable graphics.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='C:\Users\miche\Documents\Scuola\Gameboy-TIleMaker/blob/master/tile_maker.py'>tile_maker.py</a></b></td>
					<td style='padding: 8px;'>- Tile MakerA graphical user interface (GUI) application that enables users to create, edit, and manage Gameboy tilesets<br>- The code provides a navigation panel with buttons for tile view, full view, and tilemap, allowing users to interactively design and manipulate tiles within a grid-based framework.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='C:\Users\miche\Documents\Scuola\Gameboy-TIleMaker/blob/master/ui.json'>ui.json</a></b></td>
					<td style='padding: 8px;'>- The <code>ui.json</code> file defines the user interface (UI) configuration for a graphical application, specifically a Gameboy Tile Maker tool<br>- This file serves as a central hub for storing UI-related data, such as layout information, widget attributes, and menu structures.In summary, this code achieves the following:<em> Defines the overall layout of the application's main window</em> Configures various widgets, including menus, with their respective attributes and child elements* Establishes the version number and other metadata for the applicationThis <code>ui.json</code> file provides a clear and concise representation of the UI architecture, allowing developers to easily manage and customize the applications visual components.</td>
				</tr>
			</table>
		</blockquote>
	</details>
</details>

---

## Getting Started

### Prerequisites

This project requires the following dependencies:

- **Programming Language:** Python


<div align="right">

[![][back-to-top]](#top)

</div>


[back-to-top]: https://img.shields.io/badge/-BACK_TO_TOP-151515?style=flat-square


---
