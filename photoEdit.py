from PIL import Image, ImageEnhance, ImageFilter, ImageDraw
import os

path = r"D:/Code/Mini Python Projects/imgs"
pathOut = r"D:/Code/Mini Python Projects/editedImgs"

dir_list = os.listdir(path)
print("Files in ", path,)
print(dir_list)

for filename in os.listdir(path):
    img = Image.open(f"{path}/{filename}")

    edit = img.filter(ImageFilter.SHARPEN).convert('L').rotate(-90)

    #enhancer
    factor = 1.5
    enhancer = ImageEnhance.Contrast(edit)
    edit = enhancer.enhance(factor)

    clean_name = os.path.splitext(filename)[0]

    edit.save(f'.{pathOut}/{clean_name}_edited.jpg')

