import random
from block import Block
import tkinter as tk
import time

print("Permainan 1010! Block Puzzle Game")
print("By Michael Jonathan Halim | 13521124")

# Initialize board game
board = [[0 for _ in range(10)] for _ in range(10)]

# Initialize game states
score = 0
colors = [["white" for _ in range(10)] for _ in range(10)]

# Define available blocks
dot = Block([[1]], "#d9a3dc", 1)

two_dot = Block([[1, 1]], "#f9e79f", 2)

i_block = Block([[1], 
                 [1]], 
                 "#f9e79f", 2)

three_dot = Block([[1, 1, 1]], "#f5b041", 3)

I_block = Block([[1],
                [1],
                [1]], 
                "#f5b041", 3)

r_block = Block([[1, 1],
                [1, 0]], 
                "#a9f5df", 3)

l_block = Block([[1, 0],
                [1, 1]], 
                "#a9f5df", 3)

j_block = Block([[0, 1],
                [1, 1]], 
                "#a9f5df", 3)

t_block = Block([[1, 1],
                [0, 1]], 
                "#a9f5df", 3)

h_block = Block([[1, 1, 1, 1]], "#f1948a", 4)

O_block = Block([[1, 1, 1],
                [1, 1, 1],
                [1, 1, 1]], 
                "#1abc9c", 9)

H_block = Block([[1, 1, 1, 1, 1]], "#f1948a", 5)

V_block = Block([[1],
                [1],
                [1],
                [1],
                [1]], 
                "#f1948a", 5)

J_block = Block([[0, 0, 1],
                [0, 0, 1],
                [1, 1, 1]], 
                "#85c1e9", 5)

T_block = Block([[1, 1, 1],
                [0, 0, 1],
                [0, 0, 1]], 
                "#85c1e9", 5)

R_block = Block([[1, 1, 1],
                [1, 0, 0],
                [1, 0, 0]], 
                "#85c1e9", 5)

o_block = Block([[1, 1],
                [1, 1]], 
                "#56e856", 4)

v_block = Block([[1],
                [1],
                [1],
                [1]], 
                "#f1948a", 4)

L_block = Block([[1, 0, 0],
                [1, 0, 0],
                [1, 1, 1]], 
                "#85c1e9", 5)

# Combine all available blocks
blocks = [dot, two_dot, i_block, three_dot, I_block, r_block, 
          l_block, j_block, t_block, h_block, O_block, H_block, 
          V_block, J_block, T_block, R_block, o_block, v_block,
          L_block]

# Function to check game over
def game_over(selected_blocks):
    for block in selected_blocks:
        for row in range(10):
            for col in range(10):
                if(validation_check(block, row, col)):
                    # There is still a block that can be placed
                    return False
    
    # No blocks can be placed
    return True

# Function to add selected shape to a specific location
def add_selected_shape(block, i, j):
    global score

    # Get height and width block
    height = len(block)
    width = len(block[0])

    # Place block in board
    for row in range(height):
        for col in range(width):
            if board[i + row][j + col] == 0:
                board[i + row][j + col] = block[row][col]
                if board[i + row][j + col] != 0:
                    colors[i + row][j + col] = block.color
    
    # Add score
    score += block.score

# Function to generate 3 random blocks
def random_blocks():
    selected_blocks = random.choices(blocks, k=3)
    return selected_blocks

# Function to check if placing shape in a location valid or not
def validation_check(block, i, j):
    # Get height and width block
    height = len(block)
    width = len(block[0])

    # Out of bounds
    if i + height > 10 or j + width > 10:
        return False
    
    # Check if block can be placed on the starting selected box
    for row in range(height):
        for col in range(width):
            if block[row][col] == 1 and board[i + row][j + col] != 0:
                return False
    
    # Valid
    return True

# Function to check if there is a vertical or horizontal block created in board
def check_row_col_board():
    global score

    # Initialize rows and cols to be removed
    rows_to_remove = []
    cols_to_remove = []

    # Check for filled rows
    for i in range(10):
        if all(board[i][j] != 0 for j in range(10)):
            rows_to_remove.append(i)
    
    # Check for filled columns
    for j in range(10):
        if all(board[i][j] != 0 for i in range(10)):
            cols_to_remove.append(j)

    # Remove filled rows
    for row in rows_to_remove:
        for j in range(10):
            board[row][j] = 0
            colors[row][j] = "white"

    # Remove filled columns
    for col in cols_to_remove:
        for i in range(10):
            board[i][col] = 0
            colors[i][col] = "white"

    score += (len(rows_to_remove) * 10) + (len(cols_to_remove) * 10)

    if len(rows_to_remove) != 0 or len(cols_to_remove) != 0:
        return True
    else:
        return False

# Function to update the game board visually
def update_board(canvas, board_items):
    for row in range(10):
        for col in range(10):
            canvas.itemconfig(board_items[row][col], fill=colors[row][col])
    
    # Update the current score label
    current_score_label.config(text="Current Score: {}".format(score))

