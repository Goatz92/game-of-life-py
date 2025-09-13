import pygame, random

class Grid:
    """
    Handles all the operations related to the grid of the application:
    1. Drawing the grid
    2. Filling the grid with random cells
    3. Clearing the grid
    4. Manually toggling cells as live or dead with user input
    """
    # Constructor
    def __init__(self, width, height, cell_size):
        self.rows = height // cell_size
        self.columns = width // cell_size
        self.cell_size = cell_size
        self.cells = [[0 for _ in range(self.columns)] for _ in range(self.rows)]

    def draw(self, window):
        """
        Draws the grid on the window

        Args: 
            window: The resolution of the screen
        """
        for row in range(self.rows):
            for column in range(self.columns):
                color = (0, 255, 0) if self.cells[row][column] else (55, 55, 55)
                pygame.draw.rect(window, color, (column * self.cell_size, row * self.cell_size, self.cell_size - 1, self.cell_size - 1))

    def fill_random(self):
        """
        Draws a random cells in the grid
        """
        pass

    def clear(self):
        """
        Clears the grid on input
        """
        pass

    def toggle_cell(self, row, column):
        """
        Toggles a cell's state on input

        Args: 
            row (int): The row of the grid
            column (int): the column of the grid
        """