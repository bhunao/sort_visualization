import pyxel


X, Y = 130, 110
B_SIZE = 5
pyxel.init(X, Y)


bars = [x for x in range(0, 100, 100//20)]
bars = [pyxel.rndi(0, 100) for _ in range(20)]
print(bars)


def _sort():
    global bars
    size = len(bars)
    last = bars[-1]
    print("_sort")
    for i in range(0, size-2):
        if last < bars[i]:
            yield
            last, bars[i] = bars[i], last


def draw():
    pyxel.cls(1)
    for i, b in enumerate(bars):
        w, h = B_SIZE, b
        x, y = (i+1) * (B_SIZE+1), 90-h
        pyxel.rect(x, y, w, h, 10)
        pyxel.text(x, y, str(b), 9)


def update():
    global bars
    if pyxel.frame_count % 10:
        return
    _sort()
    print("update")


pyxel.run(update, draw)
