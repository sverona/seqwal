from argparse import ArgumentParser
from random import gammavariate

from PIL import Image, ImageDraw

def random_walk(seq, rand=lambda: int(gammavariate(30, 2))):
    idx = 0

    while True:
        try:
            yield tuple(seq[idx])
        except IndexError:
            break

        idx += 1
        idx += int(rand())

def __main__():
    img = Image.new('RGBA', (1920, 1080), color=(255, 255, 255, 255))
    border = 50

    seq = [tuple(int(i) for i in line.split())
           for line in open("b262626.txt").read().split("\n") if line]

    xmax = max(x for x, y in seq)
    ymax = max(y for x, y in seq)
    pen = ImageDraw.Draw(img)

    def coords(point):
        x, y = point
        return (border + (1920 - 2 * border) * x / xmax,
                1080 - border - (1080 - 2 * border) * y / ymax)

    for _ in range(10):
        points = tuple(random_walk(seq))
        points = [coords(point) for point in points]
        pen.line(points, fill=(170, 170, 170, 255), width=3)

    for point in seq:
        x, y = coords(point)
        pen.ellipse([x - 5, y - 5, x + 5, y + 5], fill=(0, 0, 0, 255))

    img.show()

if __name__ == "__main__":
    __main__()
