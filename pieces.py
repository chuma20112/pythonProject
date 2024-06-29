import pygame as pg
from game_gonfig import *


class Piece(pg.sprite.Sprite):
    def __init__(self, cell_size: int, color: str, field_name: str, file_posfix: str):
        super().__init__()
        picture = pg.image.load(PIECE_PATH + color + file_posfix).convert_alpha()
        self.image = pg.transform.scale(picture, (cell_size, cell_size))
        self.rect = self.image.get_rect()
        self._color = color
        self.field_name = field_name

    def move_to_cell(self, cell):
        self.rect = cell.rect.copy()
        self.field_name = cell.field_name

class King(Piece):
    def __init__(self, cell_size: int, color: str, field: str):
        super().__init__(cell_size, color, field, '_king.png')


class Queen(Piece):
    def __init__(self, cell_size: int, color: str, field: str):
        super().__init__(cell_size, color, field, '_queen.png')


class Rook(Piece):
    def __init__(self, cell_size: int, color: str, field: str):
        super().__init__(cell_size, color, field, '_rook.png')


class Bishop(Piece):
    def __init__(self, cell_size: int, color: str, field: str):
        super().__init__(cell_size, color, field, '_bishop.png')


class Knight(Piece):
    def __init__(self, cell_size: int, color: str, field: str):
        super().__init__(cell_size, color, field, '_knight.png')


class Pawn(Piece):
    def __init__(self, cell_size: int, color: str, field: str):
        super().__init__(cell_size, color, field, '_pawn.png')
