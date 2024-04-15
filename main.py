

import sys, random, pygame
from pygame.locals import *

FPS = 30
WINDOWWIDTH = 640
WINDOWHEIGHT = 480
BOXSIZE = 10
assert WINDOWWIDTH % BOXSIZE == 0, 'Window width must be a multiple of cell size.'
assert WINDOWHEIGHT % BOXSIZE == 0, 'Window height must be a multiple of cell size.'
NUM_CELLS_X = WINDOWWIDTH // BOXSIZE
NUM_CELLS_Y = WINDOWHEIGHT // BOXSIZE

GREY = (128,128,128)
NAVYBLUE = (60, 60, 100)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
ORANGE = (255, 128, 0)
PURPLE = (255, 0, 255)
CYAN = (0, 255, 255)

BGCOLOR = GREY


class Box: # funguje to iba bez box dovtedy kym ho budeme definovat


class Board:
    def __init__(self):
        self.board = []
        self.boardwidth = 5
        self.boardheight = 5
        self.xmargin = (WINDOWWIDTH - (self.boardwidth * BOXSIZE)) // 2
        self.ymargin = (WINDOWHEIGHT - (self.boardheight * BOXSIZE)) // 2
        self.num_mines = 5    # Number of mines generated
        self.game_ended = False

    def generate_mines(self):
        positions = [(x, y) for x in range(self.boardwidth) for y in range(self.boardheight)]
        mine_positions = random.sample(positions, self.num_mines)
        for x, y in mine_positions:
            self.grid[y][x] = 'X'    #Marks mines on the board




    def box_is_revealed(self, coordinates):
        return self.board[coordinates[0]][coordinates[1]].face_up

    def get_box(self, coordinates):
        return self.board[coordinates[0]][coordinates[1]]



def main():
    global FPSCLOCK, DISPLAY_SURFACE
    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    DISPLAY_SURFACE = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    pygame.display.set_caption('MINESWEEPER')

    mouse_coordinates = 0, 0
    game_board = Board()
    game_board.prepare_board()
    
    while True:
        mouse_clicked = False
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                terminate()
            elif event.type == MOUSEMOTION:
                mouse_coordinates = event.pos
            elif event.type == MOUSEBUTTONUP:
                mouse_coordinates = event.pos
                mouse_clicked = True
        
        current_box = get_box_xy(game_board, mouse_coordinates)

def get_left_top_coordinates(game_board, box):
    """Convert game_board coordinates to pixel coordinates."""
    x, y = box[0], box[1]
    left = x * BOXSIZE + game_board.xmargin
    top = y * BOXSIZE + game_board.ymargin
    return left, top

def get_box_xy(game_board, coordinates):
    """Convert pixel coordinates to game_board coordinates."""
    for box_xy in ((x, y) for x in range(game_board.boardwidth) for y in range(game_board.boardheight)):
        left, top = get_left_top_coordinates(game_board, box_xy)
        box_rect = pygame.Rect(left, top, BOXSIZE, BOXSIZE)
        if box_rect.collidepoint(coordinates):
            return box_xy
    return None

def draw_board(game_board):
    """Draw all of the boxes in their covered or revealed state."""
    DISPLAY_SURFACE.fill(0, 0, 0)
    for box in ((x, y) for x in range(game_board.boardwidth) for y in range(game_board.boardheight)):
        left, top = get_left_top_coordinates(game_board, box)
        if not game_board.box_is_revealed(box):  # Draw a covered box
            pygame.draw.rect(DISPLAY_SURFACE, BGCOLOR, (left, top, BOXSIZE, BOXSIZE))
        else:  # Draw the (revealed) icon
            continue
            #here will probably be revealed boxes´ looks - mines or numbers

def end_screen(game_board):
    
    font_object = pygame.font.Font("freesansbold.ttf", 32)
    text_surface_object = font_object.render("Congratulations!", True, (255,0,0))
    text_rect_object = text_surface_object.get_rect()
    text_rect_object = (200, 50)
    text_surface_object1 = font_object.render("YoU WoN YAY!!!", True, (255,0,0))
    text_rect_object1 = text_surface_object1.get_rect()
    text_rect_object1 = (200, 100)
    text_surface_object2 = font_object.render("Wanna play again?", True, (255,0,0))
    text_rect_object2 = text_surface_object2.get_rect()
    text_rect_object2 = (170, 150)
    DISPLAY_SURFACE.fill(WHITE)
    DISPLAY_SURFACE.blit(text_surface_object, text_rect_object)
    DISPLAY_SURFACE.blit(text_surface_object1, text_rect_object1)
    DISPLAY_SURFACE.blit(text_surface_object2, text_rect_object2)
    
    pygame.draw.rect(DISPLAY_SURFACE, (0,255,0), (220, 250, 60, 60)) # 320 is width/2
    pygame.draw.rect(DISPLAY_SURFACE, (255,0,0), (380, 250, 60, 60))
    yes_button = (220, 250, 60, 60)
    no_button = (380, 250, 60, 60)
    pygame.display.update()
    
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
                pygame.display.update()
            elif event.type == MOUSEMOTION:
                mouse_coordinates = event.pos
            elif event.type == MOUSEBUTTONUP:
                mouse_coordinates = event.pos
                mouse_clicked = True
                if mouse_coordinates[0] >= yes_button[0] and mouse_coordinates[0] <= yes_button[0] + yes_button[2] and mouse_coordinates[1] >= yes_button[1] and mouse_coordinates[1] <= yes_button[1] + yes_button[3]:
                    print("yes_button")
                    main()
                elif mouse_coordinates[0] >= no_button[0] and mouse_coordinates[0] <= no_button[0] + no_button[2] and mouse_coordinates[1] >= no_button[1] and mouse_coordinates[1] <= no_button[1] + no_button[3]:
                    print("no_button")
                    pygame.quit()
                    exit()
                    pygame.display.update()

def terminate():
    """Exit the program."""
    pygame.quit()
    sys.exit()


if __name__ == '__main__':
    main()
