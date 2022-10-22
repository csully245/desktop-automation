""" To turn non-square pictures into square pictures by adding white bars, mostly for instagram """

from PIL import Image
import os


class ImageEditor:
    def __init__(self, src):
        self.src = src
        self.img = Image.open(src)

    def squareize(self):
        """Turns a non-square picture into a square picture by adding white bars"""

        width, height = self.img.size
        dimension = max((width, height))
        img_new = Image.new("RGB", (dimension, dimension), (255, 255, 255))
        if width > height:
            img_new.paste(self.img, (0, (width - height) // 2))
        else:
            # TODO: never goes down this path. Why is width always the larger value?
            img_new.paste(self.img, ((height - width) // 2, 0))
        self.img = img_new

    def overwrite(self):
        self.img.save(self.src)

    def edit_dir(src, dest, func):
        """Applies function to all files in folder"""
        for file in os.listdir(src):
            ime = ImageEditor(os.path.join(src, file))
            func(ime)
            ime.img.save(os.path.join(dest, file))


if __name__ == "__main__":
    ImageEditor.edit_dir(
        "C:/Users/jsull/Downloads/fallpics-raw",
        "C:/Users/jsull/Downloads/fallpics-edit",
        ImageEditor.squareize,
    )
