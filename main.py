import pyxel


coisas = []
for n in "01234":
    for p1 in "CDEFGAB":
        coisas.append(f"{p1}{n}")


pyxel.init(200, 150)
screen_range = range(10, pyxel.width-10, pyxel.width//len(coisas)-1)

bars_size = [pyxel.rndi(0, 100) for size in screen_range][::-1]
sorted_sizes = sorted(bars_size)
xses = [x for x in screen_range]
shiny_bar = 0


def bar(pos: int, size: int, col=15):
    pyxel.rect(
        x=pos,
        y=pyxel.height-20-size,
        w=3,
        h=size,
        col=col,
    )


def play_bar():
    global shiny_bar

    sound_i = round(shiny_bar*.34)
    pyxel.sound(0).set(
        coisas[sound_i],
        "p",
        "6",
        "v",
        25,
    )
    pyxel.play(0, 0)


def kinda_of_sort(lista: list):
    global shiny_bar

    lst_len = len(lista)
    for i in range(lst_len):
        for j in range(i, lst_len):
            shiny_bar = j
            if pyxel.sin(lista[i]) > pyxel.sin(lista[j]):
                lista[i], lista[j] = lista[j], lista[i]
                print(lista[i], lista[j])
                play_bar()
                return


def draw():
    global bars_size, shiny_bar

    pyxel.cls(1)

    for i, (size, x) in enumerate(zip(bars_size, xses)):
        if i == shiny_bar - 1:
            col = pyxel.frame_count % 15
        else:
            col = 15
        bar(x, size, col=col)


def update():
    global shiny_bar, bars_size
    if bars_size == sorted_sizes:
        pass
    elif pyxel.frame_count % 3 == 0:
        # shiny_bar = (shiny_bar + 1) % len(bars_size)
        kinda_of_sort(bars_size)


pyxel.run(update, draw)
