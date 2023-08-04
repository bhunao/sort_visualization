import pyxel
from random import choice


pyxel.init(10, 18)

table = [[0 for _ in range(18)] for _ in range(10)]
piece = []
pos = [2, 4]
t = [
    [0, 1, 0],
    [1, 1, 1],
]
i = [[0, 0, 0, 0],]
piece = t.copy()


def get_blocks_pos(piece, pos):
    x, y = pos
    positions = []
    for i, line in enumerate(piece):
        for j, ll in enumerate(line):
            if ll == 1:
                positions.append((x+j, y+i))
    return positions


def adjust_piece():
    global piece, table, pos, t, i
    FALL_TIME = 10
    if pyxel.frame_count % FALL_TIME:
        return

    if len(piece) + pos[1] - 1 > 16:
        for x, y in get_blocks_pos(piece, pos):
            table[x][y] = 9
            pos = [5, 0]
            piece = i.copy()
        return
    pos[1] += 1


def draw():
    pyxel.cls(1)

    x, y = pos
    for x, y in get_blocks_pos(piece, pos):
        pyxel.pset(x, y, pyxel.frame_count % 15)

    for x, d1 in enumerate(table):
        for y, col in enumerate(d1):
            if col:
                pyxel.pset(x, y, col)


def update():
    global piece
    if pyxel.btnp(pyxel.KEY_W):
        pos[1] -= 1
    if pyxel.btnp(pyxel.KEY_S):
        pos[1] += 1
    if pyxel.btnp(pyxel.KEY_A):
        pos[0] -= 1
    if pyxel.btnp(pyxel.KEY_D):
        pos[0] += 1
    if pyxel.btnp(pyxel.KEY_SPACE):
        piece = list(zip(*piece[::-1]))
    adjust_piece()
    print(pos)


pyxel.run(update, draw)
