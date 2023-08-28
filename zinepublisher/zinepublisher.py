import fitz
import os
from PIL import Image

def pdf2pngs(src, destination, dpi=300, zoom_factor=72):
    zoom = dpi / zoom_factor
    pdf = fitz.open(src)
    for page in pdf:
        png = page.get_pixmap(dpi=dpi)
        png_path = f"{page.number}.png"
        png_path = os.path.join(destination, png_path)
        png.save(png_path)

def swap_sides(src, dest):
    img_in = Image.open(src)
    left_dims = (0, 0, img_in.width // 2, img_in.height)
    right_dims = (img_in.width // 2, 0, img_in.width, img_in.height)
    left_crop = img_in.crop(left_dims)
    right_crop = img_in.crop(right_dims)
    img_in.paste(right_crop, left_dims)
    img_in.paste(left_crop, right_dims)
    img_in.save(os.path.join(dest, "img.png"))

if __name__ == "__main__":
    src = "./Files/Queerplatonica Zine.pdf"
    dest_temp = "./Files/temp_pngs"
    os.mkdir(dest_temp)
    pdf2pngs(src, dest_temp)
    dest_final = "./Files/final_pngs"
    os.mkdir(dest_final)

    swap_sides(os.path.join(dest_temp, "1.png"), dest_final)
