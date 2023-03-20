from PIL import Image, ImageFilter

img = Image.open('./Pokedex/pikachu.jpg')

filtered_img = img.filter(ImageFilter.BLUR)
filtered_img.save("blur.png", "png")

filtered_img = img.convert('L')
filtered_img.save("grey.png", "png")


print(img.format, img.size, img.mode)