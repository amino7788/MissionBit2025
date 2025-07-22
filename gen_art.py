import random
from PIL import Image, ImageDraw


class ArtElement:
    def __init__(self, attributes):
        self.attributes = attributes

    def draw(self, draw_context):
        x, y = self.attributes["position"]
        color = self.attributes["color"]

        if "radius" in self.attributes:
            rx, ry = self.attributes["radius"]
            draw_context.ellipse([(x - rx, y - ry), (x + rx, y + ry)], fill=color)

        if "size" in self.attributes:
            w, h = self.attributes["size"]
            draw_context.rectangle((x, y, x + w, y + h), fill=color)


class Canvas:
    def __init__(self, width, height, background_color):
        self.width = width
        self.height = height
        self.background_color = background_color
        self.elements = []
        self.image = Image.new("RGB", (width, height), background_color)

    def add_element(self, element):
        self.elements.append(element)

    def render(self):
        draw = ImageDraw.Draw(self.image)
        for element in self.elements:
            element.draw(draw)
        self.image.show()
        self.image.save("output.png")


def main():
    canvas = Canvas(500, 500, (255, 255, 255))
    for _ in range(1000):
        attrs_circle = {
            "position": (random.randint(0, 500), random.randint(0, 500)),
            "radius": (random.randint(0, 60), random.randint(0, 60)),
            "color": (
                random.randint(20, 214),
                random.randint(15, 189),
                random.randint(10, 200),
            ),
        }
        attrs_rectangle = {
            "position": (random.randint(0, 500), random.randint(0, 500)),
            "size": (random.randint(0, 60), random.randint(0, 60)),
            "color": (
                random.randint(21, 216),
                random.randint(17, 185),
                random.randint(10, 200),
            ),
        }
        circle = ArtElement(attrs_circle)
        rectangle = ArtElement(attrs_rectangle)
        canvas.add_element(circle)
        canvas.add_element(rectangle)
    canvas.render()


main()
