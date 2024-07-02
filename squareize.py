""" To turn non-square pictures into square pictures by adding white bars, mostly for instagram """

from PIL import Image
import os


class ImageEditor:
    def __init__(self, src):
        self.src = src
        self.img = Image.open(src)

    def squareize(self, aspect_ratio=1, color=(255, 255, 255)):
        """Corrects an image's aspect ratio by adding colored bars bars"""

        width, height = self.img.size
        if width > height:
            new_width = int(height*aspect_ratio)
            new_height = height
        else:
            new_width = width
            new_height = int(width/aspect_ratio)

        if width/height < aspect_ratio:
            """Additional width needed - add vertical bars"""
            if width > height:
                new_width = int(height*aspect_ratio)
                new_height = height
            img_new = Image.new("RGB", (new_width, new_height), color)
            img_new.paste(self.img, (int(new_width - width)//2,0))
        elif width/height > aspect_ratio:
            """Additional height needed - add horizontal bars"""
            new_width = width
            new_height = int(width/aspect_ratio)
            img_new = Image.new("RGB", (new_width, new_height), color)
            img_new.paste(self.img, (0,int(new_height - height)//2))
        else:
            """Aspect ratios already match, do nothing"""
            pass
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
    src = "sample-files/src"
    dst = "sample-files/dst"
    for file in os.listdir(src):
        ime = ImageEditor(os.path.join(src, file))
        ime.squareize(aspect_ratio=16/9)
        ime.img.save(os.path.join(dst, file))