# Function to draw the blocks in hand below the board
def draw_blocks_in_hand(canvas, blocks_in_hand):
    # Clear the canvas of previously drawn blocks
    canvas.delete("blocks_in_hand")

    # Initialize draw variables
    block_size = 30
    start_row = 1
    last_x = 0

    # Calculate gap
    length = 0
    for block in blocks_in_hand:
        length += len(block[0])
    gap = (20 - length) // 4

    for block in blocks_in_hand:
        # Calculate the starting position of the block on the canvas
        start_x = last_x * block_size + gap * block_size
        start_y = start_row * block_size

        # Update last_x
        last_x = (start_x // 30) + len(block[0])

        # Draw the block on the canvas
        for row in range(len(block)):
            for col in range(len(block[0])):
                if block[row][col] == 1:
                    color = block.color
                    x0, y0 = start_x + col * block_size, start_y + row * block_size
                    x1, y1 = x0 + block_size, y0 + block_size
                    canvas.create_rectangle(x0, y0, x1, y1, fill=color, tags="blocks_in_hand")

# Function to play game
def play_game(canvas, board_items, blocks_in_hand_canvas):
    global score

    # Clear canva
    blocks_in_hand_canvas.delete("game_over_text")

    # Set score to 0
    score = 0

    # Function to handle game animation
    def animate():
        # Update the game board
        update_board(canvas, board_items)

        # Update the blocks in hand canvas
        draw_blocks_in_hand(blocks_in_hand_canvas, blocks_in_hand)

        # Update the main window to show the changes
        root.update()

    # Initialize blocks in hand
    blocks_in_hand = []

    # Generate first three blocks
    blocks_in_hand += random_blocks()

    # Animation
    animate()

    # Add time delay
    time.sleep(1)

    # While not game over
    while not game_over(blocks_in_hand):

        # While there are still remaining blocks in hand
        while len(blocks_in_hand) != 0:
            # Initialize index to choose block
            idx_block = -1

            # Initialize variable to restart search
            found_block = False

            # Try to put all blocks
            for row in range(10):
                # If restart search
                if found_block:
                    break

                # Check for every box
                for col in range(10):
                    for i, block in enumerate(blocks_in_hand):
                        # Check if a block can be placed in current row and col
                        if validation_check(block, row, col):
                            idx_block = i
                            found_block = True
                    
                    # If there is a block that can be added to board
                    if idx_block != -1:
                        # Add block to board
                        add_selected_shape(blocks_in_hand[idx_block], row, col)

                        # Remove block from hand
                        blocks_in_hand.pop(idx_block)

                        # Animation
                        animate()

                        # Add time delay
                        time.sleep(1)

                        # Check row and col board to get score
                        removed = check_row_col_board()

                        # Animation if needed
                        if removed:
                            animate()
                            # Add time delay
                            time.sleep(1)

                        # Start searching from beginning again with another block
                        break
            
            # Check if game over or there is still remaining blocks that can be placed
            if len(blocks_in_hand) != 0 and game_over(blocks_in_hand):
                break
        
        # Check if game still can continue
        if len(blocks_in_hand) == 0:
            blocks_in_hand += random_blocks()

            # Animation
            animate()

            # Add time delay
            time.sleep(1)
    
    # Print final score
    print("Final Score:", score)

    # Update label score
    current_score_label.config(text="Final Score: {}".format(score))

    # Display "Game Over" in the blocks_in_hand_canvas
    blocks_in_hand_canvas.delete("blocks_in_hand")
    blocks_in_hand_canvas.create_text(300, 100, text="Game Over", font=("Helvetica", 20), fill="red", tags="game_over_text")

    # Enable the "Start Game" button after the game ends
    start_button.config(state="normal")

# Function to start the game when the button is clicked
def start_game():
    global board
    global score
    global colors

    # Initialize board game
    board = [[0 for _ in range(10)] for _ in range(10)]

    # Initialize game states
    score = 0
    colors = [["white" for _ in range(10)] for _ in range(10)]

    # Disable the "Start Game" button
    start_button.config(state="disabled")

    # Create a 2D list to store the graphical items for each cell in the board
    board_items = [[None for _ in range(10)] for _ in range(10)]

    # Draw the initial game board
    for row in range(10):
        for col in range(10):
            board_items[row][col] = canvas.create_rectangle(col * 30, row * 30, (col + 1) * 30, (row + 1) * 30, fill="white")

    # Run the game loop in a separate thread
    import threading
    game_thread = threading.Thread(target=play_game, args=(canvas, board_items, blocks_in_hand_canvas))
    game_thread.start()

if __name__ == "__main__":
    # Create the main window
    root = tk.Tk()
    root.title("1010! Block Puzzle Game")

    # Dark mode theme colors
    bg_color = "#212121"  # Dark background color
    fg_color = "#FFFFFF"  # White foreground color
    canvas_color = "#424242"  # Dark color for the canvas
    
    # Set the background color of the root window
    root.configure(bg=bg_color)

    # Create a label for the title text
    title_label = tk.Label(root, text="1010! Block Puzzle Game\nby Michael Jonathan Halim | 13521124", font=("Helvetica", 14), bg=bg_color, fg=fg_color)
    title_label.pack()

    # Create a "Start" button
    start_button = tk.Button(root, text="Start Game", command=start_game, bg=bg_color, fg=fg_color)
    start_button.pack(pady=10)

    # Create a label to display the current score
    current_score_label = tk.Label(root, text="Current Score: 0", font=("Helvetica", 12), bg=bg_color, fg=fg_color)
    current_score_label.pack()

    # Create a canvas to display the game board
    canvas = tk.Canvas(root, width=300, height=300, bg=canvas_color)
    canvas.pack()
    
    # Create a canvas to display the blocks in hand
    blocks_in_hand_canvas = tk.Canvas(root, width=600, height=200, bg=canvas_color)
    blocks_in_hand_canvas.pack(pady=10)

    root.mainloop()