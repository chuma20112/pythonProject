from game_gonfig import *
from chess_items import *

clock = pg.time.Clock()
screen = pg.display.set_mode(WINDOW_SIZE)
screen.fill(BACKGROUND)

chessboard = ChessBoard(screen)

run = True
while run:
    clock.tick(FPS)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            run = False
        if event.type == pg.MOUSEBUTTONDOWN:
            chessboard.btn_down(event.button, event.pos)
        if event.type == pg.MOUSEBUTTONUP:
            chessboard.btn_up(event.button, event.pos)
        if event.type == pg.MOUSEMOTION:
            chessboard.drag(event.pos)

            